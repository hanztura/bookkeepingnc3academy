from django.db import models

# Create your models here.
class Certification(models.Model):
	"""docstring for Certification"""
	num_code = models.IntegerField(null=False)
	certification = models.CharField(max_length=50)
	alias = models.CharField(max_length=50, null=True)
	issuing_body = models.CharField(max_length=50, null=True)
	
	
class Topic(models.Model):
	"""docstring for Topic"""
	certification = models.ForeignKey(Certification, related_name='topics')
	order = models.IntegerField(null=False)
	topic = models.CharField(max_length=50)
	description = models.CharField(max_length=100, null=False)

