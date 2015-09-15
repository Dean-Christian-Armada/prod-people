"""people URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from login.views import home, validation, user_logout
# from application_form.views import form


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/logout/$', 'django.contrib.auth.views.logout',
    #                       {'next_page': '/'}),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
    url(r'^$', home, name='home'),
    url(r'^validate/$', validation, name='validate'),
    url(r'^logout/$', user_logout, name='logout'),

    # url(r'^application-form/$', form, name='application_form'),
    url(r'^application-form/', include('application_form.urls')),
    url(r'^mariners-profile/', include('mariners_profile.urls')),
    url(r'^application-profile/', include('application_profile.urls')),

    # Django autocomplete
    url(r'^autocomplete/', include('autocomplete_light.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)