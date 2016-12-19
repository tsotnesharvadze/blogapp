from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserInForm,UserUpForm,New_passwordForm
from .util import get_code,get_id
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views import View
# Create your views here.
def create_account(request):
	form=UserUpForm()

	if request.method=="POST":
		form=UserUpForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			email=form.cleaned_data['email']
			user.set_password(password)
			user.is_active=False
			user.save()




			# user=authenticate(username=username,password=password)
			
			code=get_code(user.id)
			url="http://{}/activate/{}".format(request.META['HTTP_HOST'],str(code))

			from_email = settings.EMAIL_HOST_USER
			subject="email verification"
			message='gadadit linkze tqveni account -is gasaaqtiureblad : '


			text_content = '{0}{1}'.format(message, url)
			html_content = '<p>{0}<a href="{1}">{1}</a><p>'.format(message, url)
		 
			msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			# if user is not None:
			# 	if user.is_active:
			# 		login(request,user)
			# 		return redirect("app:index")

	return render(request,"sing/singup.html",{"form":form})



def log_out(request):
	logout(request)
	return redirect("sing:sing_in")

def sing_in(request):
	form=UserInForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("app:index")

	return render(request,"sing/singin.html",{"form":form})

def activate(request,user_code):
	user_id=get_id(int(user_code))
	user=User.objects.get(id=user_id)
	
	if user is not None:
		user.is_active=True
		user.save()
		login(request,user)
		return redirect("app:index")

	return HttpResponse("sheni imeili ver gaaqtiurda :{}".format(user_code))


class new_password(View):
	def post(self,request,*args,**kwargs):
		form=New_passwordForm(request.POST)
		if form.is_valid():
			password=form.cleaned_data['password']
			confpassword=form.cleaned_data['confpassword']
			if password==confpassword:

				user=request.user
				if user.is_active:
					user.set_password(password)
					user.save()
				else:
					return HttpResponse("პაროლი წარმატებით შეიცვალა")
			
		return HttpResponse("გთხოვთ სწორად შეავსოთ ველები .. ")

	def get(self,request,*args,**kwargs):
		form=New_passwordForm()
		context={
		"form":form,
		"user":request.user
		}
		return render(request,"sing/new_password.html",context)