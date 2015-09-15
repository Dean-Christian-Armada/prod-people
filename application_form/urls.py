from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.form, name='application_form' ),
	url(r'^tmp-image/$', views.tmp_image, name='tmp_image'),
	url(r'^success/$', views.success, name='success'),
	# url(r'^pdf/(?P<id>[0-9]*)/$', views.pdf_report, name='pdf_report'),
	# url(r'^pdf/sea-services/(?P<id>[0-9]*)/$', views.pdf_report_sea_services, name='pdf_report_sea_services'),
]