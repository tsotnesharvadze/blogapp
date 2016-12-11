from django import forms
from .models import User
class SingInForm(forms.Form):
	user_email= forms.CharField(label='email', max_length=20)
	user_password= forms.CharField(label='password', max_length=40)
	class Meta:
		model= User
		fields=('email','password')


class SingUpForm(forms.Form):
	user_email= forms.CharField(label='email', max_length=20)
	user_password= forms.CharField(label='password', max_length=40)
	user_saxeli=forms.CharField(label="saxeli", max_length=20)
	user_gvari=forms.CharField(label="gvari", max_length=20)
	class Meta:
		model= User
		fields=('email','password','saxeli','gvari')