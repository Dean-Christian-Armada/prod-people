from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from jsignature.utils import draw_signature
from defender.decorators import watch_login

from notifications.models import NotificationHistory

from . models import *

import os

def welcome(request):
	userprofile = UserProfile.objects.get(user=request.user)
	os.system('say "Hi %s Welcome to People"' % userprofile.nick_name)
	return HttpResponse("")

def home(request):
	user = request.user
	userprofile = ''
	template = "home.html"
	context_dict = {"title": "MANSHIP People"}
	next_redirect = ""
	# Next URL to be redirected
	if "next" in request.GET:
		next_redirect = request.GET['next']
	if user.is_authenticated():
		user = User.objects.get(username=user)
		try:
			userprofile = UserProfile.objects.get(user=user)
		except:
			logout(request)
			return HttpResponseRedirect('/?error=Invalid Username or Password')
		userlevel = str(userprofile.userlevel)
		if userlevel == 'recruitment':
			# return signature(request)
			return HttpResponse("HELLO This is the recruitment level!<a href='/logout/'>Log Out</a>")
		elif userlevel == 'application-form':
			# return HttpResponse("HELLO This is the applicant level!<a href='/logout/'>Log Out</a>")
			return HttpResponseRedirect('/application-form/')
		else:
			# return HttpResponse("HELLO This is the crew level!<a href='/logout/'>Log Out</a>")
			# return HttpResponseRedirect('/mariners-profile/')
			# print ("----------")
			# if "next" in request.POST:
			# 	return HttpResponseRedirect(request.POST['next'])
			template = "login-landing/crewing_profiles.html"
			notifications = NotificationHistory.objects.filter(received=userprofile, boolean=False).order_by('-notification__date_time_created')[:5]
			notifications_all = NotificationHistory.objects.filter(received=userprofile)
			notifications_read = NotificationHistory.objects.filter(received=userprofile, boolean=True)

			# 	notifications = NotificationHistory.objects.filter(received=user, flag=True)
			context_dict['notifications'] = notifications
			context_dict['notifications_count'] = notifications.count()
			context_dict['notifications_all_count'] = notifications_all.count()
			context_dict['notifications_read_count'] = notifications_read.count()
			# os.system('say "Hi %s Welcome to People"' % userprofile.nick_name)
		# else:
		# 	print userlevel
		# 	print type(userlevel)
		# 	return HttpResponse("DEFAULT<a href='/logout/'>Log Out</a>")
	context_dict['user_profile'] = userprofile
	# Next URL to be redirected variable
	context_dict['next_redirect'] = next_redirect
	return render(request, template, context_dict)

@watch_login
def validation(request):
	username = ''
	password = ''
	if request.method == 'POST':
		if 'username' in request.POST and 'password' in request.POST:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				# if "next" in request.POST:
				# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
				print (request.POST)
				if request.POST['next']:
					_next_base_param = request.POST['next'].split('/')
					if _next_base_param[1] != 'application-form':
						return HttpResponseRedirect(request.POST['next'])
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/?error=Invalid Username or Password')
		else:
			return HttpResponseRedirect('/?error=Invalid LogIn Attempt')
	else:
		# raise Http404
		return HttpResponseRedirect('/?error=Invalid LogIn Attempt')

def validation_next(request):
	return HttpResponse("DEANDSA")

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
