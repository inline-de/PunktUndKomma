FROM ubuntu:latest
MAINTAINER Michael Sprauer "ms@inline.de"
RUN apt-get update -y
RUN apt-get install -y tar git curl nano build-essential \
    python3.5 python3.5-dev python-distribute python-pip3 python3-numpy \
    python3-h5py
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
EXPORT 8000

CMD manage.py runserver 0.0.0.0:8000