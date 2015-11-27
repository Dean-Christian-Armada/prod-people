from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from datetime import date, timedelta

from login.models import UserProfile
from mariners_profile.models import null_default_foreign_key_value

import os, re, sys, datetime


# Create your models here.

today = date.today()

# START Used for SCANNED DOCUMENTS on the Mariners Profile
# A scipt used for dynamic folders in file upload
def content_file_name(instance, filename):
    upload_dir = os.path.join('scanned',instance.location.name)
    return os.path.join(upload_dir, filename)

class Folder(models.Model):
	name = models.CharField(max_length=50, unique=True, default=None)
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
	slug = models.SlugField(null=True, blank=True, default=None)
	# These three notifiers are generally optionals
	low_notifier = models.CharField(max_length=50, null=True, blank=True, default=None)
	medium_notifier = models.CharField(max_length=50, null=True, blank=True, default=None)
	high_notifier = models.CharField(max_length=50, null=True, blank=True, default=None)

	def __unicode__(self):
		# return "%s / %s" % (str(self.folder), self.name)
		return "%s" % (self.slug)

	# Desired custom methods clashes from wanted output because of self ForeignKey
	def slug_name(self):
		return slugify(str(self.folder)+' '+str(self.extra_sub_folder)+' '+self.name)

	def expiry_notifications(self):
		pass

	# Dynamic and accurate notifier script via level and date
	def converted_notifier(self, notifier, user):
		_return = ''
		_list = [ self.low_notifier, self.medium_notifier, self.high_notifier ]
		if notifier == "high":
			notifier = self.high_notifier
			_index = _list.index(self.high_notifier)
			_list.remove(self.high_notifier)
		elif notifier == "medium":
			notifier = self.medium_notifier
			_index = _list.index(self.medium_notifier)
			_list.remove(self.medium_notifier)
		else:
			notifier = self.low_notifier
			_index = _list.index(self.low_notifier)
			_list.remove(self.low_notifier)
		try:
			_low_notifier = int(re.search(r'\d+', notifier).group())
			if 'month' in notifier:
				_low_notifier = 30 * _low_notifier
			elif 'week' in notifier:
				_low_notifier = 7 * _low_notifier
			elif 'year' in notifier:
				_low_notifier = 365 * _low_notifier
		except:
			_low_notifier = notifier
		x = SubFolder.objects.get(id=self.id)
		y = File.objects.filter(location=x).filter(user=user).filter(archive=0)
		z = Fields.objects.filter(location=x).filter(name__icontains="expir")
		a = FileFieldValue.objects.filter(field=z).filter(file=y)

		for b in a:
			expiry_date = b.value
			_expiry_date = expiry_date.split('-')
			_expiry_date = map(int, _expiry_date)
			_expiry_date = date( _expiry_date[0], _expiry_date[1], _expiry_date[2] )
			_day = _expiry_date - timedelta(days=_low_notifier)
			z = _list[_index:]
			if _day < today:
				_return += 1
				for s in z:
					try:
						s_low_notifier = int(re.search(r'\d+', s).group())
						if 'month' in s:
							s_low_notifier = 30 *s_low_notifier
						elif 'week' in s:
							s_low_notifier = 7 * s_low_notifier
						elif 'year' in s:
							s_low_notifier = 365 * s_low_notifier
					except:
						s_low_notifier = s
					s_day = _expiry_date - timedelta(days=s_low_notifier)
					if s_day < today:
						_return += 0
			else:
				_return += 0
		return _return

	def save(self, *args, **kwargs):
		self.slug = slugify(str(self.folder)+' '+str(self.extra_sub_folder)+' '+self.name)
		super(SubFolder, self).save(*args, **kwargs)

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
		return "%s /%s/ %s" % (str(self.user.code).upper(), str(self.location).upper(), str(self.name))

	def delete(self):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.name.name))
		super(File, self).delete()

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
	slug = models.SlugField(null=True, blank=True, default=None)

	class Meta:
		ordering = ['order']

	def label(self):
		location = str(self.location).replace("/", "-").lower()
		id = "id-%s-%s" % (self.slug, location)
		label = "<label for='%s' class='input-group-addon input-label'>%s:<label>" % (id, self.name)
		return label

	def __unicode__(self):
		location = str(self.location).replace("/", "-").lower()
		id = "id-%s-%s" % (self.slug, location)
		input_name = "%s" % (self.slug)
		label = "<label for='%s' class='input-group-addon input-label'>%s:<label>" % (id, self.name)
		if self.type == 'select':
			field = "<select name='%s' id='%s' class='%s' required></select>" % (input_name, id, self.classes)
		else:
			field = "<input type ='%s' name='%s' id='%s' class='%s' required>" % (self.type, input_name, id, self.classes) 
		return "%s" % (field)

	def save(self, *args, **kwargs):
		self.slug = slugify(str(self.location)+' '+str(self.location.extra_sub_folder)+' '+self.name)
		super(Fields, self).save(*args, **kwargs)

	def notifs(self):
		list_return = []
		
		x = Fields.objects.filter(name__icontains="expir")
		y = FileFieldValue.objects.filter(field=x)
		z = File.objects.filter(id__in=y.values('file')).filter(archive=0)
		# a = File.objects.get(id=46)
		for s in z:
			notifier_count = 0
			low_notifier = s.location.low_notifier
			medium_notifier = s.location.medium_notifier
			high_notifier = s.location.high_notifier
			try:
				_low_notifier = int(re.search(r'\d+', low_notifier).group())
				if 'month' in low_notifier:
					_low_notifier = 30 * _low_notifier
				elif 'week' in low_notifier:
					_low_notifier = 7 * _low_notifier
				elif 'year' in low_notifier:
					_low_notifier = 365 * _low_notifier
			except:
				_low_notifier = low_notifier
			try:
				_high_notifier = int(re.search(r'\d+', high_notifier).group())
				if 'month' in high_notifier:
					_high_notifier = 30 * _high_notifier
				elif 'week' in high_notifier:
					_high_notifier = 7 * _high_notifier
				elif 'year' in high_notifier:
					_high_notifier = 365 * _high_notifier
			except:
				_high_notifier = high_notifier
			try:
				_medium_notifier = int(re.search(r'\d+', medium_notifier).group())
				if 'month' in medium_notifier:
					_medium_notifier = 30 * _medium_notifier
				elif 'week' in medium_notifier:
					_medium_notifier = 7 * _medium_notifier
				elif 'year' in medium_notifier:
					_medium_notifier = 365 * _medium_notifier
			except:
				_medium_notifier = medium_notifier
			_list_notifier = [_high_notifier, _medium_notifier, _low_notifier]
			list_notifier = [high_notifier, medium_notifier, low_notifier]
			b = FileFieldValue.objects.filter(file=s).get(field__name__icontains="Expir")
			expiry_date = b.value
			_expiry_date = expiry_date.split('-')
			_expiry_date = map(int, _expiry_date)
			_expiry_date = date( _expiry_date[0], _expiry_date[1], _expiry_date[2] )
			_day = _expiry_date - timedelta(days=_list_notifier[notifier_count])
			if _day < today:
				location = s.location.slug.replace('-', '->').upper()
				user = s.user.code
				list_return.append("%s - %s will expire in %s at %s high" % (user, location, list_notifier[notifier_count], _day))
			else:
				while(_day > today):
					print notifier_count
					_day = _expiry_date - timedelta(days=_list_notifier[notifier_count])
					location = s.location.slug.replace('-', '->').upper()
					user = s.user.code
					list_return.append("%s - %s will expire in %s at %s low" % (user, location, list_notifier[notifier_count], _day))
					notifier_count += 1
		return list_return
		# 2015-10-14 - low
		# 2016-02-11 - high
		# 2015-11-13 - medium

class FileFieldValue(models.Model):
	file = models.ForeignKey(File)
	field = models.ForeignKey(Fields)
	value = models.CharField(max_length=50, default=None)

	class Meta:
		ordering = ['field']

	def __unicode__(self):
		return "%s - %s" % (self.id, self.value)
# END Used for SCANNED DOCUMENTS on the Mariners Profile