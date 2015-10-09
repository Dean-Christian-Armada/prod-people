from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.form, name='application_form' ),
	url(r'^tmp-image/$', views.tmp_image, name='tmp_image'),
	url(r'^success/$', views.success, name='success'),
	url(r'^training-certificates/$', views.trainings_certificates, name='application_form_training_certificates'),
	# url(r'^(?P<principal>(.)*)/(?P<vessel_type>(.)*)/$', views.fleet_application_form, name='fleet_application_form'),
	url(r'^(?P<principal>(.)*)/(?P<id>[0-9]*)/$', views.fleet_application_form, name='fleet_application_form'),
]