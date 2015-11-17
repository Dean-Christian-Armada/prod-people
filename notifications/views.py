from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse

from notifications.models import NotificationHistory
from login.models import UserProfile

# Create your views here.

def login_notifications(request):
	_bool = request.GET['bool']
	user_id = request.GET['user_id']
	notifications = NotificationHistory.objects.filter(received__user__id=user_id, boolean=_bool).order_by('-notification__date_time_created')[:5]

	template = 'notifications/login.html'
	context_dict = { 'notifications': notifications, 'bool': _bool }
	return render(request, template, context_dict)

def login_notifications_all(request, slug):
	user_profile = UserProfile.objects.get(slug=slug)
	notifications = NotificationHistory.objects.filter(received=user_profile).order_by('-notification__date_time_created')
	template = 'notifications/login_all.html'
	context_dict = { 'notifications': notifications }
	context_dict['user_profile'] = user_profile
	context_dict['title'] = "All Notifications"
	return render(request, template, context_dict)

def login_read_notifications(request):
	notification_id = request.GET['id']
	x = NotificationHistory.objects.get(id=notification_id)
	x.boolean = True
	x.save()
	notifications = NotificationHistory.objects.filter(received=x.received, boolean=False)
	notifications_read = NotificationHistory.objects.filter(received=x.received, boolean=True)

	return HttpResponse("%s,%s" % (notifications.count(), notifications_read.count())) 

def login_delete_notifications(request):
	notification_id = request.GET['id']
	x = NotificationHistory.objects.get(id=notification_id)
	x.delete()
	notifications = NotificationHistory.objects.filter(received=x.received, boolean=False)
	notifications_read = NotificationHistory.objects.filter(received=x.received, boolean=True)

	return HttpResponse("%s,%s" % (notifications.count(), notifications_read.count())) 