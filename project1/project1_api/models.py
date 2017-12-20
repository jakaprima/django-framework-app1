#disini taruh store application data models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager




# Create your models here.

class UserProfileManager(BaseUserManager):
	""" membantu django bekerja dengan custom model """
	def create_user(self, email, name, password=None):
		if not email:
			raise ValueError('user harus memiliki email')

		email = self.normalize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, name, password):
		""" membuat dan simpan superuser baru dengan detail """

		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	""" cobain """
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def get_full_name(self):
		""" digunakan untuk ambil users full name """
		return self.name

	def get_short_name(self):
		""" digunakan untuk get users short name """
		return self.name

	def __str__(self):
		""" django menggunakan ini ketika membutuhkan convert object ke string """
		return self.email
