from django.conf.urls import url
from .views import *

app_name="sing"



urlpatterns=[
 url(r'^$',create_account,name="create_account"),
 url(r'^log_out/',log_out,name="log_out"),
 url(r'^sing_in/',sing_in,name="sing_in"),
# url(r'^(?P<posti_id>[0-9]+)/$',posti,name="posti"),
# url(r'^(?P<posti_id>[0-9]+)/srulad/$',srulad,name="srulad"),




]