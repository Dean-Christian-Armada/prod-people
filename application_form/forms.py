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
		user = User.objects.get(username__iexact='applicant')
		userlevel = Userlevel.objects.get(userlevel__iexact='applicant')
		userprofile.user = user
		userprofile.userlevel = userlevel
		userprofile.save()
		return userprofile

class PermanentAddressForm(forms.ModelForm):
	permanent_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	permanent_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	permanent_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))
	
	class Meta:
		model = ApplicationFormPermanentAddress
		fields = ('permanent_unit', 'permanent_street')

	def save(self, commit=True):
		permanent_zip = self.cleaned_data['permanent_zip']
		permanent_barangay = self.cleaned_data['permanent_barangay']
		permanent_municipality = self.cleaned_data['permanent_municipality']

		permanent_address = super(PermanentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create({'municipality':permanent_municipality}, municipality__iexact=permanent_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality__iexact=permanent_municipality)
		barangay = Barangay.objects.get_or_create({'barangay':permanent_barangay}, barangay__iexact=permanent_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay__iexact=permanent_barangay)
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
	current_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	current_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	current_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))
	
	class Meta:
		model = ApplicationFormCurrentAddress
		fields = ('current_unit', 'current_street')

	def save(self, commit=True):
		current_zip = self.cleaned_data['current_zip']
		current_barangay = self.cleaned_data['current_barangay']
		current_municipality = self.cleaned_data['current_municipality']

		current_address = super(CurrentAddressForm, self).save(commit=False)
		municipality = Municipality.objects.get_or_create({'municipality':current_municipality}, municipality__iexact=current_municipality)
		if municipality:
			municipality = Municipality.objects.get(municipality__iexact=current_municipality)
		barangay = Barangay.objects.get_or_create({'barangay':current_barangay}, barangay__iexact=current_barangay)
		if barangay:
			barangay = Barangay.objects.get(barangay__iexact=current_barangay)
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
	preferred_vessel_type = forms.CharField(widget=autocomplete_light.TextWidget('PreferredVesselTypeAutocomplete'))
	# regex field for mobile numbersNumberInput 
	mobile_1 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"})
	mobile_2 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"}, required=False)
	mobile_3 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"}, required=False)
	# regex fild for landline numbers
	landline_1 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	landline_2 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{7})$', error_messages={'invalid': "Please input proper 7 digit telephone number format"}, required=False)
	# regex fild for sss
	sss = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input proper 10 digit format of sss"})
	# regex field for philhealth
	philhealth = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of philhealth"}, required=False)
	# regex fild for tin
	tin = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of tin"}, required=False)
	# regex fild for pagibig
	pagibig = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{12})$', error_messages={'invalid': "Please input proper 12 digit format of pagibig"}, required=False)
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
		birth_place = BirthPlace.objects.get_or_create({'birth_place':birthplace}, birth_place__iexact=birthplace)
		if birth_place:
			birth_place = BirthPlace.objects.get(birth_place__iexact=birthplace)
		preferred_vessel_type = VesselType.objects.get_or_create({'vessel_type':vessel_type}, vessel_type__iexact=vessel_type)
		if preferred_vessel_type:
			preferred_vessel_type = VesselType.objects.get(vessel_type__iexact=vessel_type)
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
		# self.cleaned_data.pop("emergency_municipality")
		self.cleaned_data.pop("age")
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
			colleges = Colleges.objects.get_or_create({'college_name':college_name}, college_name__iexact=college_name)
			if colleges:
				colleges = Colleges.objects.get(college_name__iexact=college_name)
			degree = Degree.objects.get_or_create({'degree':degree_obtained}, degree__iexact=degree_obtained)
			if degree:
				degree = Degree.objects.get(degree__iexact=degree_obtained)
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
		highschools = HighSchools.objects.get_or_create({'highschool_name':highschool_name}, highschool_name__iexact=highschool_name)
		if highschools:
			highschools = HighSchools.objects.get(highschool_name__iexact=highschool_name)
		highschool.user = userprofile
		highschool.highschool = highschools
		highschool.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['highschool'] = highschools
		value = self.cleaned_data
		HighSchool.objects.create(**value)

