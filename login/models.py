from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Userlevel(models.Model):
	userlevel = models.CharField(max_length=50, unique=True, null=True, )
	def __unicode__(self):
		return self.userlevel

class UserProfile(models.Model):
	# Regexes
	# regex for four letter codes only
	code_regex = RegexValidator(regex=r'^([a-z]{4})$', message="Please follow code format")

	user = models.ForeignKey(User)
	userlevel = models.ForeignKey('Userlevel')
	code = models.CharField(max_length=4, validators=[code_regex], unique=True, null=True, blank=True)
	first_name = models.CharField(max_length=50, null=True)
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)