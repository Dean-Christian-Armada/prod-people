# from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile
from people.models import *

import datetime

def null_default_foreign_key_value(model, field, value):
	param = {field:value}
	query = model.objects.get_or_create(**param)
	query = model.objects.get(**param)
	return query.id

class Evaluations(models.Model):
	evaluations = models.TextField(null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class PersonReference(models.Model):
	person_reference = models.CharField(max_length=100, null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.person_reference

class Company(models.Model):
	company = models.CharField(max_length=100, null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.company

class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.birth_place

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, default=None)
	manship_standard = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_name

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=False)
	manship_standard = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.vessel_type.upper()

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.civil_status

class MarinerStatus(models.Model):
	mariner_status = models.CharField(max_length=50, null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

	def __unicode__(self):
		return self.mariner_status

class Colleges(models.Model):
	college_name = models.CharField(max_length=100, default=None)
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.college_name

class Degree(models.Model):
	degree = models.CharField(max_length=100, default=None)
	company_standard = models.NullBooleanField(default=True)
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

class Vocationals(models.Model):
	vocational_name = models.CharField(max_length=100, null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True)
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.vocational_name

class PrimarySchools(models.Model):
	primaryschool_name = models.CharField(max_length=100, null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.primaryschool_name

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.relationship

class Departments(models.Model):
	department = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s - %s" % (self.id, self.department)

class Rank(models.Model):
	department = models.ForeignKey(Departments, default=null_default_foreign_key_value(Departments, 'department', ''))
	rank = models.CharField(max_length=50, default=None)
	hiring = models.BooleanField(default=False)
	company_standard = models.NullBooleanField(default=True)
	# Application Form Ordering Dorpdown Purposes
	order = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.rank.upper()

class COCRank(models.Model):
	coc_rank = models.CharField(max_length=50, null=True, blank=True, default=None)
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.coc_rank.upper()

class LandPosition(models.Model):
	land_position = models.CharField(max_length=50, null=True, blank=True, default=None)
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.land_position

class EngineType(models.Model):
	engine_type = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.engine_type

class ManningAgency(models.Model):
	manning_agency = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=True)
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
	company_standard = models.NullBooleanField(default=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.municipality

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=True)
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
	english = models.CharField(max_length=50, default=None, null=True, blank=True)

	def __unicode__(self):
		return self.english

class Dialect(models.Model):
	dialect = models.CharField(max_length=50, default=None, null=True, blank=True)

	def __unicode__(self):
		return self.dialect

# class Position(models.Model):
# 	position = models.CharField(max_length=50, default=None)

class Bank(models.Model):
	bank = models.CharField(max_length=50, default=None,)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.bank

class Branch(models.Model):
	branch = models.CharField(max_length=50, default=None,)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.branch

class PassportPlaceIssued(models.Model):
	passport_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.passport_place

class SBookPlaceIssued(models.Model):
	sbook_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.sbook_place

class USVisaPlaceIssued(models.Model):
	us_visa_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.us_visa_place

class SchengenVisaPlaceIssued(models.Model):
	schengen_visa_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.schengen_visa_place

class YellowFeverPlaceIssued(models.Model):
	yellow_fever_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.yellow_fever_place

class LicensePlaceIssued(models.Model):
	license_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.license_place

class COCPlaceIssued(models.Model):
	coc_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.coc_place

class TrainingPlaceIssued(models.Model):
	training_place = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.training_place

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
	company_standard = models.NullBooleanField(default=True)
	manship_standard = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.flags

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, default=None)
	trainings_certificates_abbreviation = models.CharField(max_length=15, null=True, blank=True, default=None)
	departments = models.ManyToManyField(Departments, blank=True)
	company_standard = models.NullBooleanField(default=True)
	national_certificate = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.trainings_certificates

	def get_departments(self):
		return "\n, ".join([d.department for d in self.departments.all()])

class Principal(models.Model):
	principal = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(default=False)
	manship_standard = models.BooleanField(default=False)
	flags_standard = models.ManyToManyField(Flags, blank=True)
	trainings_certificate_standard = models.ManyToManyField(TrainingCertificates, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.principal.upper()

class TrainingCenter(models.Model):
	training_center = models.CharField(max_length=50, default=None, blank=True)
	company_standard = models.NullBooleanField(default=True)

	def __unicode__(self):
		return self.training_center

class TradeArea(models.Model):
	trade_area = models.CharField(max_length=50, default=None, null=True, blank=True)
	company_standard = models.NullBooleanField()

	def __unicode__(self):
		return self.trade_area

class CurrentAddress(models.Model):
	current_zip = models.ForeignKey(Zip, default=None)
	current_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	current_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.current_unit, self.current_street, self.current_zip.barangay, self.current_zip.municipality, self.current_zip)

class PermanentAddress(models.Model):
	permanent_zip = models.ForeignKey(Zip, default=None)
	permanent_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	permanent_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return "%s %s %s %s %s" % (self.permanent_unit, self.permanent_street, self.permanent_zip.barangay, self.permanent_zip.municipality, self.permanent_zip)

class PersonalData(AbstractPersonalData):
	# pass
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)
	dialect = models.ForeignKey(Dialect, default=1)
	english = models.ForeignKey(English, default=1)

