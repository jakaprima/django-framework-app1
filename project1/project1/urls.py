#deklarasi URL untuk django project

from django.conf.urls import include, url
from django.contrib import admin
from app1 import views
# from app2 import views
# from app3 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.index, name='index'), #buat url di project ini buat yang biasa
    # url(r'^$', views.CBView.as_view()),
    url(r'^$', views.IndexView.as_view()),
    url(r'^app2/', include('app2.urls')), #buat url di app
    url(r'^app3/', include('app3.urls', namespace="namespace3", app_name='app3_name')), # app_name buat di view href entar
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('project1_api.urls'))
]
