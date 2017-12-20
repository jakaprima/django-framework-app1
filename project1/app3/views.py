from django.shortcuts import render

# Create your views here.
def index(request):
	dict1 = {'data1': 'test', 'data2': 100}
	return render(request, 'app3/index.html', dict1)

def other(request):
	return render(request, 'app3/other.html')

def relative(request):
	return render(request, 'app3/relative.html')
