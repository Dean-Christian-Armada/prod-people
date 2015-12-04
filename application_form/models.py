# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import *
from mariners_profile.models import Zip, Flags, TrainingCertificates, Sources, Specifics, Rank, Status

# Creates Applicant Status
def default_applicant_status():
	try:
		status_value = "Pending"
		status = Status.objects.get_or_create({'status':status_value}, status__iexact=status_value)
		status = Status.objects.get(status__iexact=status_value)
		return status.id
	except:
		return None

class ApplicationFormCurrentAddress(models.Model):
	current_zip = models.ForeignKey(Zip, default=None)
	current_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	current_street = models.CharField(max_length=50, null=True, blank=True, default=None)

	class Meta:
		verbose_name_plural = "Applicant's Current Address"

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.current_unit, self.current_street, self.current_zip.barangay, self.current_zip.municipality, self.current_zip)

class ApplicationFormPermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	permanent_street = models.CharField(max_length=50, null=True, blank=True, default=None)

	class Meta:
		verbose_name_plural = "Applicant's Permanent Address"

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.permanent_unit, self.permanent_street, self.permanent_zip.barangay, self.permanent_zip.municipality, self.permanent_zip)

class ApplicationFormPersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(ApplicationFormCurrentAddress, default=None)
	permanent_address = models.ForeignKey(ApplicationFormPermanentAddress, default=None)

	class Meta:
		verbose_name_plural = "Applicant's Personal Data"

class ApplicationFormSpouse(AbstractSpouseData):
	class Meta:
		verbose_name_plural = "Applicant's Spouse"
	pass

class ApplicationFormCollege(AbstractCollege):
	class Meta:
		verbose_name_plural = "Applicant's College"
	pass

class ApplicationFormHighSchool(AbstractHighSchool):
	class Meta:
		verbose_name_plural = "Applicant's HighSchool"
	pass

class ApplicationFormEmergencyContact(AbstractEmergencyContact):
	class Meta:
		verbose_name_plural = "Applicant's Emergency Contacts"
	pass

class ApplicationFormVisaApplication(AbstractVisaApplication):
	class Meta:
		verbose_name_plural = "Applicant's US Visa Information"
	pass
	
class ApplicationFormDetained(AbstractDetained):
	class Meta:
		verbose_name_plural = "Applicant's Background Information regarding Country Detainment"
	pass	

class ApplicationFormDisciplinaryAction(AbstractDisciplinaryAction):
	class Meta:
		verbose_name_plural = "Applicant's Background Information regarding Employment Disciplinary Action"
	pass

class ApplicationFormChargedOffense(AbstractChargedOffense):
	class Meta:
		verbose_name_plural = "Applicant's Background Information regarding Administrative Charged Offense"
	pass
	
class ApplicationFormTermination(AbstractTermination):
	class Meta:
		verbose_name_plural = "Applicant's Background Information regarding Employment Termination"
	pass	

class ApplicationFormPassport(AbstractPassport):
	class Meta:
		verbose_name_plural = "Applicant's Passport Information"
	pass

class ApplicationFormSbook(AbstractSbook):
	class Meta:
		verbose_name_plural = "Applicant's Seaman's Book Information"
	pass

class ApplicationFormCOC(AbstractCOC):
	class Meta:
		verbose_name_plural = "Applicant's COC License Information"
	pass

class ApplicationFormLicense(AbstractLicense):
	class Meta:
		verbose_name_plural = "Applicant's PRC / Marina License Information"
	pass

class ApplicationFormSRC(AbstractSRC):
	class Meta:
		verbose_name_plural = "Applicant's SRC License Information"
	pass

class ApplicationFormGOC(AbstractGOC):
	class Meta:
		verbose_name_plural = "Applicant's GOC License Information"
	pass

class ApplicationFormUSVisa(AbstractUSVisa):
	class Meta:
		verbose_name_plural = "Applicant's US Visa Information"
	pass

class ApplicationFormSchengenVisa(AbstractSchengenVisa):
	class Meta:
		verbose_name_plural = "Applicant's Schengen Visa Information"
	pass
class ApplicationFormYellowFever(AbstractYellowFever):
	class Meta:
		verbose_name_plural = "Applicant's Yellow Fever Information"
	pass

class ApplicationFormFlagDocuments(AbstractFlagDocuments):
	flags = models.ManyToManyField(Flags, blank=True, default=None)

class ApplicationFormTrainingCertificateDocuments(AbstractTrainingCertificateDocuments):
	trainings_certificates = models.ManyToManyField(TrainingCertificates, default=None)

class ApplicationFormSeaService(AbstractSeaService):
	class Meta:
		verbose_name_plural = "Applicant's Sea Service Records"
	pass

class AppSource(models.Model):
	source = models.ForeignKey(Sources, default=None)
	specific = models.ForeignKey(Specifics, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	class Meta:
		verbose_name_plural = "Applicant's MANSHIP Application Resources"

	def __unicode__(self):
		x = str(self.source)
		if str(self.specific):
			x += "- %s" % self.specific
		return x.upper()

class Essay(models.Model):
	essay = models.TextField(null=True, blank=True, default=None)
	class Meta:
		verbose_name_plural = "Applicant's Essay"

	def __unicode__(self):
		return self.essay

class ApplicationForm(models.Model):

	# ForeignKey with Django Users Model 
	user = models.ForeignKey(UserProfile, default=None)

	picture = models.ImageField(upload_to='photos/application-form', blank=True, default=None)
	signature = models.ImageField(upload_to='signatures/application-form', blank=True, default=None)
	
	# ForeignKeys
	position_applied = models.ForeignKey(Rank, related_name="position_applied", default=None)
	alternative_position = models.ForeignKey(Rank, related_name="alternative_position", default=None)
	application_source = models.ForeignKey(AppSource, default=None)
	# Status of the applicant if passed, failed or onhold
	status = models.ForeignKey(Status, default=default_applicant_status())

	# Date Fields
	application_date = models.DateField(default=None)
	
	# Text Field
	essay = models.ForeignKey(Essay, default=None)

	class Meta:
		verbose_name_plural = "Applicant's Form"

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user