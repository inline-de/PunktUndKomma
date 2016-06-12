from django.db import models
import keras
from random import randint
from keras.models import Sequential
from keras.preprocessing import text, sequence
from keras.layers import Dense, Activation, Embedding, LSTM, Masking
from keras.optimizers import SGD
import numpy as np

# Create your models here.

RESULTS = {
    '.': 1,
    ',': 2,
    '!': 3,
    '?': 4,
}


def clean(string):
    return string.replace(".", "").replace(",", "").replace("!", "").replace("?", "")


def last_char_to_result(last_char):
    i = RESULTS.get(last_char, 0)
    result = [0] * (len(RESULTS) + 1)
    result[i] = 1
    return result


class Dataset():
    def __init__(self, maxlen, max_features):
        self.max_features = max_features
        self.maxlen = maxlen
        dataset = open("dataset.txt")
        all_data = dataset.read().split()
        self.all_words = list(filter(None, all_data))  # remove empty strings
        print("Total number of words: {}".format(len(self.all_words)))

    def word_count(self):
        return len(self.all_words)

    def load_sample(self, lookahead, skip=True):
        sentence = []  # ['word','word',...]
        result = []  # [0,1,0,0,0] #6
        upper_limit = self.word_count() - self.maxlen - 2
        offset = randint(0, max(self.word_count(), upper_limit))
        num_words = randint(2, self.maxlen)
        sentence = self.all_words[offset:(offset + num_words)]
        if sentence == [] or sentence[-1] == '':
            return self.load_sample(skip)
        if len(sentence) <= lookahead:
            return self.load_sample(lookahead, skip)
        last_char = sentence[-1 - lookahead][-1]
        result = last_char_to_result(last_char)
        if skip and (RESULTS.get(last_char, 0) == 0) and (randint(0, 100) > 30):
            return self.load_sample(lookahead, skip)
        sentence = list(map(clean, sentence))
        return " ".join(sentence), result

    def transform(self, sentence):
        x = text.one_hot(sentence, self.max_features, lower=True, filters=" ")
        x_new = [[0 if t != i else 1 for i in range(self.max_features)] for t in x]

        null_vector = [0] * self.max_features
        pad_size = self.maxlen - len(x_new)
        for i in range(pad_size):
            x_new.append(null_vector)
        return x_new

    def create(self, size, skip=True):
        X = []
        y = []
        for iteration in range(0, size):
            sentence, result = self.load_sample(skip)
            X.append(self.transform(sentence))
            y.append(result)
        return np.array(X), np.array(y)


class Predictor():
    lookahead = 5
    maxlen = 80  # cut texts after this number of words (among top max_features most common words)
    max_features = 200  # Anzahl der Wörter
    trainset_size = 100
    testset_size = 40
    epochs = 30

    def  __init__(self):
        self.dataset = Dataset(self.maxlen,self.max_features)
        self.create_model()
        self.train()

    def create_model(self):
        self.model = Sequential()
        self.model.add(Masking(mask_value=0, input_shape=(self.maxlen, self.max_features)))
        # model.add(Embedding(max_features, 128, input_length=maxlen, dropout=0.2))
        self.model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
        self.model.add(Dense(len(RESULTS) + 1))
        # model.add(Activation('relu'))
        # try using different optimizers and different optimizer configs
        self.model.compile(loss='binary_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

    def train(self):
        X, y = self.dataset.create(self.trainset_size)
        print("Start training with (sentence * words * kind-of-word) = {}".format(X.shape))
        self.model.fit(X, y, nb_epoch=self.epochs)

    def predict(self, data):
        y = self.model.predict(np.array([self.dataset.transform(data)]))[-1]
        return {'foo': 'bar', "data": data, "result": y}
