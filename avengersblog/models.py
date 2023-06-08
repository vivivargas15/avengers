from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
	title= models.CharField(max_length=200)
	text=models.TextField()
	time=models.CharField(max_length=200)

	def __str__(self):
		return self.title


