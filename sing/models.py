from django.db import models

# Create your models here.
class User(models.Model):
	saxeli=models.CharField(max_length=20)
	gvari=models.CharField(max_length=20)
	email=models.EmailField(max_length=40)
	password=models.CharField(max_length=20)

	def __str__(self):
		return self.saxeli ,self.gvari