FROM ubuntu:latest
MAINTAINER Michael Sprauer "ms@inline.de"
RUN apt-get update -y
RUN apt-get install -y tar git curl nano build-essential \
    python3.5 python3.5-dev python-distribute python3-pip python3-numpy \
    python3-h5py


ENTRYPOINT ["python3"]
EXPOSE 8000

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app
