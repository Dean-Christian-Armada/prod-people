from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

# Creates default User Model
def default_user():
	user_name = 'default'
	try:
		try:
			user = User.objects.create_user(user_name, '', user_name)
			user.save()
		except:
			user = User.objects.get(username=user_name)
		return user.id
	except:
		return None

def default_user_level():
	try:
		_user_level = 'default'
		user_level = Userlevel.objects.get_or_create(userlevel=_user_level)
		user_level = Userlevel.objects.get(userlevel=_user_level)
		return user_level.id
	except:
		return None

def default_user_user_level():
	try:
		default = 'default'
		user_level = Userlevel.objects.get_or_create(userlevel=default)
		user_level = Userlevel.objects.get(userlevel=default)
		user_profile = UserProfile.objects.get_or_create(first_name=default, middle_name=default, last_name=default )
		user_profile = UserProfile.objects.get(first_name=default, middle_name=default, last_name=default )
		return user_profile.id
	except:
		return None

class Userlevel(models.Model):
	userlevel = models.CharField(max_length=50, unique=True, null=True, )
	def __unicode__(self):
		return self.userlevel

class UserProfile(models.Model):
	# Regexes
	# regex for four letter codes only
	code_regex = RegexValidator(regex=r'^([a-z]{4})$', message="Please follow code format")

	user = models.ForeignKey(User, default=default_user())
	userlevel = models.ForeignKey(Userlevel, default=default_user_level())
	code = models.CharField(max_length=4, validators=[code_regex], unique=True, null=True, blank=True)
	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	nick_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	picture = models.ImageField(upload_to='photos/manship-employees', null=True, blank=True, default=None)

	def __unicode__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)