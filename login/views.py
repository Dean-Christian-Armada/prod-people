from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from jsignature.utils import draw_signature


from . models import *

def home(request):
	user = request.user
	template = "home.html"
	context_dict = {}
	context_dict = {"title": "Manship People Software"}
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
		elif userlevel == 'crewing':
			# return HttpResponse("HELLO This is the crew level!<a href='/logout/'>Log Out</a>")
			# return HttpResponseRedirect('/mariners-profile/')
			template = "login-landing/crewing_profiles.html"
		else:
			print userlevel
			print type(userlevel)
			return HttpResponse("DEFAULT<a href='/logout/'>Log Out</a>")
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
