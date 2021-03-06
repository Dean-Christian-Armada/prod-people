from django.contrib import admin
from . models import *

class UserNotificationReceiversAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'get_receivers')

# Register your models here.
admin.site.register(NotificationStatus)
admin.site.register(EmailNotification)
admin.site.register(Notification)
admin.site.register(UserNotificationReceivers, UserNotificationReceiversAdmin)
admin.site.register(NotificationHistory)
admin.site.register(BaseURL)