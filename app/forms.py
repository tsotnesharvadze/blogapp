from django import forms
from .models import Comment,Post
from django.utils.translation import ugettext_lazy as _
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['komentari']

class PostForm(forms.ModelForm):
	class Meta:
		model =Post
		fields=["postis_satauri","postis_contenti","surati"]
		