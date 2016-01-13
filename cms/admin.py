from django.contrib import admin

from . models import *

class FolderAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'order']

class SubFolderAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'extra_sub_folder', 'upload', 'order']

class FieldAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'id', 'location', 'name', 'order']


# Register your models here.
admin.site.register(Folder, FolderAdmin)
admin.site.register(SubFolder, SubFolderAdmin)
admin.site.register(File)
admin.site.register(Fields, FieldAdmin)
admin.site.register(FileFieldValue)
admin.site.register(UpdateFileInfoLog)