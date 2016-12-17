from django import forms
from django.contrib.auth.models import User


class UserUpForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'pass',
		}))
	class Meta:
		model=User
		fields=['username','email','password']

class UserInForm(forms.Form):
	username=forms.CharField(max_length=50)
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'pass',
		}))

	class Meta:
		fields=['username','password']
