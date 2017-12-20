from django.conf.urls import include, url 
from app3 import views 

# template tagging
#app_name = 'app3_name' #variable buat di view

urlpatterns = [
	url(r'^$', views.index, name="app3index"),
	url(r'^relative/$', views.relative, name='relative'),
	url(r'^other/$', views.other, name="other"), #name = buat di view
]
