from django.db import models

class News(models.Model):
	picture = models.CharField(max_length=20, blank=True)
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now=True)
	content = models.CharField(max_length=3000)
