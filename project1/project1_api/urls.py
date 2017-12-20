from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter # buat bikin viewset

from . import views

# buat di http://0.0.0.0:8080/api/ #kalo masuknnya lewat sini pake class HelloViewSet
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login') #pake base_name kalo bukan modelviewset

urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
	url(r'', include(router.urls))
]