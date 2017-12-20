from django.contrib import admin
from app4.models import School, Student

# Register your models here.
admin.site.register(School)
admin.site.register(Student)

#abis ini makemigrations & migrate
#lalu ke views
