from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
	user = models.OneToOneField(User, null=True)
	first_name_chinese = models.CharField(max_length=7, null=True)
	last_name_chinese = models.CharField(max_length=5, null=True)
	link = models.CharField(max_length=50, blank=True)
	status = models.CharField(max_length=20)
	thesis = models.CharField(max_length=50, blank=True)
	thesis_chinese = models.CharField(max_length=30, blank=True)
	gyear = models.CharField(max_length=4, blank=True)
	degree = models.CharField(max_length=20)
	picture = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.user.username

class Collaborator(models.Model):
	name = models.CharField(max_length=20)
	link = models.CharField(max_length=50, blank=True)
	department = models.CharField(max_length=40)
	country = models.CharField(max_length=10)

	def __str__(self):
		return self.name