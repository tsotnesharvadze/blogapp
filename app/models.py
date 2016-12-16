from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# Create your models here.
class Comment(models.Model):
	#posti=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name=_("პოსტი"),null=True)
	komentari=models.CharField(verbose_name=_("კომენტარი"),max_length=200)
	def __str__(self):
		return self.komentari

	class Meta:
		verbose_name_plural=_("კომენტარები")
		verbose_name=_("კომენტარი")
class Post(models.Model):
	postis_satauri=models.CharField(verbose_name=_("სათაური"),max_length=50)
	postis_contenti=models.TextField(verbose_name=_("კონტენტი"))
	sheqmnis_dro=models.DateTimeField(verbose_name=_('შექმნის დრო'),auto_now_add=True, blank=True)
	surati=models.ImageField(verbose_name=_("სურათი"),upload_to='app')
	ganaxlebis_dro=models.DateTimeField(verbose_name=_('განახლების დრო'),auto_now_add=True, blank=True)
	comment= models.ManyToManyField(Comment,verbose_name=_("კომენტარი"))

	def get_medium_desc(self):
		return self.postis_contenti[:300]+" . . ."

	def get_short_desc(self):
		return self.postis_contenti[:10]+" . . ."

	def __str__(self):
		return self.postis_satauri
	class Meta:
		verbose_name_plural=_("პოსტები")
		verbose_name=_("პოსტი")
