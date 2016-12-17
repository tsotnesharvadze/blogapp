from django.conf.urls import url
from .views import *

app_name="sing"



urlpatterns=[
 url(r'^$',sing_in,name="sing_in"),
 url(r'^create_account/$',create_account,name="create_account"),
 url(r'^log_out/$',log_out,name="log_out"),
 url(r'^activate/(?P<user_code>[0-9]+)/$',activate,name="activate"),

# url(r'^(?P<posti_id>[0-9]+)/$',posti,name="posti"),
# url(r'^(?P<posti_id>[0-9]+)/srulad/$',srulad,name="srulad"),




]