class EmergencyContactForm(forms.ModelForm):
	relationship = forms.CharField(widget=autocomplete_light.TextWidget('RelationshipAutocomplete'))
	emergency_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	emergency_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))
	emergency_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	emergency_contact = forms.RegexField(widget=forms.NumberInput(), regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"})
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
			municipality = Municipality.objects.get_or_create({'municipality':emergency_municipality}, municipality__iexact=emergency_municipality)
			if municipality:
				municipality = Municipality.objects.get(municipality__iexact=emergency_municipality)
			barangay = Barangay.objects.get_or_create({'barangay':emergency_barangay}, barangay__iexact=emergency_barangay)
			if barangay:
				barangay = Barangay.objects.get(barangay__iexact=emergency_barangay)
			relationships = Relationship.objects.get_or_create({'relationship':relationship}, relationship__iexact=relationship)
			if relationships:
				relationships = Relationship.objects.get(relationship__iexact=relationship)
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
		place_issued = PassportPlaceIssued.objects.get_or_create(passport_place='')
		if place_issued:
			place_issued = PassportPlaceIssued.objects.get(passport_place='')
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
		place_issued = SBookPlaceIssued.objects.get_or_create(sbook_place='')
		if place_issued:
			place_issued = SBookPlaceIssued.objects.get(sbook_place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['sbook_place_issued'] = place_issued
		value = self.cleaned_data
		Sbook.objects.create(**value)

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
		src_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if src_rank:
			src_rank = Rank.objects.get(rank__iexact=rank)
		src.src_rank = src_rank
		src.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['src_rank'] = src_rank
		# self.cleaned_data['src_expiry'] = None
		# self.cleaned_data['src_date_issued'] = None
		value = self.cleaned_data
		SRC.objects.create(**value)

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
		place_issued = USVisaPlaceIssued.objects.get_or_create(us_visa_place='')
		if place_issued:
			place_issued = USVisaPlaceIssued.objects.get(us_visa_place='')
		self.cleaned_data['us_visa_place_issued'] = place_issued
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
		place_issued = SchengenVisaPlaceIssued.objects.get_or_create(schengen_visa_place='')
		if place_issued:
			place_issued = SchengenVisaPlaceIssued.objects.get(schengen_visa_place='')
		self.cleaned_data['schengen_visa_place_issued'] = place_issued
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
		place_issued = YellowFeverPlaceIssued.objects.get_or_create(yellow_fever_place='')
		if place_issued:
			place_issued = YellowFeverPlaceIssued.objects.get(yellow_fever_place='')
		self.cleaned_data['yellow_fever_place_issued'] = place_issued
		self.cleaned_data['user'] = userprofile
		value = self.cleaned_data
		YellowFever.objects.create(**value)

class FlagForm(forms.ModelForm):
	flags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=Flags.objects.filter(manship_standard=1), required=False)
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
			x = FlagDocumentsDetailed.objects.get_or_create(flags_documents=flagdocuments, flags=flag_values, flags_boolean=True)

# used for the dyanmic certificates with AJAX in the application form
class DynamicTrainingCertificateForm(forms.Form):
	def __init__(self, rank_id, national_certificate=True, *args, **kwargs):
		super(DynamicTrainingCertificateForm, self).__init__(*args, **kwargs)
		try:
			rank = Rank.objects.get(id=rank_id)
			queryset = TrainingCertificates.objects.filter(departments=rank.department).filter(company_standard=1)
			if national_certificate == False:
				queryset = queryset.filter(national_certificate=False)
			self.fields['trainings_certificates'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalCheckboxRenderer), queryset=queryset.order_by('id'), error_messages={'required': 'Please do not forget to select among the trainings and certificates'})
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

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
			x = TrainingCertificateDocumentsDetailed.objects.get_or_create(trainings_certificate_documents=trainingcertificatedocuments, trainings_certificates=trainings_certificates_values, place_trained=place_trained, trainings_certificates_boolean=True)

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
			vesselname = VesselName.objects.get_or_create({'vessel_name':vessel_name}, vessel_name__iexact=vessel_name)
			if vesselname:
				vesselname = VesselName.objects.get(vessel_name__iexact=vessel_name)
			vesseltype = VesselType.objects.get_or_create({'vessel_type':vessel_type}, vessel_type__iexact=vessel_type)
			if vesseltype:
				vesseltype = VesselType.objects.get(vessel_type__iexact=vessel_type)
			flags = Flags.objects.get_or_create({'flags':flag}, flags__iexact=flag)
			if flags:
				flags = Flags.objects.get(flags__iexact=flag)
			enginetype = EngineType.objects.get_or_create({'engine_type':engine_type}, engine_type__iexact=engine_type)
			if enginetype:
				enginetype = EngineType.objects.get(engine_type__iexact=engine_type)
			manningagency = ManningAgency.objects.get_or_create({'manning_agency':manning_agency}, manning_agency__iexact=manning_agency)
			if manningagency:
				manningagency = ManningAgency.objects.get(manning_agency__iexact=manning_agency)
			principals = Principal.objects.get_or_create({'principal':principal}, principal__iexact=principal)
			if principals:
				principals = Principal.objects.get(principal__iexact=principal)
			ranks = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
			if ranks:
				ranks = Rank.objects.get(rank__iexact=rank)
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
	essay = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control essay"}))
	class Meta:
		model = ApplicationForm
		fields = ('application_date', 'alternative_position', 'position_applied')

	def clean(self):

		try:
			position_applied = self.cleaned_data['position_applied']
			alternative_position = self.cleaned_data['alternative_position']
		except:
			pass
		try:
			# Script to let cadets only take the essay
			# position_applied = Rank.objects.get(rank=position_applied)
			# alternative_position = Rank.objects.get(rank=alternative_position)
			# if "Cadet".lower() in position_applied.rank.lower() or "Cadet".lower() in alternative_position.rank.lower():
			msg = "The Essay must be at least 50 words"
			try:
				essay = selfdata['essay']
			except:
				essay = self.cleaned_data['essay']
			words = ''.join(c if c.isalnum() else ' ' for c in essay).split()
			if len(words) < 50:
				self.add_error('essay', msg)
		except:
			pass

		# script to make sure that the referrer's are filled up if selected
		try:
			referred_by = self.cleaned_data['referred_by']
			source = self.cleaned_data['source']
			if referred_by == '' and source == 'Referred By':
				msg = "Please pick your referrer"
				self.add_error('referred_by', msg)
		except:
			pass

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
				referred_by = ReferrersPool.objects.get(name__iexact=referred_by)
			except:
				self.cleaned_data['source'] = Sources.objects.get(source__iexact='Friends or Relatives')
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
		specifics = Specifics.objects.get_or_create({'specific':specific}, specific__iexact=specific)
		if specifics:
			specifics = Specifics.objects.get(specific__iexact=specific)

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
			referrer = ReferrersPool.objects.get(name__iexact=referred_by)
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

