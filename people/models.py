from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.fields.related import ManyToManyField

from login.models import UserProfile
# from mariners_profile.models import BirthPlace, VesselType, CivilStatus

from django_date_extensions.fields import ApproximateDateField	

from datetime import date
# from dateutil import relativedelta as rdelta

class AbstractPersonalData(models.Model):
	name = models.ForeignKey(UserProfile, default=None)

	# ForeignKeys
	birth_place = models.ForeignKey('mariners_profile.BirthPlace', default=None)
	preferred_vessel_type = models.ForeignKey('mariners_profile.VesselType', default=None)
	civil_status = models.ForeignKey('mariners_profile.CivilStatus', default=None)

	# CharFields
	father_first_name = models.CharField(max_length=50, null=True, default=None)
	father_middle_name = models.CharField(max_length=50, null=True, default=None)
	father_last_name = models.CharField(max_length=50, null=True, default=None)
	mother_first_name = models.CharField(max_length=50, null=True, default=None)
	mother_middle_name = models.CharField(max_length=50, null=True, default=None)
	mother_last_name = models.CharField(max_length=50, null=True, default=None)

	# Integer Fields
	# age = models.PositiveIntegerField(default=None)
	landline_1 = models.PositiveIntegerField(null=True, blank=True, default=None)
	landline_2 = models.PositiveIntegerField(null=True, blank=True, default=None)
	mobile_1 = models.PositiveIntegerField(null=True, default=None)
	mobile_2 = models.PositiveIntegerField(null=True, blank=True, default=None)
	mobile_3 = models.PositiveIntegerField(null=True, blank=True, default=None)
	sss = models.PositiveIntegerField(null=True, default=None)
	philhealth = models.BigIntegerField(null=True, blank=True, default=None)
	tin = models.BigIntegerField(null=True, blank=True, default=None)
	pagibig = models.BigIntegerField(null=True, blank=True, default=None)

	# EmailFields
	email_address_1 = models.EmailField(null=True, default=None)
	email_address_2 = models.EmailField(blank=True, null=True, default=None)

	# Social Accounts
	facebook_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	twitter_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	instagram_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	googleplus_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	linkedin_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	pinterest_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	reddit_account = models.CharField(max_length=30, blank=True, null=True, default=None)
	tumblr_account = models.CharField(max_length=30, blank=True, null=True, default=None)

	# DateFields
	birth_date = models.DateField(default=None)

	# ThirdParty Fields
	availability_date = models.CharField(max_length=15, default=None)
	
	class Meta:
		abstract = True

	def __unicode__(self):
		return "%s %s %s" % (self.name.first_name, self.name.middle_name, self.name.last_name)

	# Do not remove to avoid ValueError
	def save(self, *args, **kwargs):
		if self.landline_2 == '':
			self.landline_2 = None
		if self.philhealth == '':
			self.philhealth = None
		if self.tin == '':
			self.tin = None
		if self.pagibig == '':
			self.pagibig = None
		if self.landline_1 == '':
			self.landline_1 = None
		if self.mobile_2 == '':
			self.mobile_2 = None
		if self.mobile_3 == '':
			self.mobile_3 = None

		super(AbstractPersonalData, self).save(*args, **kwargs)

	def prefix_mobile_1(self):
		count =  len(str(self.mobile_1))
		if count == 10:
			self.mobile_1 = '+63'+str(self.mobile_1)
		elif not self.mobile_1:
			self.mobile_1 = ''
		return self.mobile_1

	def prefix_mobile_2(self):
		count =  len(str(self.mobile_2))
		if count == 10:
			self.mobile_2 = '+63'+str(self.mobile_2)
		elif not self.mobile_2:
			self.mobile_2 = ''
		return self.mobile_2

	def prefix_mobile_3(self):
		count =  len(str(self.mobile_3))
		if count == 10:
			self.mobile_3 = '+63'+str(self.mobile_3)
		elif not self.mobile_3:
			self.mobile_3 = ''
		return self.mobile_3

	def none_landline_1(self):
		if not self.landline_1:
			self.landline_1 = ''
		return self.landline_1

	def none_landline_2(self):
		if not self.landline_2:
			self.landline_2 = ''
		return self.landline_2

	def age(self):
		today = date.today()
		birthday = self.birth_date
		age = today - birthday
		age = age.days
		age = age / 365
		return age



