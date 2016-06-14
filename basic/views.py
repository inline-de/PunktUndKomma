from json import JSONEncoder

from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

from basic.models import Predictor

predictor = Predictor()

def home(request):
    context = {
        "lookahead": predictor.lookahead,
        "maxlen": predictor.maxlen,
        "max_features": predictor.max_features,
        "trainset_size": predictor.trainset_size,
        "testset_size": predictor.testset_size,
        "epochs": predictor.epochs,
        "loss": predictor.model.loss,
        "test_score": predictor.test_score,
        "test_accuracy": predictor.test_accuracy,
    }
    template = loader.get_template('basic/index.html')
    return HttpResponse(template.render(context, request))


def predict(r):
    json = predictor.predict(r.GET.get('text'))
    return JsonResponse(json, JSONEncoder)
