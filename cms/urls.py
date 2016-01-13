from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^zipped/$', views.zipped, name='zipped'),
	url(r'^targz/$', views.targz, name='targz'),
	url(r'^tarbz2/$', views.tarbz2, name='tarbz2'),
]