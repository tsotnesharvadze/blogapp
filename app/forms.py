from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _
class CommentForm(forms.Form):
    new_comment = forms.CharField(label=_('კომენტარი '), max_length=100)
    class Meta:

    	model= Comment
    	fields=('kometari',)
    	#pagination