from django.db import models

# setelah buat ini python manage.py makemigrations
# python manage.py migrate
# maka table akan terbuat

# Create your models here.
class User(models.Model):
	nama_depan = models.CharField(max_length=128)
	nama_belakang = models.CharField(max_length=128)
	email = models.EmailField(max_length=264, unique=True)

class Topic(models.Model):
	top_name = models.CharField(max_length=264, unique=True)

	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage)
	date = models.DateField()

	def __str__(self):
		return str(self.date)
