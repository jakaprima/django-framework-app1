from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

# Create your views here.
class SchoolListView(ListView):
	context_object_name = 'schools' #custom generated nama variable buat di view kalo ga pake ini jadi school_list
	model = models.School 

class SchoolDetailView(DetailView):
	context_object_name = 'school_detail' #kalo ini generated otomatis variablenya jadi school kalo mau custom kaya gini
	model = models.School 
	template_name = 'app4/school_detail.html'

#abis ini ke templates