class LicenseForm(forms.ModelForm):
	license_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)
	alternative_position = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	position_applied = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))

	class Meta:
		model = ApplicationFormLicense
		fields = ('license', )

	# script to make sure that the applicants except the cadets are required to fill the license
	def clean(self):
		license = self.cleaned_data['license']
		license_rank = self.cleaned_data['license_rank']
		try:
			position_applied = self.cleaned_data['position_applied']
			alternative_position = self.cleaned_data['alternative_position']
		except:
			pass

		try:
			position_applied = Rank.objects.get(rank=position_applied)
			alternative_position = Rank.objects.get(rank=alternative_position)

			if "Cadet".lower() not in position_applied.rank.lower() or "Cadet".lower() not in alternative_position.rank.lower():
				msg = "This field is required"
				if license == '':
					self.add_error('license', msg)
				if license_rank == '':
					self.add_error('license_rank', msg)
		except:
			pass

	def save(self, commit=True):
		rank = self.cleaned_data['license_rank']
		license = super(LicenseForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		license.user = userprofile
		license_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if license_rank:
			license_rank = Rank.objects.get(rank__iexact=rank)
		license.license_rank = license_rank
		license.save()
		place_issued = LicensePlaceIssued.objects.get_or_create(license_place='')
		if place_issued:
			place_issued = LicensePlaceIssued.objects.get(license_place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['license_rank'] = license_rank
		# self.cleaned_data['license_expiry'] = None
		# self.cleaned_data['license_date_issued'] = None
		self.cleaned_data['license_place_issued'] = place_issued
		value = self.cleaned_data
		self.cleaned_data.pop("position_applied")
		self.cleaned_data.pop("alternative_position")
		License.objects.create(**value)

class COCForm(forms.ModelForm):
	coc_rank = forms.CharField(widget=autocomplete_light.TextWidget('COCRankAutocomplete'), required=False)
	alternative_position = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	position_applied = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))

	class Meta:
		model = ApplicationFormCOC
		fields = ('coc', 'coc_expiry')

	# script to make sure that the applicants except the cadets are required to fill the coc
	def clean(self):
		coc = self.cleaned_data['coc']
		coc_rank = self.cleaned_data['coc_rank']
		coc_expiry = self.cleaned_data['coc_expiry']
		try:
			position_applied = self.cleaned_data['position_applied']
			alternative_position = self.cleaned_data['alternative_position']
		except:
			pass

		try:
			position_applied = Rank.objects.get(rank=position_applied)
			alternative_position = Rank.objects.get(rank=alternative_position)

			if "Cadet".lower() not in position_applied.rank.lower() or "Cadet".lower() not in alternative_position.rank.lower():
				msg = "This field is required"
				if coc == '':
					self.add_error('coc', msg)
				if coc_rank == '':
					self.add_error('coc_rank', msg)
				if coc_expiry == None:
					self.add_error('coc_expiry', msg)
		except:
			pass

	def save(self, commit=True):
		rank = self.cleaned_data['coc_rank']
		coc = super(COCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		coc.user = userprofile
		coc_rank = COCRank.objects.get_or_create({'coc_rank':rank}, coc_rank__iexact=rank)
		if coc_rank:
			coc_rank = COCRank.objects.get(coc_rank__iexact=rank)
		coc.coc_rank = coc_rank
		coc.save()
		place_issued = COCPlaceIssued.objects.get_or_create(coc_place='')
		if place_issued:
			place_issued = COCPlaceIssued.objects.get(coc_place='')
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['coc_rank'] = coc_rank
		# self.cleaned_data['coc_date_issued'] = None
		self.cleaned_data['coc_place_issued'] = place_issued
		value = self.cleaned_data
		self.cleaned_data.pop("position_applied")
		self.cleaned_data.pop("alternative_position")
		COC.objects.create(**value)

class GOCForm(forms.ModelForm):
	alternative_position = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	position_applied = forms.ModelChoiceField(widget=forms.Select, queryset=Rank.objects.filter(hiring=1).order_by('order'))
	class Meta:
		model = ApplicationFormGOC
		fields = ('goc', 'goc_expiry')

	# script to make sure that the applicants except the cadets are required to fill the goc
	def clean(self):
		goc = self.cleaned_data['goc']
		goc_expiry = self.cleaned_data['goc_expiry']
		try:
			position_applied = self.cleaned_data['position_applied']
			alternative_position = self.cleaned_data['alternative_position']
		except:
			pass

		try:
			position_applied = Rank.objects.get(rank=position_applied)
			alternative_position = Rank.objects.get(rank=alternative_position)

			if "Cadet".lower() not in position_applied.rank.lower() or "Cadet".lower() not in alternative_position.rank.lower():
				msg = "This field is required"
				if goc == '':
					self.add_error('goc', msg)
				if goc_expiry == None:
					self.add_error('goc_expiry', msg)
		except:
			pass

	def save(self, commit=True):
		goc = super(GOCForm, self).save(commit=False)
		userprofile = UserProfile.objects.latest('id')
		goc.user = userprofile
		goc.save()
		self.cleaned_data['user'] = userprofile
		self.cleaned_data['goc_date_issued'] = None
		value = self.cleaned_data
		self.cleaned_data.pop("position_applied")
		self.cleaned_data.pop("alternative_position")
		GOC.objects.create(**value)

class StatusForm(forms.Form):
	status = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(renderer=HorizontalRadioRenderer), queryset=Status.objects.filter(), required=False)

# Used for Ionic Application Form template
class ApplicationReceivedForm(forms.Form):
	try:
		received_by = Userlevel.objects.get(userlevel='fleet2')
		received_by = forms.ModelChoiceField(widget=forms.Select, queryset=UserProfile.objects.filter(userlevel=received_by))
	except:
		pass