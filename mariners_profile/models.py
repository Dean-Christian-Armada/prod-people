# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import *



class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.birth_place

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_name

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_type

class Principal(models.Model):
	principal = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.principal

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.civil_status

class Colleges(models.Model):
	college_name = models.CharField(max_length=100, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.college_name

class Degree(models.Model):
	degree = models.CharField(max_length=100, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.degree

class HighSchools(models.Model):
	highschool_name = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.highschool_name

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.relationship

class Rank(models.Model):
	rank = models.CharField(max_length=50, default=None)
	hiring = models.BooleanField(default=0)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	# Application Form Ordering Dorpdown Purposes
	order = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.rank

class COCRank(models.Model):
	coc_rank = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.coc_rank

class EngineType(models.Model):
	engine_type = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.engine_type

class ManningAgency(models.Model):
	manning_agency = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.manning_agency

class CauseOfDischarge(models.Model):
	cause_of_discharge = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.cause_of_discharge

class Municipality(models.Model):
	municipality = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.municipality

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.barangay

class Sources(models.Model):
	source = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.source

class Specifics(models.Model):
	specific = models.CharField(max_length=50, default=None, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.specific

class Reasons(models.Model):
	reason = models.TextField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.reason

class Status(models.Model):
	status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.status

class English(models.Model):
	english = models.CharField(max_length=50, default=None)

class Dialect(models.Model):
	dialect = models.CharField(max_length=50, default=None)

class Position(models.Model):
	position = models.CharField(max_length=50, default=None)

class Bank(models.Model):
	bank = models.CharField(max_length=50, default=None,)

class Branch(models.Model):
	branch = models.CharField(max_length=50, default=None,)

class PassportPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(max_length=50, default=True)

	def __unicode__(self):
		return self.place

class SBookPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(max_length=50, default=True)

	def __unicode__(self):
		return self.place

class Zip(models.Model):
	zip = models.PositiveIntegerField(unique=True, default=None)
	barangay = models.ForeignKey(Barangay, default=None)
	municipality = models.ForeignKey(Municipality, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return unicode(self.zip)

class Flags(models.Model):
	flags = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.flags

class TrainingCertificatesSegregation(models.Model):
	segregation = models.CharField(max_length=50, default=None)

	def __unicode__(self):
		return self.segregation

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, default=None)
	segregation = models.ForeignKey(TrainingCertificatesSegregation, default=1)
	company_standard = models.NullBooleanField(max_length=50, default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.trainings_certificates

class TrainingCenter(models.Model):
	training_center = models.CharField(max_length=50, default=None, blank=True)

	def __unicode__(self):
		return self.training_center

class CurrentAddress(models.Model):
	current_zip = models.ForeignKey(Zip, default=None)
	current_unit = models.CharField(max_length=50, default=None)
	current_street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.current_unit, self.current_street, self.current_zip.barangay, self.current_zip.municipality, self.current_zip)

class PermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, default=None)
	permanent_street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.permanent_unit, self.permanent_street, self.permanent_zip.barangay, self.permanent_zip.municipality, self.permanent_zip)

class PersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)

class Spouse(AbstractSpouseData):
	pass

class College(AbstractCollege):
	pass

class HighSchool(AbstractHighSchool):
	pass

class EmergencyContact(AbstractEmergencyContact):
	pass

class VisaApplication(AbstractVisaApplication):
	pass
	
class Detained(AbstractDetained):
	pass	

class DisciplinaryAction(AbstractDisciplinaryAction):
	pass

class ChargedOffense(AbstractChargedOffense):
	pass
	
class Termination(AbstractTermination):
	pass	

class Passport(AbstractPassport):
	passport_place_issued = models.ForeignKey(PassportPlaceIssued, default=None, blank=True)
	passport_date_issued = models.DateField(default=None, null=True, blank=True)

class Sbook(AbstractSbook):
	sbook_place_issued = models.ForeignKey(SBookPlaceIssued, default=None, blank=True)
	sbook_date_issued = models.DateField(default=None, null=True, blank=True)

class COC(AbstractCOC):
	coc_date_issued = models.DateField(default=None, null=True, blank=True)

class License(AbstractLicense):
	license_expiry = models.DateField(default=None, null=True, blank=True)
	license_date_issued = models.DateField(default=None, null=True, blank=True)

class SRC(AbstractSRC):
	src_expiry = models.DateField(default=None, null=True, blank=True)
	src_date_issued = models.DateField(default=None, null=True, blank=True)
	
class GOC(AbstractGOC):
	goc_date_issued = models.DateField(default=None, null=True, blank=True)
	# goc_rank = models.ForeignKey('mariners_profile.Rank', default=None)

class USVisa(AbstractUSVisa):
	pass
	# us_visa_place_issued = models.ForeignKey(USVisaPlaceIssued, default=None, blank=True)

class SchengenVisa(AbstractSchengenVisa):
	pass
	# schengen_visa_place_issued = models.ForeignKey(SchengenVisaPlaceIssued, default=None, blank=True)

class YellowFever(AbstractYellowFever):
	pass
	# yellow_fever_place_issued = models.ForeignKey(YellowFeverPlaceIssued, default=None, blank=True)
	# yellow_fever_date_issued = models.DateField(default=None, null=True, blank=True)

class FlagDocuments(AbstractFlagDocuments):
	flags = models.ManyToManyField(Flags, through='mariners_profile.FlagDocumentsDetailed', blank=True, default=None)

class FlagDocumentsDetailed(models.Model):
	flags_documents = models.ForeignKey(FlagDocuments, on_delete=models.CASCADE)
	flags = models.ForeignKey(Flags, on_delete=models.CASCADE)
	sbook_number = models.PositiveIntegerField(null = True, blank=True)
	sbook_expiry = models.DateField(null=True, blank=True)
	license_number = models.PositiveIntegerField(null = True, blank=True)
	license_expiry = models.DateField(null=True, blank=True)

	def __unicode__(self):
		user = "%s %s %s" % (self.flags_documents.user.first_name, self.flags_documents.user.middle_name, self.flags_documents.user.last_name)
		return "%s - %s" % (user, self.flags.flags)

class TrainingCertificateDocuments(AbstractTrainingCertificateDocuments):
	trainings_certificates = models.ManyToManyField(TrainingCertificates, default=None)

class TrainingCertificateDocumentsDetailed(models.Model):
	trainings_certificate_documents = models.ForeignKey(TrainingCertificateDocuments, on_delete=models.CASCADE)
	trainings_certificates = models.ForeignKey(TrainingCertificates, on_delete=models.CASCADE)
	number = models.PositiveIntegerField(null=True, blank=True)
	issued = models.DateField(null=True, blank=True)
	place_trained = models.ForeignKey(TrainingCenter)

class SeaService(AbstractSeaService):
	pass

# This is a temporary model object for the referrer's pool
class ReferrersPool(models.Model):
	# first_name = models.CharField(max_length=30, default=None)
	# middle_name = models.CharField(max_length=30, default=None, blank=True)
	# last_name = models.CharField(max_length=30, default=None)
	name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.name

	# def name(self):
	# 	return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

class MarinersProfile(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	status = models.NullBooleanField(default=0)
	# ForeignKey temporarily at ReferrersPool
	# Eventually will be a foreign key to UserProfile
	referrer = models.ForeignKey(ReferrersPool)
	position = models.ForeignKey(Rank)
	picture = models.ImageField(upload_to='photos/mariners-profile', blank=True, default=None)
	signature = models.ImageField(upload_to='signatures/mariners-profile', blank=True, default=None)

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user