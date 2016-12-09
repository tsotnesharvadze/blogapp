from django import forms
from .models import Comment
class CommentForm(forms.Form):
    new_comment = forms.CharField(label='Your name', max_length=100)
    class Meta:
    	model= Comment
    	fields=('kometari',)
    	#pagination