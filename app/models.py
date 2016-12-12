from django.db import models

# Create your models here.
class Post(models.Model):
	postis_satauri=models.CharField("სათაური",max_length=50)
	postis_contenti=models.TextField("კონტენტი")
	sheqmnis_dro=models.DateTimeField('შექმნის დრო')
	surati=models.ImageField("სურათი",upload_to='app')
	ganaxlebis_dro=models.DateTimeField('განახლების დრო')


	def get_medium_desc(self):
		return self.postis_contenti[:300]+" . . ."

	def get_short_desc(self):
		return self.postis_contenti[:10]+" . . ."

	def __str__(self):
		return self.postis_satauri
	class Meta:
		verbose_name="პოსტები"

class Comment(models.Model):
	posti=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="პოსტი")
	komentari=models.CharField(verbose_name="კომენტარი",max_length=200)
	def __str__(self):
		return self.komentari

	class Meta:
		verbose_name="კომენტარები"
