from django.shortcuts import render
from django.http import HttpResponse
#buat class base views
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
	template_name = 'app1/index.html'
	def get_context_data(self, **kwargs): #ada *args sebagai tuples ada kwargs sebagai dictionary
		# super().methoName(args)
		# super().get_context_data(**kwargs) di python 3

		# super(subclass, instance).method(args) python 2
		context =  super(IndexView, self).get_context_data(**kwargs)
		context['key'] = 'dictionary'
		return context


#ngecek CBV
# from django.http import HttpResponse
# class CBView(View):
# 	def get(self, request):
# 		return HttpResponse('class based views sangat keren')


# Create your views here.
def index(request):
	# return HttpResponse("hello World!!")
	return render(request, 'app1/index.html')
