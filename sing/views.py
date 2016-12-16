from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.
def create_account(request):
	form=UserForm()
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()


			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("app:index")

	return render(request,"sing/sing.html",{"form":form})



def log_out(request):
	logout(request)
	return HttpResponse("you are log_out")

def sing_in(request):
	form=SingInForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			pass
	return render()