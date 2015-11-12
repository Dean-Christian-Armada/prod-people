from django.db import models

from login.models import UserProfile


# Create your models here.

class CompanyPositions(models.Model):
	positions = models.CharField(max_length=100, default=None)

class UserCompanyProfile(models.Model):
	user = models.ForeignKey(UserProfile)
	position = models.ForeignKey(CompanyPositions)
	street = models.CharField(max_length=50, null=True, blank=True, default=None)
	unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	zip = models.ForeignKey('mariners_profile.Zip', default=None)
	contact = models.BigIntegerField(null=True, blank=True, default=None)