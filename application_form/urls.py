from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.form, name='application_form' ),
	url(r'^tmp-image/$', views.tmp_image, name='tmp_image'),
	url(r'^success/$', views.success, name='success'),
	url(r'^training-certificates/$', views.trainings_certificates, name='application_form_training_certificates'),
	url(r'^city-municipality/$', views.city_municipality, name='application_form_city_municipality'),
	url(r'^ncr-barangay/$', views.ncr_barangay, name='application_form_ncr_barangay'),
	url(r'^auto-zip-code/$', views.auto_zip_code, name='application_form_auto_zip_code'),
	# url(r'^(?P<principal>(.)*)/(?P<vessel_type>(.)*)/$', views.fleet_application_form, name='fleet_application_form'),
	url(r'^principal/(?P<principal>(.)*)/(?P<id>[0-9]*)/$', views.fleet_application_form, name='fleet_application_form'),
	url(r'^principal/(?P<principal>(.)*)/(?P<id>[0-9]*)/pdf/$', views.pdf_fleet_application_form, name='pdf_fleet_application_form'),
	url(r'^principal/(?P<principal>(.)*)/(?P<id>[0-9]*)/pdf/blank/$', views.blank_pdf_fleet_application_form, name='blank_pdf_fleet_application_form'),
	url(r'^manship/(?P<id>[0-9]*)/$', views.manship_form, name='manship_form'),
	url(r'^manship/(?P<id>[0-9]*)/pdf/$', views.pdf_complete_manship_form, name='pdf_complete_manship_form'),
	url(r'^manship/(?P<id>[0-9]*)/pdf/blank/$', views.blank_pdf_complete_manship_form, name='blank_pdf_complete_manship_form'),
	url(r'^manship/sea-services/(?P<id>[0-9]*)/pdf/$', views.pdf_manship_sea_services_form, name='pdf_manship_sea_services_form'),
	url(r'^manship/sea-services/(?P<id>[0-9]*)/pdf/blank/$', views.blank_pdf_manship_sea_services_form, name='blank_pdf_manship_sea_services_form'),
]