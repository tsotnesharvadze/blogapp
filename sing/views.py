from django.shortcuts import render
from .models import User
from .forms import SingUpForm
# Create your views here.
def index(request):
	form1=SingUpForm()
	if request.method=="POST":
		q=User(
			saxeli=request.POST.get("user_saxeli"),
			gvari=request.POST.get("user_gvari"),
			email=request.POST.get("user_email"),
			password=request.POST.get("user_password"))
		q.save()
	return render(request,"sing/sing_in.html",{"form1":form1})