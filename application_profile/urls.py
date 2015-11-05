from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='application_profiles' ),
	url(r'^(?P<slug>[\w\-]+)/$', views.profile, name='application_profile' ),
	url(r'^pdf/(?P<id>[0-9]*)/$', views.pdf, name='pdf_profile' ),
	url(r'^pdf/sea-service/(?P<id>[0-9]*)$', views.pdf_sea_services, name='pdf_sea_services' ),
	url(r'^principal-vessel-types', views.dynamic_vessel_types_via_principal, name='dynamic_vessel_types_via_principal')
]