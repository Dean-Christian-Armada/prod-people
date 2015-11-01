from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='mariners_profiles' ),
	url(r'^(?P<slug>[\w\-]+)/$', views.profile, name='mariners_profile' ),
]