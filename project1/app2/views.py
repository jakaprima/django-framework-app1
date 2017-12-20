from django.shortcuts import render
from django.http import HttpResponse
from app2.models import Topic,Webpage,AccessRecord
from app2.forms import UserBaruForm
from . import forms

# Create your views here.
def index(request):
	# print(request)
	# return HttpResponse('<b>halo ini app2</b>')

	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}

	#dictionary_saya = {'key': "isi data"}
	return render(request, 'app2/index.html', context=date_dict) #ambil dari template

def form_name_view(request):
	form = forms.FormName()
	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			print('validasi success')
			print('name '+ form.cleaned_data['name']) #name itu dari formnya
			print('email '+ form.cleaned_data['email'])
			print('text '+ form.cleaned_data['text'])
	return render(request, 'app2/form.html', {'form': form})

def signup(request):
	form = UserBaruForm()
	if request.method == "POST":
		form = UserBaruForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('error form invalid')

	return render(request, 'app2/signup.html', {'form': form})

