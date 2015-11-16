from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^login/$', views.login_notifications, name='login_notifications'),
	url(r'^login/all/(?P<slug>[\w\-]+)/$', views.login_notifications_all, name='login_notifications_all'),
	url(r'^login/read/$', views.login_read_notifications, name='login_read_notifications'),
	url(r'^login/delete/$', views.login_delete_notifications, name='login_delete_notifications'),
]