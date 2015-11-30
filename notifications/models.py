from django.db.models.fields.related import ManyToManyField
from django.db import models

from login.models import UserProfile
# from .serializers import NotificationSerializer

from ckeditor.fields import RichTextField
# from swampdragon.models import SelfPublishModel

# Create your models here.

class BaseURL(models.Model):
	base_url = models.CharField(max_length=50, default=None)

	def __unicode__(self):
		return self.base_url

class NotificationStatus(models.Model):
	base_url = models.ForeignKey(BaseURL, default=None)
	status = models.CharField(max_length=100, default=None)
	label = models.TextField(default=None)

	def __unicode__(self):
		return "%s - %s" % (self.status.upper(), self.label)

# Creates the Notification Email
class EmailNotification(models.Model):
	notification_status = models.ForeignKey(NotificationStatus)
	greetings = RichTextField()
	message = RichTextField()

	def __unicode__(self):
		return self.notification_status.label

class Notification(models.Model):
	user = models.ForeignKey(UserProfile)
	status = models.ForeignKey(NotificationStatus)
	date_time_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s %s" % (self.user, self.status, self.date_time_created)

class UserNotificationReceivers(models.Model):
	status = models.ForeignKey(NotificationStatus)
	receiver = models.ManyToManyField(UserProfile)

	def __unicode__(self):
		return unicode(self.status)

	def get_receivers(self):
		# return self.receiver.all()
		return "\n, ".join([d.code for d in self.receiver.all()])

class NotificationHistory(models.Model):
	received = models.ForeignKey(UserProfile, blank=True, null=True)
	notification = models.ForeignKey(Notification, blank=True, null=True)
	boolean = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s - %s / %s" % (self.received, self.notification, self.boolean)

# class NotificationHistory(SelfPublishModel, models.Model):
# 	serializer_class = NotificationSerializer
# 	received = models.ForeignKey(UserProfile, blank=True, null=True)
# 	notification = models.ForeignKey(Notification, blank=True, null=True)
# 	boolean = models.BooleanField(default=False)

# 	def __unicode__(self):
# 		return "%s - %s / %s" % (self.received, self.notification, self.boolean)

	# The save algorithm for the NotificationHistory
	# def save(self, *args, **kwargs):
	# 	notification = self.notification
	# 	user_notification_receivers = UserNotificationReceivers.objects.get(status=notification.status)
	# 	receivers = user_notification_receivers.receiver.all()
	# 	for x in receivers:
	# 		NotificationHistory.objects.create(notification=notification, received=x)
	# 	super(NotificationHistory, self).save(*args, **kwargs)