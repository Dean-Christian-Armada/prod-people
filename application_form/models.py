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

	def __str__(self):
		return "%s %s %s %s %s" % (self.current_unit, self.current_street, self.current_zip.barangay, self.current_zip.municipality, self.current_zip)

class ApplicationFormPermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	permanent_street = models.CharField(max_length=50, null=True, blank=True, default=None)

	def __str__(self):
		return "%s %s %s %s %s" % (self.permanent_unit, self.permanent_street, self.permanent_zip.barangay, self.permanent_zip.municipality, self.permanent_zip)

class ApplicationFormPersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(ApplicationFormCurrentAddress, default=None)
	permanent_address = models.ForeignKey(ApplicationFormPermanentAddress, default=None)

	

class ApplicationFormSpouse(AbstractSpouseData):
	
	pass

class ApplicationFormCollege(AbstractCollege):
	
	pass

class ApplicationFormHighSchool(AbstractHighSchool):
	
	pass

class ApplicationFormEmergencyContact(AbstractEmergencyContact):
	
	pass

class ApplicationFormVisaApplication(AbstractVisaApplication):
	
	pass
	
class ApplicationFormDetained(AbstractDetained):
	
	pass	

class ApplicationFormDisciplinaryAction(AbstractDisciplinaryAction):
	
	pass

class ApplicationFormChargedOffense(AbstractChargedOffense):
	
	pass
	
class ApplicationFormTermination(AbstractTermination):
	
	pass	

class ApplicationFormPassport(AbstractPassport):
	
	pass

class ApplicationFormSbook(AbstractSbook):
	
	pass

class ApplicationFormCOC(AbstractCOC):
	
	pass

class ApplicationFormLicense(AbstractLicense):
	
	pass

class ApplicationFormSRC(AbstractSRC):
	
	pass

class ApplicationFormGOC(AbstractGOC):
	
	pass

class ApplicationFormUSVisa(AbstractUSVisa):
	
	pass

class ApplicationFormSchengenVisa(AbstractSchengenVisa):
	
	pass
class ApplicationFormYellowFever(AbstractYellowFever):
	
	pass

class ApplicationFormFlagDocuments(AbstractFlagDocuments):
	flags = models.ManyToManyField(Flags, blank=True, default=None)

class ApplicationFormTrainingCertificateDocuments(AbstractTrainingCertificateDocuments):
	trainings_certificates = models.ManyToManyField(TrainingCertificates, default=None)

class ApplicationFormSeaService(AbstractSeaService):
	
	pass

class AppSource(models.Model):
	source = models.ForeignKey(Sources, default=None)
	specific = models.ForeignKey(Specifics, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __str__(self):
		x = str(self.source)
		if str(self.specific):
			x += "- %s" % self.specific
		return x.upper()

class Essay(models.Model):
	essay = models.TextField(null=True, blank=True, default=None)
	
	def __str__(self):
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

	def __str__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user

	def essay_count(self):
		essay = self.essay.essay
		count_words = ''.join(c if c.isalnum() else ' ' for c in essay).split()
		count_words = len(count_words)
		return count_words

class ApplicationFormStatusLog(models.Model):
	application_form = models.ForeignKey(ApplicationForm)
	user = models.ForeignKey(UserProfile)
	old_status = models.CharField(max_length=75, null=True, blank=True)
	new_status = models.CharField(max_length=75, null=True, blank=True)
	date_time = models.DateTimeField(auto_now_add=True, editable=True)

	def __str__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s, %s, %s, %s" % (self.application_form, user, old_status, new_status)