from django.db.models.fields.related import ManyToManyField
from django.db import models

from login.models import UserProfile

# Create your models here.

class NotificationStatus(models.Model):
	status = models.CharField(max_length=100, default=None)
	label = models.TextField(default=None)

class EmailNotification(models.Model):
	notification_status = models.ForeignKey(NotificationStatus)
	message = models.TextField()

class Notification(models.Model):
	user = models.ForeignKey(UserProfile)
	status = models.ForeignKey(NotificationStatus)
	date_time_created = models.DateTimeField(auto_now_add=True)

class UserNotificationReceivers(models.Model):
	status = models.ForeignKey(NotificationStatus)
	receiver = models.ManyToManyField(Notification)

class NotificationHistory(models.Model):
	received = models.ForeignKey(UserProfile)
	notification = models.ForeignKey(Notification)