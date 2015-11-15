from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from jsignature.utils import draw_signature

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
			template = "login-landing/crewing_profiles.html"
			notifications = NotificationHistory.objects.filter(received=userprofile, boolean=False)
			# if not notifications:
			# 	notifications = NotificationHistory.objects.filter(received=user, flag=True)
			context_dict['notifications'] = notifications
			# os.system('say "Hi %s Welcome to People"' % userprofile.nick_name)
		# else:
		# 	print userlevel
		# 	print type(userlevel)
		# 	return HttpResponse("DEFAULT<a href='/logout/'>Log Out</a>")
	context_dict['user_profile'] = userprofile
	return render(request, template, context_dict)

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
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/?error=Invalid Username or Password')
		else:
			return HttpResponseRedirect('/?error=Invalid LogIn Attempt')
	else:
		# raise Http404
		return HttpResponseRedirect('/?error=Invalid LogIn Attempt')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
