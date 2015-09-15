from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django_date_extensions.fields import ApproximateDateField

from login.models import UserProfile

# Notes
#  Use ModelBase / class model inheritance for created and modified
# change user onetoone field

# START NORMALIZATION

# ManyToMany Fields for 3NFs

class TrainingCenter(models.Model):
	training_center = models.CharField(max_length=50, default=None)


class Flags(models.Model):
	flags = models.CharField(max_length=50, default=None)
	company_standard = models.NullBooleanField(max_length=50, default=False)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )
class FlagDocuments(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	flags = models.ManyToManyField(Flags, through='FlagDocumentsDetailed', blank=True, default=None)
class FlagDocumentsDetailed(models.Model):
	flags_documents = models.ForeignKey(FlagDocuments, on_delete=models.CASCADE)
	flags = models.ForeignKey(Flags, on_delete=models.CASCADE)
	sbook_number = models.PositiveIntegerField()
	sbook_expiry = models.DateField()
	license_number = models.PositiveIntegerField()
	license_expiry = models.DateField()

class TrainingCertificates(models.Model):
	trainings_certificates = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )
class TrainingCertificateDocuments(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	trainings_certificates = models.ManyToManyField(TrainingCertificates, default=None)
class TrainingCertificateDocumentsDetailed(models.Model):
	trainings_certificate_documents = models.ForeignKey(TrainingCertificateDocuments, on_delete=models.CASCADE)
	number = models.PositiveIntegerField()
	issued = models.DateField()
	place_trained = models.OneToOneField(TrainingCenter)

# Foreign Models for 2NFs
class BirthPlace(models.Model):
	birth_place = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class VesselName(models.Model):
	vessel_name = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class VesselType(models.Model):
	vessel_type = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Principal(models.Model):
	principal = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CivilStatus(models.Model):
	civil_status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class Colleges(models.Model):
	college = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class Degree(models.Model):
	degree = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class HighSchools(models.Model):
	highschool = models.CharField(max_length=100, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	# full_name = models.CharField(max_length=100, default=None)

class Relationship(models.Model):
	relationship = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Rank(models.Model):
	rank = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class EngineType(models.Model):
	engine_type = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class ManningAgency(models.Model):
	manning_agency = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CauseOfDischarge(models.Model):
	cause_of_discharge = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Municipality(models.Model):
	municipality = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Barangay(models.Model):
	barangay = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Sources(models.Model):
	source = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Specifics(models.Model):
	specific = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Reasons(models.Model):
	reason = models.TextField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Status(models.Model):
	status = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class English(models.Model):
	english = models.CharField(max_length=50, default=None)

class Dialect(models.Model):
	dialect = models.CharField(max_length=50, default=None)

class Position(models.Model):
	position = models.CharField(max_length=50, default=None)

class Bank(models.Model):
	bank = models.CharField(max_length=50, default=None)

class Branch(models.Model):
	branch = models.CharField(max_length=50, default=None)

class PassportPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None)

class SBookPlaceIssued(models.Model):
	place = models.CharField(max_length=50, default=None)

# Foreign Models for 1NFs

class Spouse(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	name = models.CharField(max_length=100, blank=True, default=None)
	married_date = models.DateField(blank=True, default=None)
	birthdate = models.DateField(blank=True, default=None)
	contact = models.CharField(max_length=100, blank=True, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class College(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	college = models.ForeignKey(Colleges, related_name='Colleges', default=None)
	degree = models.ForeignKey(Degree, default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class HighSchool(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	highschool = models.ForeignKey(HighSchools, related_name='Highschools', default=None)
	schoolyear_from = models.PositiveSmallIntegerField(default=None)
	schoolyear_to = models.PositiveSmallIntegerField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

class Zip(models.Model):
	zip = models.PositiveIntegerField(default=None)
	barangay = models.ForeignKey(Barangay, default=None)
	municipality = models.ForeignKey(Municipality, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class EmergencyContact(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	relationship = models.ForeignKey(Relationship, default=None)
	zip = models.ForeignKey(Zip, default=None)
	name = models.CharField(max_length=100, default=None)
	contact = models.CharField(max_length=100, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class CurrentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class PermanentAddress(models.Model):
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class AppSource(models.Model):
	source = models.ForeignKey(Sources, default=None)
	specific = models.ForeignKey(Specifics, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )

# START Background Info
class VisaApplication(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	visa_application = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Detained(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	detained = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class DisciplinaryAction(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	disciplinary_action = models.NullBooleanField(default=None)
	reason = models.ForeignKey(Reasons, default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )
# END Background Info


class Passport(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	passport = models.CharField(max_length=100, unique=True, default=None)
	expiry = models.DateField(default=None)
	place_issued = models.ForeignKey(PassportPlaceIssued, default=None, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class Sbook(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	sbook = models.CharField(max_length=100, unique=True, default=None)
	sbook_expiry = models.DateField(default=None)
	place_issued = models.ForeignKey(SBookPlaceIssued, default=None, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class COC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	coc = models.CharField(max_length=100, unique=True, default=None)
	issued = models.DateField(default=None)
	coc_expiry = models.DateField(default=None)
	rank = models.ForeignKey(Rank, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class License(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	license = models.CharField(max_length=100, unique=True, default=None)
	license_issued = models.DateField(default=None)
	license_expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class SRC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	src = models.CharField(max_length=100, unique=True, default=None)
	src_issued = models.DateField(default=None)
	src_expiry = models.DateField(default=None)
	src_rank = models.ForeignKey(Rank, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class GOC(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	goc = models.CharField(max_length=100, unique=True, default=None)
	goc_issued = models.DateField(default=None)
	goc_expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class USVisa(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	us_visa = models.CharField(max_length=100, unique=True, default=None)
	us_visa_expiry = models.DateField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class SchengenVisa(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	schengen_visa = models.CharField(max_length=100, unique=True, default=None)
	schengen_visa_expiry = models.DateField(blank=True, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class YellowFever(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	yellow_fever = models.CharField(max_length=100, unique=True, default=None)
	yellow_fever_expiry = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class LandEmployment(models.Model):
	user = models.OneToOneField(UserProfile, default=None)

	employer_name =  models.CharField(max_length=100, default=None)
	position = models.ForeignKey(Position, default=None)
	date_from = models.DateField()
	date_to = models.DateField()
	contact_person = models.CharField(max_length=100, default=None)
	contact_number = models.BigIntegerField()
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class BeneficiaryDetails(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	last_name = models.CharField(max_length=30, default=None)
	first_name = models.CharField(max_length=30, default=None)
	middle_name = models.CharField(max_length=30, default=None)
	relationship = models.ForeignKey(Relationship, default=None)
	contact_number = models.BigIntegerField()
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class AllotmentDetails(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	allottee_name =  models.CharField(max_length=100, default=None)
	relationship = models.ForeignKey(Relationship, default=None)
	zip = models.ForeignKey(Zip, default=None)
	unit = models.CharField(max_length=50, default=None)
	street = models.CharField(max_length=50, default=None)
	contact_number = models.BigIntegerField()
	bank = models.ForeignKey(Bank, default=None)
	branch = models.ForeignKey(Branch, default=None)
	account_number = models.BigIntegerField()
	
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

class STCWEndorsement(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	issued = models.DateField(default=None)
	expiry = models.DateField(default=None)
	rank = models.ForeignKey(Rank, default=None)

class STCWCertificate(models.Model):
	user = models.OneToOneField(UserProfile, default=None)
	issued = models.DateField(default=None)
	expiry = models.DateField(default=None)
	rank = models.ForeignKey(Rank, default=None)


# END NORMALIZATION


class PersonalData(models.Model):
	# Regex
	# regex for mobile numbers
	mobile_regex = RegexValidator(regex=r'^09([0-9]{9})$', message="Please input proper mobile number format 09xxxxxxxxx")
	# regex for landline numbers
	landline_regex = RegexValidator(regex=r'^([0-9]{7})$', message="Please input proper 7 digit telephone number format")
	# regex for sss
	sss_regex = RegexValidator(regex=r'^([0-9]{10})$', message="Please input proper 10 digit format of sss")
	# regex for philhealth
	philhealth_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of philhealth")
	# regex for tin
	tin_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of tin")
	# regex for pagibig
	pagibig_regex = RegexValidator(regex=r'^([0-9]{12})$', message="Please input proper 12 digit format of pagibig")
	# twelvedigit_regex = RegexValidator(regex=r'^([0-9]{12})$', message="This id contains 12 digit number") 

	# OneToOneField with Django Users Model 
	name = models.OneToOneField(UserProfile, default=None)

	# ForeignKeys
	birth_place = models.ForeignKey(BirthPlace, default=None)
	preferred_vessel_type = models.ForeignKey(VesselType, default=None)
	civil_status = models.ForeignKey(CivilStatus, default=None)
	current_address = models.ForeignKey(CurrentAddress, default=None)
	permanent_address = models.ForeignKey(PermanentAddress, default=None)
	english = models.ForeignKey(English, blank=True, default=None)
	dialect = models.ForeignKey(Dialect, blank=True, default=None)

	

	# CharFields
	mobile_1 = models.BigIntegerField(validators=[mobile_regex], default=None)
	mobile_2 = models.BigIntegerField(validators=[mobile_regex], blank=True, default=None)
	father_name = models.CharField(max_length=100, default=None)
	mother_name = models.CharField(max_length=100, default=None)

	# Integer Fields
	age = models.PositiveIntegerField(default=None)
	landline_1 = models.PositiveIntegerField(validators=[landline_regex], blank=True, default=None)
	landline_2 = models.PositiveIntegerField(validators=[landline_regex], blank=True, default=None)
	sss = models.PositiveIntegerField(validators=[sss_regex], default=None)
	philhealth = models.BigIntegerField(validators=[philhealth_regex], blank=True, default=None)
	tin = models.BigIntegerField(validators=[tin_regex], blank=True, default=None)
	pagibig = models.BigIntegerField(validators=[pagibig_regex], blank=True, default=None)

	# EmailFields
	email_address_1 = models.EmailField(default=None)
	email_address_2 = models.EmailField(blank=True, default=None)

	# DateFields
	birth_date = models.DateField(default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	# ThirdParty Fields
	availability_date = ApproximateDateField(default=None)


class SeaService(models.Model):

	# OneToOneField with Django Users Model 
	user = models.OneToOneField(UserProfile, default=None)

	# ForeignKeys
	vessel_name = models.ForeignKey(VesselName, default=None)
	vessel_type = models.ForeignKey(VesselType, default=None)
	flag = models.ForeignKey(Flags, default=None)
	engine_type = models.ForeignKey(EngineType, default=None)
	manning_agency = models.ForeignKey(ManningAgency, default=None)
	principal = models.ForeignKey(Principal, default=None)
	rank = models.ForeignKey(Rank, default=None)
	cause_of_discharge = models.ForeignKey(CauseOfDischarge, default=None)

	# Integer Fields
	grt = models.PositiveIntegerField(default=None)
	dwt = models.PositiveIntegerField(default=None)
	year_built = models.PositiveSmallIntegerField(default=None)
	duration = models.PositiveSmallIntegerField(default=None)

	# Decimal Fields
	hp = models.DecimalField(decimal_places=1, max_digits=10, default=None)
	kw = models.DecimalField(decimal_places=1, max_digits=10, default=None)

	# Date Fields
	date_joined = models.DateField(default=None)
	date_left = models.DateField(default=None)
	date_modified = models.DateTimeField(auto_now=True, blank=True, )


class AppForm(models.Model):

	# OneToOneField with Django Users Model 
	user = models.OneToOneField(UserProfile, default=None)
	
	# ForeignKeys
	position_applied = models.ForeignKey(Rank, related_name="position_applied", default=None)
	alternative_position = models.ForeignKey(Rank, related_name="alternative_position", default=None)
	application_source = models.ForeignKey(AppSource, default=None)
	status = models.ForeignKey(Status, default=None)

	# Image Fields
	picture = models.ImageField(upload_to='application/pictures', blank=True, default=None)
	signatures = models.ImageField(upload_to='application/signatures', blank=True, default=None)

	# Date Fields
	application_date = models.DateField(default=None)
	date_created = models.DateTimeField(auto_now_add=True, )
	date_modified = models.DateTimeField(auto_now=True, blank=True, )

	# Text Field
	essay = models.TextField(default=None)

# class Verification(models.Model):
# 	verfied_by = models.CharField(max_length=100)
# 	company = models.ForeignKey(Company, default=None)