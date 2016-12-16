from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
# Create your views here.
def index(request):
	form1=UserForm()
	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleane_date['username']
			password=form.cleane_date['password']
			user.set_password(password)
			user.save()


			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("app:index")

	return render(request,"sing/sing.html",{"form":form})