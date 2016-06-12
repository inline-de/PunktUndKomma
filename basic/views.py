from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader

from basic.models import Predictor

predictor = Predictor()

def home(request):
    context = {}
    template = loader.get_template('basic/index.html')
    return HttpResponse(template.render(context, request))


def predict(r):
    json = predictor.predict(r.data)
    return JsonResponse(json)
