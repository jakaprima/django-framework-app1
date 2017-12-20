from django.conf.urls import url
from app2 import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^formpage/', views.form_name_view, name='form_name'),
	url(r'^daftar/', views.signup, name='daftar'),
]