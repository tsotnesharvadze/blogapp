from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _
class CommentForm(forms.Form):
<<<<<<< HEAD
	class Meta:
		model = Comment
		fields = ['course']
	new_comment = forms.CharField(label='კომენტარი ', max_length=100)
=======
    new_comment = forms.CharField(label=_('კომენტარი '), max_length=100)
    class Meta:
>>>>>>> 81a5fbffaf0ec4f216d57a66d547c4dc56ebc95a

	def clean_email(self):
		comment=self.cleaned_data.get("kometari")
		return comment