class Spouse(AbstractSpouseData):
	pass

class College(AbstractCollege):
	pass

class HighSchool(AbstractHighSchool):
	pass

class Vocational(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	vocational = models.ForeignKey(Vocationals, null=True, blank=True, default=None)
	vocationalyear_from = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
	vocationalyear_to = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.vocational, self.vocationalyear_from, self.vocationalyear_to)

class PrimarySchool(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	primaryschool = models.ForeignKey(PrimarySchools, null=True, blank=True, default=None)
	primaryschoolyear_from = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
	primaryschoolyear_to = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.primaryschool, self.primaryschoolyear_from, self.primaryschoolyear_to)


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
	sbook_date_expiry = models.DateField(default=None, null=True, blank=True)

class COC(AbstractCOC):
	coc_date_issued = models.DateField(default=None, null=True, blank=True)
	coc_grade = models.CharField(max_length=50, default=None, null=True, blank=True)
	coc_place_issued = models.ForeignKey(COCPlaceIssued, default=1, blank=True)

class License(AbstractLicense):
	license_date_issued = models.DateField(default=None, null=True, blank=True)
	license_expiry = models.DateField(default=None, null=True, blank=True)
	license_grade = models.CharField(max_length=50, default=None, null=True, blank=True)
	license_place_issued = models.ForeignKey(LicensePlaceIssued, default=1, blank=True)

