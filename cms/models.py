from django.db import models
from django.template.defaultfilters import slugify

from login.models import UserProfile
from mariners_profile.models import null_default_foreign_key_value

import os


# Create your models here.

# START Used for SCANNED DOCUMENTS on the Mariners Profile
# A scipt used for dynamic folders in file upload
def content_file_name(instance, filename):
    upload_dir = os.path.join('scanned',instance.location.name)
    return os.path.join(upload_dir, filename)

class Folder(models.Model):
	name = models.CharField(max_length=50, default=None)
	order = models.SmallIntegerField(null=True, blank=True, default=None)

	def slug_name(self):
		return slugify(self.name)

	def __unicode__(self):
		return self.name

class SubFolder(models.Model):
	folder = models.ForeignKey(Folder, default=null_default_foreign_key_value(Folder, 'name', ''))
	extra_sub_folder = models.ForeignKey('self', default=null_default_foreign_key_value('self', 'name', ''))
	name = models.CharField(max_length=100, null=True, blank=True, default=None)
	order = models.SmallIntegerField(null=True, blank=True, default=None)
	upload = models.BooleanField(default=True)

	def slug_name(self):
		return slugify(self.name)


	def __unicode__(self):
		return "%s/%s" % (str(self.folder), self.name)

class File(models.Model):
	user = models.ForeignKey(UserProfile)
	location = models.ForeignKey(SubFolder)
	name = models.FileField(upload_to=content_file_name)
	uploaded_by = models.ForeignKey(UserProfile, related_name='uploaded_by', default=None)
	uploaded_date = models.DateField(auto_now_add=True, editable=True)
	archive = models.BooleanField(default=False)

	def download_link(self):
		return "/media/%s" % self.name


	def logo(self):
		file_type = str(self.name).split('.')
		file_type = file_type[1]
		if file_type == 'pdf':
			logo = "http://static1.squarespace.com/static/53ffba10e4b034368de43c27/t/54933095e4b040ee5343c55a/1418932373734/"
		elif file_type == 'xls' or file_type == 'xlsx':
			logo = "http://icons.iconarchive.com/icons/carlosjj/microsoft-office-2013/256/Excel-icon.png"
		else:
			logo = "/media/"+str(self.name)
		return logo

	def file_name(self):
		file_name = str(self.name).split('/')
		num = len(file_name) - 1 
		return file_name[num]

	def __unicode__(self):
		return "%s/%s/%s" % (str(self.user.code).upper(), str(self.location).upper(), str(self.name))

class Label(models.Model):
	name = models.CharField(max_length=50, default=None)

	def __unicode__(self):
		return self.name

class Fields(models.Model):
	location = models.ForeignKey(SubFolder)
	name = models.CharField(max_length=50, default=None)
	type = models.CharField(max_length=10, default='text')
	classes = models.CharField(max_length=75, default='form-control input-form')
	order = models.SmallIntegerField(null=True, blank=True, default=None)
	# slug = models.SlugField(null=True, blank=True, unique=True,  default=None)

	def label(self):
		location = str(self.location).replace("/", "-").lower()
		id = "id-%s-%s" % (slugify(self.name), location)
		label = "<label for='%s' class='input-group-addon input-label'>%s:<label>" % (id, self.name)
		return label

	def __unicode__(self):
		location = str(self.location).replace("/", "-").lower()
		id = "id-%s-%s" % (slugify(self.name), location)
		label = "<label for='%s' class='input-group-addon input-label'>%s:<label>" % (id, self.name)
		if self.type == 'select':
			field = "<select name='%s' id='%s' class='%s' required></select>" % (slugify(self.name), id, self.classes)
		else:
			field = "<input type ='%s' name='%s' id='%s' class='%s' required>" % (self.type, slugify(self.name), id, self.classes) 
		return "%s" % (field)

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.name)
	# 	try:
	# 		super(Fields, self).save(*args, **kwargs)
	# 	except:
	# 		pass


class FileFieldValue(models.Model):
	file = models.ForeignKey(File)
	field = models.ForeignKey(Fields)
	value = models.CharField(max_length=50, default=None)

	def __unicode__(self):
		return self.value
# END Used for SCANNED DOCUMENTS on the Mariners Profile