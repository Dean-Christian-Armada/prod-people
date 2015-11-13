from django.contrib import admin

from . models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'code', 'picture')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Userlevel)