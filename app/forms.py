from django import forms

class PostisForm(forms.Form):
	postfile=forms.FileField(label='select a file',
							  help_txt="maxsimluri zoma 42 mb",
							  )