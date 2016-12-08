from django.conf.urls import url
from .views import *

app_name="app"



urlpatterns=[
url(r'^$',index,name="index"),

url(r'^(?P<posti_id>[0-9]+)/$',posti,name="posti"),
url(r'^(?P<posti_id>[0-9]+)/srulad/$',srulad,name="srulad"),



]