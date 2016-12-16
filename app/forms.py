from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['komentari']
	# new_comment = forms.CharField(label='კომენტარი ', max_length=100)

	# def clean_email(self):
	# 	comment=self.cleaned_data.get("kometari")
	# 	return comment