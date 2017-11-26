from django.db import models

# Create your models here.
class Course(models.Model):
	"""docstring for Course"""
	code = models.CharField(max_length=10, null=True)
	course = models.CharField(max_length=50)
	course_image = models.ImageField(upload_to='courses/', null=True, blank=True)
	description = models.CharField(max_length=100)
	url = models.URLField()