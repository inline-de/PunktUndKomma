# Talk urls
from django.conf.urls import patterns, url
from basic import views

urlpatterns = [
    url(r'^$', views.home),

    # api
    url(r'^api/v1/predict$', views.predict),
]
