from django.db import models

# Create your models here.

class Destination(models.Model):

	name = models.CharField(max_length=100 , null=True)
	img=models.ImageField(null=True , blank=True)
	desc= models.TextField(null=True)
	 