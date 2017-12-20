#register models dimana django akan guanin untuk django admin interface

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
