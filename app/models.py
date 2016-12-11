from django.db import models

# Create your models here.
class Post(models.Model):
	postis_satauri=models.CharField(max_length=50)
	postis_contenti=models.TextField(max_length=20000)
	sheqmnis_dro=models.DateTimeField('შექმნის დრო')
	surati=models.ImageField(upload_to='app')
	ganaxlebis_dro=models.DateTimeField('განახლების დრო')

	def get_medium_desc(self):
		k=0
		text=""
		for i in self.postis_contenti[:300]:
			if k%111==0:
				text+="\n"
			text+=i
			k+=1
		return text+" . . ."	

	def get_short_desc(self):
		return self.postis_contenti[:10]+" . . ."

	def __str__(self):
		return self.postis_satauri


class Comment(models.Model):
	posti=models.ForeignKey(Post,on_delete=models.CASCADE)
	komentari=models.CharField(max_length=200)
	def __str__(self):
		return self.komentari
