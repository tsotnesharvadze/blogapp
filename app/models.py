from django.db import models

# Create your models here.
class Post(models.Model):
	postis_contenti=models.CharField(max_length=2000)
	postis_satauri=models.CharField(max_length=50)
	sheqmnis_dro=models.DateTimeField('შექმნის დრო')
	surati=models.ImageField(upload_to='app')
	ganaxlebis_dro=models.DateTimeField('განახლების დრო')

	def get_medium_desc(self):
		return self.postis_contenti[:200]+" . . ."	

	def get_short_desc(self):
		return self.postis_contenti[:10]+" . . ."

	def __str__(self):
		return self.postis_satauri


class Comment(models.Model):
	posti=models.ForeignKey(Post,on_delete=models.CASCADE)
	komentari=models.CharField(max_length=200)
	def __str__(self):
		return self.komentari
