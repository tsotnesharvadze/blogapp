from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
# Create your views here.
def index(request):
	return HttpResponse("zdarova")

def posti(request,posti_id):
	return HttpResponse("პიროვნება : {}".format(Post.objects.get(pk=posti_id)))


def srulad(request,posti_id):
	return HttpResponse(Post.objects.all()[int(posti_id)-1].postis_contenti)