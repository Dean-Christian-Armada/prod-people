from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db.models import Q
from django.conf import settings
from django import forms

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from jsignature.utils import draw_signature

from .models import *
from login.models import UserProfile, Userlevel
from mariners_profile.models import *

from datetime import date

import os, sys, shutil, autocomplete_light

# All data input processes are located here
# def clean processes the insert data on the mariners profile


# Renders manually made for horizontal selections
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizontalCheckboxRenderer(forms.CheckboxSelectMultiple.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class ApplicantNameForm(forms.ModelForm):
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Last Name", 'data-toggle':'tooltip'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"First Name", 'data-toggle':'tooltip'}))
	middle_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Middle Name", 'data-toggle':'tooltip'}))
	
	class Meta:
		model = UserProfile
		fields = ('last_name', 'first_name', 'middle_name')

	def save(self, commit=True):
		userprofile = super(ApplicantNameForm, self).save(commit=False)
		user = User.objects.get(username='applicant')
		userlevel = Userlevel.objects.get(userlevel='applicant')
		userprofile.user = user
		userprofile.userlevel = userlevel
		userprofile.save()
		return userprofile

class PermanentAddressForm(forms.ModelForm):
	permanent_zip = forms.IntegerField()
	permanent_barangay = forms.CharField()
	permanent_municipality = forms.CharField()
	
	class Meta:
		model = ApplicationFormPermanentAddress
		fields = ('permanent_unit', 'permanent_street')

	def save(self, commit=True):
		permanent_zip = self.cleaned_data['permanent_zip']
		permanent_barangay = self.cleaned_data['permanent_barangay']
		permanent_municipality = self.cleaned_data['permanent_municipality']

		permanent_address = super(PermanentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create(municipality=permanent_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality=permanent_municipality)
		barangay = Barangay.objects.get_or_create(barangay=permanent_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay=permanent_barangay)
		try:
			zip = Zip.objects.get_or_create(zip=permanent_zip, barangay=barangay, municipality=municipality)[0]	
		except:
			zip = Zip.objects.get(zip=permanent_zip)
		permanent_address.permanent_zip = zip
		permanent_address.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['permanent_zip'] = zip
		# Remove data not on the Mariners Object fields
		self.cleaned_data.pop("permanent_municipality")
		self.cleaned_data.pop("permanent_barangay")
		value = self.cleaned_data
		PermanentAddress.objects.create(**value)
		return permanent_address


class CurrentAddressForm(forms.ModelForm):
	current_zip = forms.IntegerField()
	current_barangay = forms.CharField()
	current_municipality = forms.CharField()
	
	class Meta:
		model = ApplicationFormCurrentAddress
		fields = ('current_unit', 'current_street')

	def save(self, commit=True):
		current_zip = self.cleaned_data['current_zip']
		current_barangay = self.cleaned_data['current_barangay']
		current_municipality = self.cleaned_data['current_municipality']

		current_address = super(CurrentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create(municipality=current_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality=current_municipality)
		barangay = Barangay.objects.get_or_create(barangay=current_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay=current_barangay)
		try:
			zip = Zip.objects.get_or_create(zip=current_zip, barangay=barangay, municipality=municipality)[0]
		except:
			zip = Zip.objects.get(zip=current_zip)
		current_address.current_zip = zip
		current_address.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['current_zip'] = zip
		# Remove data not on the Mariners Object fields
		self.cleaned_data.pop("current_municipality")
		self.cleaned_data.pop("current_barangay")
		value = self.cleaned_data
		CurrentAddress.objects.create(**value)
		return current_address

class PersonalDataForm(forms.ModelForm):
	birth_place = forms.CharField()
	preferred_vessel_type = forms.CharField(widget=autocomplete_light.TextWidget('VesselTypeAutocomplete'))
	# regex fild for mobile numbersNumberInput 
	mobile_1 = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"})
	mobile_2 = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"}, required=False)
	# regex fild for landline numbers
	landline_1 = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	landline_2 = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	# regex fild for sss
	sss = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input proper 10 digit format of sss"})
	# regex fild for philhealth
	philhealth = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of philhealth"}, required=False)
	# regex fild for tin
	tin = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of tin"}, required=False)
	# regex fild for pagibig
	pagibig = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of pagibig"}, required=False)
	age = forms.IntegerField(error_messages={'required': 'Please Fill up your Date of Birth'})

 
	class Meta:
		model = ApplicationFormPersonalData
		fields = '__all__'
		exclude = ('name', 'birth_place', 'preferred_vessel_type', 'permanent_address', 'current_address')

	def save(self, commit=True):
		birthplace = self.cleaned_data['birth_place']
		vessel_type = self.cleaned_data['preferred_vessel_type']

		personal_data = super(PersonalDataForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		permanent_address = ApplicationFormPermanentAddress.objects.latest('id')
		current_address = ApplicationFormCurrentAddress.objects.latest('id')
		birth_place = BirthPlace.objects.get_or_create(birth_place=birthplace)
		if birth_place:
			birth_place = BirthPlace.objects.get(birth_place=birthplace)
		preferred_vessel_type = VesselType.objects.get_or_create(vessel_type=vessel_type)
		if preferred_vessel_type:
			preferred_vessel_type = VesselType.objects.get(vessel_type=vessel_type)
		personal_data.name = userprofile
		personal_data.birth_place = birth_place
		personal_data.preferred_vessel_type = preferred_vessel_type
		personal_data.permanent_address = permanent_address
		personal_data.current_address = current_address
		personal_data.save()
		# Modify cleaned_data for var arguments on creating data on the Mariners Object
		self.cleaned_data['birth_place'] = birth_place
		self.cleaned_data['preferred_vessel_type'] = preferred_vessel_type
		permanent_address = PermanentAddress.objects.latest('id')
		current_address = CurrentAddress.objects.latest('id')
		self.cleaned_data['permanent_address'] = permanent_address
		self.cleaned_data['current_address'] = current_address
		self.cleaned_data['name'] = userprofile
		value = self.cleaned_data
		PersonalData.objects.create(**value)
		return personal_data

class SpouseForm(forms.ModelForm):
	spouse_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"}, required=False)
	class Meta:
		model = ApplicationFormSpouse
		fields = '__all__'
		exclude = ('user', )

	def save(self, commit=True):
		spouse = super(SpouseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		spouse.user = userprofile
		spouse.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		Spouse.objects.create(**value)

class CollegeForm(forms.ModelForm):
	# college = forms.CharField()
	college = forms.CharField(widget=autocomplete_light.TextWidget('CollegeAutocomplete'))
	degree = forms.CharField(widget=autocomplete_light.TextWidget('DegreeAutocomplete'))
	class Meta:
		model = ApplicationFormCollege
		fields = '__all__'
		exclude = ('user', 'college', 'degree' )

	def save(self, commit=True):
		# Try is used to proceed if second formset onwards is left blank
		try:
			college_name = self.cleaned_data['college']
			degree_obtained = self.cleaned_data['degree']
			college = super(CollegeForm, self).save(commit=False)
			userprofile = UserProfile.objects.latest('id')
			colleges = Colleges.objects.get_or_create(college_name=college_name)
			if colleges:
				colleges = Colleges.objects.get(college_name=college_name)
			degree = Degree.objects.get_or_create(degree=degree_obtained)
			if degree:
				degree = Degree.objects.get(degree=degree_obtained)
			college.user = userprofile
			college.college = colleges
			college.degree = degree
			college.save()
			self.cleaned_data['user'] = userprofile
			self.cleaned_data['college'] = colleges
			self.cleaned_data['degree'] = degree
			value = self.cleaned_data
			College.objects.create(**value)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

class HighSchoolForm(forms.ModelForm):
	highschool = forms.CharField()
	class Meta:
		model = ApplicationFormHighSchool
		fields = '__all__'
		exclude = ('user', 'highschool')

	def save(self, commit=True):
		highschool_name = self.cleaned_data['highschool']
		highschool = super(HighSchoolForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		highschools = HighSchools.objects.get_or_create(highschool_name=highschool_name)
		if highschools:
			highschools = HighSchools.objects.get(highschool_name=highschool_name)
		highschool.user = userprofile
		highschool.highschool = highschools
		highschool.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['highschool'] = highschools
		value = self.cleaned_data
		HighSchool.objects.create(**value)

class EmergencyContactForm(forms.ModelForm):
	relationship = forms.CharField()
	emergency_zip = forms.IntegerField()
	emergency_municipality = forms.CharField()
	emergency_barangay = forms.CharField()
	emergency_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"})
	class Meta:
		model = ApplicationFormEmergencyContact
		fields = '__all__'
		exclude = ('user', 'emergency_zip', 'relationship')

	def save(self, commit=True):
		# Try is used to proceed if second formset onwards is left blank
		try:
			emergency_zip = self.cleaned_data['emergency_zip']
			emergency_barangay = self.cleaned_data['emergency_barangay']
			emergency_municipality = self.cleaned_data['emergency_municipality']
			relationship = self.cleaned_data['relationship']
			emergency_contact = super(EmergencyContactForm, self).save(commit=False)
			userprofile = UserProfile.objects.latest('id')
			municipality = Municipality.objects.get_or_create(municipality=emergency_municipality)
			if municipality:
				municipality = Municipality.objects.get(municipality=emergency_municipality)
			barangay = Barangay.objects.get_or_create(barangay=emergency_barangay)
			if barangay:
				barangay = Barangay.objects.get(barangay=emergency_barangay)
			relationships = Relationship.objects.get_or_create(relationship=relationship)
			if relationships:
				relationships = Relationship.objects.get(relationship=relationship)
			try:
				zip = Zip.objects.get_or_create(zip=emergency_zip, barangay=barangay, municipality=municipality)[0]
			except:
				zip = Zip.objects.get(zip=emergency_zip)
			emergency_contact.user = userprofile
			emergency_contact.emergency_zip = zip
			emergency_contact.relationship = relationships
			emergency_contact.save()
			# Modify cleaned_data for var arguments on creating data on the Mariners Object
			self.cleaned_data['user'] = userprofile
			self.cleaned_data['emergency_zip'] = zip
			self.cleaned_data['relationship'] = relationships
			# Remove data not on the Mariners Object fields
			self.cleaned_data.pop("emergency_municipality")
			self.cleaned_data.pop("emergency_barangay")
			value = self.cleaned_data
			EmergencyContact.objects.create(**value)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

class VisaApplicationForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	visa_application = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	visa_application_reason = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Write your reason here", 'rows':"5", 'style':"display:none"}), required=False)
	class Meta:
		model = ApplicationFormVisaApplication
		fields = ('visa_application', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			visa_application = selfdata['visa_application']
		except:
			visa_application = self.cleaned_data['visa_application']
		if visa_application is None:	
			self.add_error('visa_application', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['visa_application_reason']
		visa_application = super(VisaApplicationForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		visa_application.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		visa_application.visa_application_reason = reasons
		visa_application.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['visa_application_reason'] = reasons
		value = self.cleaned_data
		VisaApplication.objects.create(**value)

class DetainedForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	detained = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	detained_reason = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Write your reason here", 'rows':"5", 'style':"display:none"}), required=False)
	class Meta:
		model = ApplicationFormDetained
		fields = ('detained', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			detained = selfdata['detained']
		except:
			detained = self.cleaned_data['detained']
		if detained is None:	
			self.add_error('detained', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['detained_reason']
		detained = super(DetainedForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		detained.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		detained.detained_reason = reasons
		detained.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['detained_reason'] = reasons
		value = self.cleaned_data
		Detained.objects.create(**value)

class DisciplinaryActionForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	disciplinary_action = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	disciplinary_action_reason = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Write your reason here", 'rows':"5", 'style':"display:none"}), required=False)
	class Meta:
		model = ApplicationFormDisciplinaryAction
		fields = ('disciplinary_action', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			disciplinary_action = selfdata['disciplinary_action']
		except:
			disciplinary_action = self.cleaned_data['disciplinary_action']
		if disciplinary_action is None:	
			self.add_error('disciplinary_action', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['disciplinary_action_reason']
		disciplinary_action = super(DisciplinaryActionForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		disciplinary_action.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		disciplinary_action.disciplinary_action_reason = reasons
		disciplinary_action.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['disciplinary_action_reason'] = reasons
		value = self.cleaned_data
		DisciplinaryAction.objects.create(**value)

class ChargedOffenseForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	charged_offense = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	charged_offense_reason = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Write your reason here", 'rows':"5", 'style':"display:none"}), required=False)
	class Meta:
		model = ApplicationFormChargedOffense
		fields = ('charged_offense', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			charged_offense = selfdata['charged_offense']
		except:
			charged_offense = self.cleaned_data['charged_offense']
		if charged_offense is None:	
			self.add_error('charged_offense', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['charged_offense_reason']
		charged_offense = super(ChargedOffenseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		charged_offense.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		charged_offense.charged_offense_reason = reasons
		charged_offense.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['charged_offense_reason'] = reasons
		value = self.cleaned_data
		ChargedOffense.objects.create(**value)

class TerminationForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	termination = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	termination_reason = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Write your reason here", 'rows':"5", 'style':"display:none"}), required=False)
	class Meta:
		model = ApplicationFormTermination
		fields = ('termination', )

	def clean(self):
		msg = "Please choose either yes or no"
		try:
			termination = selfdata['termination']
		except:
			termination = self.cleaned_data['termination']
		if termination is None:	
			self.add_error('termination', msg)

	def save(self, commit=True):
		reason = self.cleaned_data['termination_reason']
		termination = super(TerminationForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		termination.user = userprofile
		reasons = Reasons.objects.get_or_create(reason=reason)
		if reasons:
			reasons = Reasons.objects.get(reason=reason)
		termination.termination_reason = reasons
		termination.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['termination_reason'] = reasons
		value = self.cleaned_data
		Termination.objects.create(**value)

class PassportForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormPassport
		fields = ('passport', 'passport_expiry')

	def save(self, commit=True):
		passport = super(PassportForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		passport.user = userprofile
		passport.save()
		place_issued = PassportPlaceIssued.objects.get_or_create(place='')
		if place_issued:
			place_issued = PassportPlaceIssued.objects.get(place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['passport_place_issued'] = place_issued
		value = self.cleaned_data
		Passport.objects.create(**value)

class SbookForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormSbook
		fields = ('sbook', 'sbook_expiry')

	def save(self, commit=True):
		sbook = super(SbookForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		sbook.user = userprofile
		sbook.save()
		place_issued = SBookPlaceIssued.objects.get_or_create(place='')
		if place_issued:
			place_issued = SBookPlaceIssued.objects.get(place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['sbook_place_issued'] = place_issued
		value = self.cleaned_data
		Sbook.objects.create(**value)

class COCForm(forms.ModelForm):
	coc_rank = forms.CharField(widget=autocomplete_light.TextWidget('COCRankAutocomplete'))
	class Meta:
		model = ApplicationFormCOC
		fields = ('coc', 'coc_expiry')

	def save(self, commit=True):
		rank = self.cleaned_data['coc_rank']
		coc = super(COCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		coc.user = userprofile
		coc_rank = COCRank.objects.get_or_create(coc_rank=rank)
		if coc_rank:
			coc_rank = COCRank.objects.get(coc_rank=rank)
		coc.coc_rank = coc_rank
		coc.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['coc_rank'] = coc_rank
		self.cleaned_data['coc_date_issued'] = None
		value = self.cleaned_data
		COC.objects.create(**value)

class LicenseForm(forms.ModelForm):
	license_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)
	class Meta:
		model = ApplicationFormLicense
		fields = ('license', )

	def clean(self):
		try:
			license = selfdata['license']
			license_rank = selfdata['license_rank']
		except:
			license = self.cleaned_data['license']
			license_rank = self.cleaned_data['license_rank']
		if license == '' and license_rank != '':
			msg = "Please input license"
			self.add_error('license', msg)
		elif license_rank == '' and license != '':
			msg_rank = "Please choose a rank"
			self.add_error('license_rank', msg_rank)

	def save(self, commit=True):
		rank = self.cleaned_data['license_rank']
		license = super(LicenseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		license.user = userprofile
		license_rank = Rank.objects.get_or_create(rank=rank)
		if license_rank:
			license_rank = Rank.objects.get(rank=rank)
		license.license_rank = license_rank
		license.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['license_rank'] = license_rank
		self.cleaned_data['license_expiry'] = None
		self.cleaned_data['license_date_issued'] = None
		value = self.cleaned_data
		License.objects.create(**value)

class SRCForm(forms.ModelForm):
	src_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'))
	class Meta:
		model = ApplicationFormSRC
		fields = ('src', )

	def save(self, commit=True):
		rank = self.cleaned_data['src_rank']
		src = super(SRCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		src.user = userprofile
		src_rank = Rank.objects.get_or_create(rank=rank)
		if src_rank:
			src_rank = Rank.objects.get(rank=rank)
		src.src_rank = src_rank
		src.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['src_rank'] = src_rank
		self.cleaned_data['src_expiry'] = None
		self.cleaned_data['src_date_issued'] = None
		value = self.cleaned_data
		SRC.objects.create(**value)

class GOCForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormGOC
		fields = ('goc', 'goc_expiry')

	def save(self, commit=True):
		goc = super(GOCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		goc.user = userprofile
		goc.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['goc_date_issued'] = None
		value = self.cleaned_data
		GOC.objects.create(**value)

class USVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	us_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = ApplicationFormUSVisa
		fields = ('us_visa', 'us_visa_expiry')

	def clean(self):
		try:
			value = selfdata['us_visa']
			expiry = selfdata['us_visa_expiry']
		except:
			value = self.cleaned_data['us_visa']
			expiry = self.cleaned_data['us_visa_expiry']
		if value is None:	
			msg = "Please choose either yes or no"
			self.add_error('us_visa', msg)
		elif value == 1 and expiry is None:
			msg_expiry = "Please fill up the date of expiry"
			self.add_error('us_visa_expiry', msg_expiry)

	def save(self, commit=True):
		us_visa = super(USVisaForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		us_visa.user = userprofile
		us_visa.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		USVisa.objects.create(**value)

class SchengenVisaForm(forms.ModelForm):
	CHOICES = (
			('1', 'Yes'),
			('0', 'No'),
		)
	schengen_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	class Meta:
		model = ApplicationFormSchengenVisa
		fields = ('schengen_visa', 'schengen_visa_expiry')

	def clean(self):
		try:
			value = selfdata['schengen_visa']
			expiry = selfdata['schengen_visa_expiry']
		except:
			value = self.cleaned_data['schengen_visa']
			expiry = self.cleaned_data['schengen_visa_expiry']
		if value is None:	
			msg = "Please choose either yes or no"
			self.add_error('schengen_visa', msg)
		elif value == 1 and expiry is None:
			msg_expiry = "Please fill up the date of expiry"
			self.add_error('schengen_visa_expiry', msg_expiry)

	def save(self, commit=True):
		schengen_visa = super(SchengenVisaForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		schengen_visa.user = userprofile
		schengen_visa.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		SchengenVisa.objects.create(**value)

class YellowFeverForm(forms.ModelForm):
	class Meta:
		model = ApplicationFormYellowFever
		fields = ('yellow_fever', 'yellow_fever_expiry')

	def save(self, commit=True):
		yellow_fever = super(YellowFeverForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		yellow_fever.user = userprofile
		yellow_fever.save()
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		YellowFever.objects.create(**value)

class FlagForm(forms.ModelForm):
	flags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=Flags.objects.filter(company_standard=1), required=False)
	class Meta:
		model = ApplicationFormFlagDocuments
		fields = ('flags', )

	def save(self, commit=True):
		flag = super(FlagForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		flag.user = userprofile
		flag.save()
		self.cleaned_data['user'] = userprofile
		# Saving in Mariners Profile script
		value = self.cleaned_data
		# Creating flagdocuments object representing the user object for the FlagDocumentsDetailed model
		flagdocuments = FlagDocuments.objects.get_or_create(user=userprofile)
		if flagdocuments:
			flagdocuments = FlagDocuments.objects.get(user=userprofile)
		# Returning flag key that contains all the flag objects
		flags = value['flags']
		# looping the flag objects to be inserted on the FlagDocumentsDetailed model with the flagdocuments object
		for flag_values in flags:
			x = FlagDocumentsDetailed.objects.get_or_create(flags_documents=flagdocuments, flags=flag_values)

# Will be used for the dyanmic certificates with AJAX
# class DynamicTrainingCertificateForm(forms.ModelForm):
# 	pass

class TrainingCertificateForm(forms.ModelForm):
	trainings_certificates = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=TrainingCertificates.objects.filter(company_standard=1), error_messages={'required': 'Please do not forget to select among the trainings and certificates'})
	class Meta:
		model = ApplicationFormTrainingCertificateDocuments
		fields = ('trainings_certificates', )

	def save(self, commit=True):
		trainings_certificates = super(TrainingCertificateForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		trainings_certificates.user = userprofile
		trainings_certificates.save()
		self.cleaned_data['user'] = userprofile
		# Saving in Mariners Profile script
		value = self.cleaned_data
		# Creating flagdocuments object representing the user object for the FlagDocumentsDetailed model
		trainingcertificatedocuments = TrainingCertificateDocuments.objects.get_or_create(user=userprofile)
		if trainingcertificatedocuments:
			trainingcertificatedocuments = TrainingCertificateDocuments.objects.get(user=userprofile)
		place_trained = TrainingCenter.objects.get_or_create(training_center='')
		if place_trained:
			place_trained = TrainingCenter.objects.get(training_center='')
		trainings_certificates = value['trainings_certificates']
		for trainings_certificates_values in trainings_certificates:
			x = TrainingCertificateDocumentsDetailed.objects.get_or_create(trainings_certificate_documents=trainingcertificatedocuments, trainings_certificates=trainings_certificates_values, place_trained=place_trained)

class SeaServiceForm(forms.ModelForm):
	vessel_name = forms.CharField()
	vessel_type = forms.CharField(widget=autocomplete_light.TextWidget('VesselTypeAutocomplete'))
	flag = forms.CharField(widget=autocomplete_light.TextWidget('FlagsAutocomplete'))
	engine_type = forms.CharField(widget=autocomplete_light.TextWidget('EngineTypeAutocomplete'))
	manning_agency = forms.CharField(widget=autocomplete_light.TextWidget('ManningAgencyAutocomplete'))
	# Do not make principal autocomplete
	principal = forms.CharField()
	rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'))
	class Meta:
		model = ApplicationFormSeaService
		fields = '__all__'
		exclude = ('date_modified', 'vessel_name', 'vessel_type', 'flag', 'engine_type', 'manning_agency', 'principal', 'rank', 'user')



	def save(self, commit=True):
		try:
			vessel_name = self.cleaned_data['vessel_name']
			vessel_type = self.cleaned_data['vessel_type']
			flag = self.cleaned_data['flag']
			engine_type = self.cleaned_data['engine_type']
			manning_agency = self.cleaned_data['manning_agency']
			principal = self.cleaned_data['principal']
			rank = self.cleaned_data['rank']
			sea_services = super(SeaServiceForm, self).save(commit=False)
			userprofile = UserProfile.objects.latest('id')
			vesselname = VesselName.objects.get_or_create(vessel_name=vessel_name)
			if vesselname:
				vesselname = VesselName.objects.get(vessel_name=vessel_name)
			vesseltype = VesselType.objects.get_or_create(vessel_type=vessel_type)
			if vesseltype:
				vesseltype = VesselType.objects.get(vessel_type=vessel_type)
			flags = Flags.objects.get_or_create(flags=flag)
			if flags:
				flags = Flags.objects.get(flags=flag)
			enginetype = EngineType.objects.get_or_create(engine_type=engine_type)
			if enginetype:
				enginetype = EngineType.objects.get(engine_type=engine_type)
			manningagency = ManningAgency.objects.get_or_create(manning_agency=manning_agency)
			if manningagency:
				manningagency = ManningAgency.objects.get(manning_agency=manning_agency)
			principals = Principal.objects.get_or_create(principal=principal)
			if principals:
				principals = Principal.objects.get(principal=principal)
			ranks = Rank.objects.get_or_create(rank=rank)
			if ranks:
				ranks = Rank.objects.get(rank=rank)
			sea_services.user = userprofile
			sea_services.vessel_name = vesselname
			sea_services.vessel_type = vesseltype
			sea_services.flag = flags
			sea_services.engine_type = enginetype
			sea_services.principal = principals
			sea_services.manning_agency = manningagency
			sea_services.rank = ranks
			sea_services.save()
			self.cleaned_data['user'] = userprofile
			self.cleaned_data['vessel_name'] = vesselname
			self.cleaned_data['vessel_type'] = vesseltype
			self.cleaned_data['flag'] = flags
			self.cleaned_data['engine_type'] = enginetype
			self.cleaned_data['manning_agency'] = manningagency
			self.cleaned_data['principal'] = principals
			self.cleaned_data['rank'] = ranks
			value = self.cleaned_data
			SeaService.objects.create(**value)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

class ApplicationForm(autocomplete_light.ModelForm):
	# pass
	# Date today script
	ADVERTISEMENT_CHOICES = (
			('SEAWAY', 'SEAWAY'),
			('BUHAY MARINO', 'BUHAY MARINO'),
			('HARBOR SCOPE', 'HARBOR SCOPE'),
			('NEWSPAPER', 'NEWSPAPER'),
		)
	INTERNET_CHOICES = (
			('www.manship.com', 'www.manship.com'),
			('www.seamanjobsite.com', 'www.seamanjobsite.com'),
			('www.pinoyseaman.com', 'www.pinoyseaman.com'),
			('www.crewtoo.com', 'www.crewtoo.com'),
		)
	# application_date = forms.DateField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Date of Application", 'data-toggle':'tooltip', 'readonly':'readonly', 'value':today}))
	signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000'}))
	alternative_position = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	position_applied = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	source = forms.ModelChoiceField(widget=forms.RadioSelect, error_messages={'required': 'Please let us know how you learned our company'}, queryset=Sources.objects.filter(~Q(source="Friends or Relatives")))
	advertisements = forms.ChoiceField(widget=forms.Select(attrs={'class':"specific"}), choices=ADVERTISEMENT_CHOICES, required=False)
	internet = forms.ChoiceField(widget=forms.Select(attrs={'class':"specific", 'required':'required'}), choices=INTERNET_CHOICES, required=False)
	referred_by = forms.CharField(widget=autocomplete_light.TextWidget('ReferrerAutocomplete', attrs={'placeholder':'Search Referrer', 'class':"specific"}) , required=False)
	application_picture = forms.CharField()
	scheme = forms.CharField()
	http_host = forms.CharField()
	essay = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control essay"}), required=False)
	class Meta:
		model = ApplicationForm
		fields = ('application_date', 'alternative_position', 'position_applied')

	def save(self, commit=True):
		advertisements = self.cleaned_data['advertisements']
		internet = self.cleaned_data['internet']
		referred_by = self.cleaned_data['referred_by']
		essay = self.cleaned_data['essay']
		application_picture = self.cleaned_data['application_picture']
		scheme = self.cleaned_data['scheme']
		http_host = self.cleaned_data['http_host']
		# Sources Validation
		if advertisements:
			self.cleaned_data['specific'] = advertisements
			self.cleaned_data.pop("advertisements")
		elif internet:
			self.cleaned_data['specific'] = internet
			self.cleaned_data.pop("internet")
		# Reffered By and (Friends or Relatives) validation
		# If not in the referrers Pool it will be considerer as a friend or relative
		elif referred_by:
			try:
				referred_by = ReferrersPool.objects.get(name=referred_by)
			except:
				self.cleaned_data['source'] = Sources.objects.get(source='Friends or Relatives')
			self.cleaned_data['specific'] = referred_by
			self.cleaned_data.pop("referred_by")
		else:
			self.cleaned_data['specific'] = ''

		signature = self.cleaned_data['signature']
		source = self.cleaned_data['source']
		specific = self.cleaned_data['specific']
		position_applied = self.cleaned_data['position_applied']
		userprofile = UserProfile.objects.latest('id')
		first_name = userprofile.first_name
		middle_name = userprofile.middle_name
		last_name = userprofile.last_name
		file_name = first_name+middle_name+last_name
		file_name = "".join(file_name.split())
		
		application = super(ApplicationForm, self).save(commit=False)
		specifics = Specifics.objects.get_or_create(specific=specific)
		if specifics:
			specifics = Specifics.objects.get(specific=specific)

		# Signature script on saving in a folder
		signature_path = "media/signature/application-form/"+file_name+".png"
		if signature:
			signature_picture = draw_signature(signature)
			_signature_file_path = draw_signature(signature, as_file=True)
			signature_file_path = settings.MEDIA_ROOT+"/signatures/application-form/"
			shutil.move(_signature_file_path, signature_file_path)
			_signature_file_path = _signature_file_path.replace('/tmp/', 'signatures/application-form/')

		essays = Essay.objects.get_or_create(essay=essay)
		if essays:
			essays = Essay.objects.get(essay=essay)

		
		# Webcam script on saving in a folder
		try:
			tmp_application_picture = application_picture
			tmp_application_picture = tmp_application_picture.replace(scheme+"://"+http_host+"/media", "")
			tmp_application_picture = settings.MEDIA_ROOT+tmp_application_picture
			path_application_picture = "media/photos/application-form/"+file_name+".jpg"
			# settings.MEDIA_ROOT is declared so it is flexible even in cloud
			application_picture = settings.MEDIA_ROOT+"/photos/application-form/"+file_name+".jpg"
			shutil.move(tmp_application_picture, application_picture)
			application_picture = path_application_picture.replace("media/", "")
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

		appsource = AppSource.objects.get_or_create(source=source, specific=specifics)
		if appsource:
			appsource = AppSource.objects.get(source=source, specific=specifics)
		application.user = userprofile
		application.application_source = appsource
		application.picture = application_picture
		application.essay = essays
		application.signature = _signature_file_path
		application.save()
		try:
			referrer = ReferrersPool.objects.get(name=referred_by)
		except:
			referrer = ReferrersPool.objects.get_or_create(name='')
			referrer =ReferrersPool.objects.get(name='')
		self.cleaned_data['signature'] = _signature_file_path
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['picture'] = application_picture
		self.cleaned_data['position'] = position_applied
		self.cleaned_data['referrer'] = referrer
		self.cleaned_data.pop("essay")
		self.cleaned_data.pop("position_applied")
		self.cleaned_data.pop("application_picture")
		self.cleaned_data.pop("source")
		self.cleaned_data.pop("http_host")
		self.cleaned_data.pop("alternative_position")
		self.cleaned_data.pop("scheme")
		self.cleaned_data.pop("application_date")
		try:
			self.cleaned_data.pop("advertisements")
		except:
			pass
		try:
			self.cleaned_data.pop("specific")
		except:
			pass
		try:
			self.cleaned_data.pop("referred_by")
		except:
			pass
		try:
			self.cleaned_data.pop("internet")
		except:
			pass
		value = self.cleaned_data
		MarinersProfile.objects.create(**value)

class StatusForm(forms.Form):
	status = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalRadioRenderer), queryset=Status.objects.filter(), required=False)