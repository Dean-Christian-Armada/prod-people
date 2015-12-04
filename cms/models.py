from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from datetime import date, timedelta

from login.models import UserProfile
from mariners_profile.models import null_default_foreign_key_value, MarinersProfile

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
		return self.name.capitalize()

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

	class Meta:
		verbose_name_plural = "Subfolders"

	def __unicode__(self):
		# return "%s / %s" % (str(self.folder), self.name)
		return "%s" % (self.slug)

	# Made for the Scorpio / HSM presentation
	def capitalize_name(self):
		return self.name.capitalize()

	# Desired custom methods clashes from wanted output because of self ForeignKey
	def slug_name(self):
		return slugify(str(self.folder)+' '+str(self.extra_sub_folder)+' '+self.name)

	def expiry_notifications(self):
		pass

	# Dynamic and accurate notifier script via level and date
	def converted_notifier(self, notifier, user):
		_return = 0
		_list = [ self.low_notifier, self.medium_notifier, self.high_notifier ]
		if notifier == "high":
			_notifier = self.high_notifier
			_index = _list.index(self.high_notifier)
			# _list.remove(self.high_notifier)
		elif notifier == "medium":
			_notifier = self.medium_notifier
			_index = _list.index(self.medium_notifier)
			# _list.remove(self.medium_notifier)
		else:
			_notifier = self.low_notifier
			_index = _list.index(self.low_notifier)
			# _list.remove(self.low_notifier)
		try:
			_day_notifier = int(re.search(r'\d+', _notifier).group())
			if 'month' in _notifier:
				_day_notifier = 30 * _day_notifier
			elif 'week' in _notifier:
				_day_notifier = 7 * _day_notifier
			elif 'year' in _notifier:
				_day_notifier = 365 * _day_notifier
		except:
			_day_notifier = _notifier
		x = SubFolder.objects.get(id=self.id)
		y = File.objects.filter(location=x).filter(user=user).filter(archive=False)
		z = Fields.objects.filter(location=x).filter(name__icontains="expir")
		a = FileFieldValue.objects.filter(field=z).filter(file=y)

		for b in a:
			# if self.id == 71:
			# 	print b
			expiry_date = b.value
			_expiry_date = expiry_date.split('-')
			_expiry_date = map(int, _expiry_date)
			_expiry_date = date( _expiry_date[0], _expiry_date[1], _expiry_date[2] )
			_day = _expiry_date - timedelta(days=_day_notifier)
			# if self.id == 71:
			# 	print _day
			if _day < today:
				_return += 1
				try:
					z = _list[_index+1]
					try:
						s_day_notifier = int(re.search(r'\d+', z).group())
						if 'month' in z:
							s_day_notifier = 30 *s_day_notifier
						elif 'week' in z:
							s_day_notifier = 7 * s_day_notifier
						elif 'year' in z:
							s_day_notifier = 365 * s_day_notifier
					except:
						s_day_notifier = z
					s_day = _expiry_date - timedelta(days=s_day_notifier)
					if s_day < today:
						# if self.id == 71:
						# 	print notifier
						_return -= 1
				except:
					pass
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
		verbose_name_plural = "Fields"
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
		unset_list_return = set()
		_notifier_count = 0
		x = Fields.objects.filter(name__icontains="expir")
		y = FileFieldValue.objects.filter(field=x)
		z = File.objects.filter(id__in=y.values('file')).filter(archive=0)
		# a = File.objects.get(id=46)
		for s in z:
			name = unicode(s.name).split('/')
			name = name[len(name)-1]
			notifier_count = 0
			unset_list_return_len = len(unset_list_return)
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
				try:
					low_notifier = int(low_notifier)
					low_notifier = "%d days" % low_notifier
				except:
					pass
			except:
				_low_notifier = 0
				low_notifier = "%d days" % low_notifier
			try:
				_high_notifier = int(re.search(r'\d+', high_notifier).group())
				if 'month' in high_notifier:
					_high_notifier = 30 * _high_notifier
				elif 'week' in high_notifier:
					_high_notifier = 7 * _high_notifier
				elif 'year' in high_notifier:
					_high_notifier = 365 * _high_notifier
				try:
					high_notifier = int(high_notifier)
					high_notifier = "%d days" % high_notifier
				except:
					pass
			except:
				_high_notifier = 0
				high_notifier = "%d days" % high_notifier
			try:
				_medium_notifier = int(re.search(r'\d+', medium_notifier).group())
				if 'month' in medium_notifier:
					_medium_notifier = 30 * _medium_notifier
				elif 'week' in medium_notifier:
					_medium_notifier = 7 * _medium_notifier
				elif 'year' in medium_notifier:
					_medium_notifier = 365 * _medium_notifier
				try:
					medium_notifier = int(medium_notifier)
					medium_notifier = "%d days" % medium_notifier
				except:
					pass
			except:
				_medium_notifier = 0
				medium_notifier = "%d days" % medium_notifier
			_list_notifier = [_high_notifier, _medium_notifier, _low_notifier]
			list_notifier = [high_notifier, medium_notifier, low_notifier]
			list_indicator_notifier = ["high notifier", "medium notifier", "low notifier"]
			b = FileFieldValue.objects.filter(file=s).get(field__name__icontains="Expir")
			expiry_date = b.value
			_expiry_date = expiry_date.split('-')
			_expiry_date = map(int, _expiry_date)
			_expiry_date = date( _expiry_date[0], _expiry_date[1], _expiry_date[2] )
			_day = _expiry_date - timedelta(days=_list_notifier[notifier_count])
			location = s.location.slug.replace('-', '->').upper()
			user = s.user
			picture = MarinersProfile.objects.get(user=user.id).picture
			if _day < today:
				if int(re.search(r'\d+', list_notifier[notifier_count]).group()) == 0:
					unset_list_return.add("<a class='border-bottom-top-1-white'><b>Please set the %s of %s</b></a>" % (list_indicator_notifier[notifier_count], location))
					if len(unset_list_return) != unset_list_return_len:
						_notifier_count += 1
				else:
					_notifier_count += 1
					list_return.append("<a class='border-bottom-top-1-white' href='/mariners-profile/%s/' target='_blank'><img src='/media/%s' height='50px' width='50px'> %s - %s->%s will expire in %s at %s</a>"% (user.slug, picture, user.code, location, name, list_notifier[notifier_count], _expiry_date))
					break
			else:
				while(_day > today):
					
					try:
						_day = _expiry_date - timedelta(days=_list_notifier[notifier_count])
						if int(re.search(r'\d+', list_notifier[notifier_count]).group()) == 0:
							unset_list_return.add("<a class='border-bottom-top-1-white'><b>Please set the %s of %s</b></a>" % (list_indicator_notifier[notifier_count], location))
							if len(unset_list_return) != unset_list_return_len:
								_notifier_count += 1
						else:
							_notifier_count += 1
							list_return.append("<a class='border-bottom-top-1-white' href='/mariners-profile/%s/' target='_blank'><img src='/media/%s' height='50px' width='50px'> %s - %s->%s will expire in %s at %s</a>"% (user.slug, picture, user.code, location, name, list_notifier[notifier_count], _expiry_date))
							break
					except:
						break
					notifier_count += 1
		print unset_list_return
		return (_notifier_count, list_return, unset_list_return)

class FileFieldValue(models.Model):
	file = models.ForeignKey(File)
	field = models.ForeignKey(Fields)
	value = models.CharField(max_length=50, default=None)

	class Meta:
		verbose_name_plural = "File Field Values"
		ordering = ['field']

	def __unicode__(self):
		return "%s - %s" % (self.id, self.value)
# END Used for SCANNED DOCUMENTS on the Mariners Profile