class NTCLicense(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	ntc_license = models.CharField(max_length=100, unique=True, default=None)
	ntc_license_date_issued = models.DateField(default=None, null=True, blank=True)
	ntc_license_date_expiry = models.DateField(default=None, null=True, blank=True)
	ntc_license_rank = models.ForeignKey(Rank, default=null_default_foreign_key_value(Rank, 'rank', ''))

class SRC(AbstractSRC):
	src_date_issued = models.DateField(default=None, null=True, blank=True)
	src_expiry = models.DateField(default=None, null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.src_date_issued == '':
			self.src_date_issued = None
		if self.src_expiry == '':
			self.src_expiry = None
		super(SRC, self).save(*args, **kwargs)

class STCWEndorsement(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	stcw_endorsement = models.CharField(max_length=100, unique=True, default=None)
	stcw_endorsement_date_issued = models.DateField(default=None, null=True, blank=True)
	stcw_endorsement_date_expiry = models.DateField(default=None, null=True, blank=True)
	stcw_endorsement_rank = models.ForeignKey(Rank, default=null_default_foreign_key_value(Rank, 'rank', ''))

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.primaryschool, self.primaryschoolyear_from, self.primaryschoolyear_to)


class STCWCertificate(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	stcw_certificate = models.CharField(max_length=100, unique=True, default=None)
	stcw_certificate_date_issued = models.DateField(default=None, null=True, blank=True)
	stcw_certificate_date_expiry = models.DateField(default=None, null=True, blank=True)
	stcw_certificate_rank = models.ForeignKey(Rank, default=null_default_foreign_key_value(Rank, 'rank', ''))

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return "%s - %s / %s-%s" % (user, self.primaryschool, self.primaryschoolyear_from, self.primaryschoolyear_to)

class GOC(AbstractGOC):
	goc_date_issued = models.DateField(default=None, null=True, blank=True)
	goc_rank = models.ForeignKey('mariners_profile.Rank', default=null_default_foreign_key_value(Rank, 'rank', ''))

class USVisa(AbstractUSVisa):
	# pass
	us_visa_place_issued = models.ForeignKey(USVisaPlaceIssued, blank=True)
	us_visa_date_issued = models.DateField(default=None, null=True, blank=True)
	us_visa_number = models.PositiveIntegerField(null=True, blank=True, default=None)

class SchengenVisa(AbstractSchengenVisa):
	# pass
	schengen_visa_place_issued = models.ForeignKey(SchengenVisaPlaceIssued, blank=True)
	schengen_visa_date_issued = models.DateField(default=None, null=True, blank=True)
	schengen_visa_number = models.PositiveIntegerField(null=True, blank=True, default=None)

class YellowFever(AbstractYellowFever):
	# pass
	yellow_fever_place_issued = models.ForeignKey(YellowFeverPlaceIssued, blank=True)
	yellow_fever_date_issued = models.DateField(default=None, null=True, blank=True)

class FlagDocuments(AbstractFlagDocuments):
	flags = models.ManyToManyField(Flags, through='mariners_profile.FlagDocumentsDetailed', blank=True, default=None)

class FlagDocumentsDetailed(models.Model):
	flags_documents = models.ForeignKey(FlagDocuments, on_delete=models.CASCADE)
	flags = models.ForeignKey(Flags, on_delete=models.CASCADE)
	sbook_number = models.PositiveIntegerField(null = True, blank=True)
	sbook_expiry = models.DateField(null=True, blank=True)
	license_number = models.PositiveIntegerField(null = True, blank=True)
	license_expiry = models.DateField(null=True, blank=True)
	flags_rank = models.ForeignKey('mariners_profile.Rank', default=null_default_foreign_key_value(Rank, 'rank', ''))

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
	expiry = models.DateField(default=None, null=True, blank=True)
	place_trained = models.ForeignKey(TrainingCenter, default=null_default_foreign_key_value(TrainingCenter, 'training_center', ''))
	training_place_issued = models.ForeignKey(TrainingPlaceIssued, default=null_default_foreign_key_value(TrainingPlaceIssued, 'training_place', ''))

	def __unicode__(self):
		user = "%s %s %s" % (self.trainings_certificate_documents.user.first_name, self.trainings_certificate_documents.user.middle_name, self.trainings_certificate_documents.user.last_name)
		return "%s - %s" % (user, self.trainings_certificates.trainings_certificates)

class PrincipalVesselType(models.Model):
	principal = models.ForeignKey(Principal)
	vessel_type = models.ManyToManyField(VesselType)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.principal.principal

class SeaService(AbstractSeaService):
	# pass
	trade_area = models.ForeignKey(TradeArea)
	
	def bhp(self):
		bhp = float(self.kw) * 0.746
		return bhp	

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
	date_hired = models.DateField(default=None, null=True, blank=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		user = "%s %s %s" % (self.user.first_name, self.user.middle_name, self.user.last_name)
		return user

class MarinerStatusComment(models.Model):
	mariner_status_comment = models.TextField(default=None, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __unicode__(self):
		return self.mariner_status_comment

class MarinerStatusHistory(models.Model):
	user = models.ForeignKey(UserProfile, related_name='mariner_user', default=None)
	# updated_by = models.ForeignKey(UserProfile, related_name='updated_by', default=None)
	updated_on = models.DateField(auto_now_add=True)
	mariner_principal = models.ForeignKey(Principal, default=null_default_foreign_key_value(Principal, 'principal', ''))
	mariner_status = models.ForeignKey(MarinerStatus, default=null_default_foreign_key_value(MarinerStatus, 'mariner_status', ''))
	since = models.DateField(null=True, blank=True, default=None)
	until = models.DateField(null=True, blank=True, default=None)
	mariner_status_comment = models.ForeignKey(MarinerStatusComment, default=null_default_foreign_key_value(MarinerStatusComment, 'mariner_status_comment', ''))

	def __unicode__(self):
		value = "%s %s %s - %s - %s" % (self.user.first_name, self.user.middle_name, self.user.last_name, self.mariner_principal, self.mariner_status)
		return value

	def days(self):
		since = self.since
		until = self.until
		if not self.until:
			until = datetime.date.today()
		days = until - since
		days = str(days).split(' ')
		days = days[0]
		# not yet working
		print until
		return days

	def str_mariner_status_comment(self):
		comment = str(self.mariner_status_comment)
		if comment == '':
			comment = "THERE ARE NO COMMENTS"
		return comment

class NonConformingSeafarerReason(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	non_conforming_reason = models.TextField(default=None)

	def __unicode__(self):
		value = "%s %s %s - %s" % (self.user.first_name, self.user.middle_name, self.user.last_name, self.non_conforming_reason)	

# Used in Reference in failed cases
class NegativeSeagoingHistory(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	seagoing_comments = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

# Used in Reference in failed cases
class NegativeHealthProblems(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	health_problems = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Reference(models.Model):
	user = models.ForeignKey(UserProfile, related_name="user_mariner", default=None)
	verified_by = models.ForeignKey(UserProfile, related_name="verified_by", default=None)
	company = models.ForeignKey(Company, default=None)
	date = models.DateField(null=True, blank=True, default=None)
	person_contacted = models.ForeignKey(PersonReference, default=None)
	veracity_seagoing_history = models.NullBooleanField(default=1)
	health_problem = models.NullBooleanField(default=0)
	financial_liability = models.NullBooleanField(default=1)
	rehiring_prospects = models.NullBooleanField(default=1)
	character = models.TextField(null=True, blank=True, default=None)
	comments = models.TextField(null=True, blank=True, default=None)

	def __unicode__(self):
		return unicode(self.verified_by)

class Evaluation(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	# evalutation = models.ForeignKey(Evaluations, default=None)
	evaluation = models.TextField(null=True, blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	def __str__(self):
		return "%s - %s" % (self.user, self.evaluation)

class Dependents(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	dependent_relationship = models.ForeignKey('mariners_profile.Relationship', default=None)
	dependent_zip = models.ForeignKey('mariners_profile.Zip', default=None)
	dependent_first_name = models.CharField(max_length=50, null=True, default=None)
	dependent_middle_name = models.CharField(max_length=50, null=True, default=None)
	dependent_last_name = models.CharField(max_length=50, null=True, default=None)
	dependent_contact = models.BigIntegerField(null=True, blank=True, default=None)
	dependent_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	dependent_unit = models.CharField(max_length=50, null=True, blank=True, default=None)

	def __unicode__(self):
		user = "%s %s %s" % (self.dependent_first_name, self.dependent_middle_name, self.dependent_last_name)
		return user

	def prefix_dependent_contact(self):
		count =  len(str(self.dependent_contact))
		if count == 10:
			self.dependent_contact = '+63'+str(self.dependent_contact)
		return self.dependent_contact

class LandEmployment(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	employer_first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	employer_middle_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	employer_last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	land_position = models.ForeignKey(LandPosition, default=None)
	start_date = models.DateField(default=None, null=True, blank=True)
	end_date = models.DateField(default=None, null=True, blank=True)
	contact_first_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	contact_middle_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	contact_last_name = models.CharField(max_length=50, null=True, blank=True, default=None)
	contact_person_number =  models.BigIntegerField(null=True, blank=True, default=None)
	employer_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	employer_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	employer_zip = models.ForeignKey('mariners_profile.Zip', default=None)

	def __unicode__(self):
		employer = "%s %s %s" % (self.employer_first_name, self.employer_middle_name, self.employer_last_name)
		return employer

class Beneficiary(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	beneficiary_first_name = models.CharField(max_length=50, null=True, default=None)
	beneficiary_middle_name = models.CharField(max_length=50, null=True, default=None)
	beneficiary_last_name = models.CharField(max_length=50, null=True, default=None)
	beneficiary_relationship = models.ForeignKey(Relationship, default=None)
	beneficiary_number = models.BigIntegerField(null=True, blank=True, default=None)

	def __unicode__(self):
		beneficiary = "%s %s %s" % (self.beneficiary_first_name, self.beneficiary_middle_name, self.beneficiary_last_name)
		return beneficiary

class Allotee(models.Model):
	user = models.ForeignKey(UserProfile, default=None)
	allotee_first_name = models.CharField(max_length=50, null=True, default=None)
	allotee_middle_name = models.CharField(max_length=50, null=True, default=None)
	allotee_last_name = models.CharField(max_length=50, null=True, default=None)
	allotee_relationship = models.ForeignKey(Relationship, default=None)
	allotee_number = models.BigIntegerField(null=True, blank=True, default=None)
	allotee_unit = models.CharField(max_length=50, null=True, blank=True, default=None)
	allotee_street = models.CharField(max_length=50, null=True, blank=True, default=None)
	allotee_zip = models.ForeignKey('mariners_profile.Zip', default=None)
	bank = models.ForeignKey(Bank, default=None)
	allotment_account_number = models.BigIntegerField(null=True, blank=True, default=None)