class AbstractSpouseData(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	spouse_first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	spouse_middle_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	spouse_last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	married_date = models.DateField(null=True, blank=True, default=None)
	birthdate = models.DateField(null=True, blank=True, default=None)
	spouse_contact = models.BigIntegerField(null=True, blank=True, default=None)
	spouse_working = models.NullBooleanField(default=None)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if self.spouse_last_name == '':
			return False
		if self.spouse_contact == '':
			self.spouse_contact = None
		super(AbstractSpouseData, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s %s" % (self.spouse_first_name, self.spouse_middle_name, self.spouse_last_name)

	def prefix_spouse_contact(self):
		count =  len(str(self.spouse_contact))
		if count == 10:
			self.spouse_contact = '+63'+str(self.spouse_contact)
		return self.spouse_contact

	def area_code_spouse_contact(self):
		count =  len(str(self.spouse_contact))
		area_code = ''
		if count == 10:
			area_code = '(+63)'
		else:
			area_code = None
		return area_code

class AbstractCollege(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	college = models.ForeignKey('mariners_profile.Colleges', default=None)
	degree = models.ForeignKey('mariners_profile.Degree', default=None)
	collegeyear_from = models.PositiveSmallIntegerField(default=None)
	collegeyear_to = models.PositiveSmallIntegerField(default=None)

	class Meta:
		abstract = True
	
	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.college, self.collegeyear_from, self.collegeyear_to)

class AbstractHighSchool(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	highschool = models.ForeignKey('mariners_profile.HighSchools', default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.highschool, self.schoolyear_from, self.schoolyear_to)

class AbstractEmergencyContact(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	relationship = models.ForeignKey('mariners_profile.Relationship', default=None)
	emergency_zip = models.ForeignKey('mariners_profile.Zip', default=None)
	emergency_first_name = models.CharField(max_length=50, null=True, default=None)
	emergency_middle_name = models.CharField(max_length=50, null=True, default=None)
	emergency_last_name = models.CharField(max_length=50, null=True, default=None)
	emergency_contact = models.BigIntegerField(null=True, blank=True, default=None)
	emergency_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	emergency_unit = models.CharField(max_length=50, null=True, blank=True, default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.emergency_first_name, self.emergency_middle_name, self.emergency_last_name)
		return user

	def prefix_emergency_contact(self):
		count =  len(str(self.emergency_contact))
		if count == 10:
			self.emergency_contact = '+63'+str(self.emergency_contact)
		return self.emergency_contact

# START Background Info
class AbstractVisaApplication(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	visa_application = models.NullBooleanField(default=None)
	visa_application_reason = models.ForeignKey('mariners_profile.Reasons', default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.visa_application)
	

class AbstractDetained(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	detained = models.NullBooleanField(default=None)
	detained_reason = models.ForeignKey('mariners_profile.Reasons', default=None)

	class Meta:
		abstract = True
	

class AbstractDisciplinaryAction(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	disciplinary_action = models.NullBooleanField(default=None)
	disciplinary_action_reason = models.ForeignKey('mariners_profile.Reasons', default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.disciplinary_action)

class AbstractChargedOffense(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	charged_offense = models.NullBooleanField(default=None)
	charged_offense_reason = models.ForeignKey('mariners_profile.Reasons', default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.charged_offense)


class AbstractTermination(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	termination = models.NullBooleanField(default=None)
	termination_reason = models.ForeignKey('mariners_profile.Reasons', default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.termination)


class AbstractPassport(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	passport = models.CharField(max_length=100, unique=True, default=None)
	passport_expiry = models.DateField(default=None)
	# place_issued = models.ForeignKey(PassportPlaceIssued, default=None, blank=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.passport)

class AbstractSbook(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	sbook = models.CharField(max_length=100, unique=True, default=None)
	sbook_expiry = models.DateField(default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.sbook)
	
class AbstractCOC(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	coc = models.CharField(max_length=100, null=True, blank=True, default=None, )
	coc_expiry = models.DateField(null=True, blank=True, default=None)
	coc_rank = models.ForeignKey('mariners_profile.COCRank', default=None, blank=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.coc)
	
class AbstractLicense(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	license = models.CharField(max_length=100, default=None, null=True, blank=True)
	license_rank = models.ForeignKey('mariners_profile.Rank', default=None, blank=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.license)
	
class AbstractSRC(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	src = models.CharField(max_length=100, unique=True, default=None)
	src_rank = models.ForeignKey('mariners_profile.Rank', default="mariners_profile.null_default_foreign_key_value(Rank, 'rank', '')")

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.src)
	
class AbstractGOC(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	goc = models.CharField(max_length=100, 	null=True, blank=True, default=None, )
	goc_expiry = models.DateField(null=True, blank=True, default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.goc)
	
class AbstractUSVisa(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	us_visa = models.NullBooleanField()
	us_visa_expiry = models.DateField(blank=True, null=True, default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.us_visa)

	def determine_us_visa(self):
		if self.us_visa == True:
			determine = "Yes"
		else:
			determine = "None"
		return determine

	
class AbstractSchengenVisa(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	schengen_visa = models.NullBooleanField()
	schengen_visa_expiry = models.DateField(blank=True, null=True, default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.schengen_visa)

	def determine_schengen_visa(self):
		if self.schengen_visa == True:
			determine = "Yes"
		else:
			determine = "None"
		return determine
	
class AbstractYellowFever(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	yellow_fever = models.CharField(max_length=100, unique=True, default=None)
	yellow_fever_expiry = models.DateField(default=None)

	class Meta:
		abstract = True
	
	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s %s" % (user, self.yellow_fever)

class AbstractFlagDocuments(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user

class AbstractTrainingCertificateDocuments(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	
	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user

class AbstractSeaService(models.Model):

	# OneToOneField with Django Users Model 
	user = models.ForeignKey(UserProfile, default=None)

	# ForeignKeys
	vessel_name = models.ForeignKey('mariners_profile.VesselName', default=None)
	vessel_type = models.ForeignKey('mariners_profile.VesselType', default=None)
	flag = models.ForeignKey('mariners_profile.Flags', default=None)
	engine_type = models.ForeignKey('mariners_profile.EngineType', default=None)
	manning_agency = models.ForeignKey('mariners_profile.ManningAgency', default=None)
	principal = models.ForeignKey('mariners_profile.Principal', default=None)
	rank = models.ForeignKey('mariners_profile.Rank', default=None)
	cause_of_discharge = models.ForeignKey('mariners_profile.CauseOfDischarge', default=None)

	# Integer Fields
	grt = models.PositiveIntegerField(default=None, null=True, blank=True)
	dwt = models.PositiveIntegerField(default=None, null=True, blank=True)
	year_built = models.PositiveSmallIntegerField(default=None, blank=True)
	# duration = models.PositiveSmallIntegerField(default=None, blank=True)

	# Decimal Fields
	hp = models.DecimalField(decimal_places=1, max_digits=10, default=None, blank=True)
	kw = models.DecimalField(decimal_places=1, max_digits=10, default=None, blank=True)

	# Date Fields
	date_joined = models.DateField(default=None)
	date_left = models.DateField(default=None)

	class Meta:
		abstract = True

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s" % (user, self.vessel_name)

	def duration(self):
		date_joined = self.date_joined
		date_left = self.date_left
		duration = date_left - date_joined
		return duration.days

	def duration_months(self):
		date_joined = self.date_joined
		date_left = self.date_left
		duration = date_left - date_joined
		months = duration.days / 30
		return months

	def none_dwt(self):
		if not self.dwt:
			self.dwt = ''
		return self.dwt

	def none_grt(self):
		if not self.grt:
			self.grt = ''
		return self.grt