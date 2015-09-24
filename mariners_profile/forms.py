from django.db.models.signals import post_save
from django import forms

import autocomplete_light

from application_form.forms import *

from mariners_profile.models import *

class MarinersDataTables(autocomplete_light.ModelForm):
	search = forms.CharField(widget=autocomplete_light.TextWidget('MarinersAutocomplete', attrs={'placeholder':'Search Mariners', 'class':'form-control search-input', 'name': 'search' }))

	class Meta:
		model = MarinersProfile
		fields = ('search', )

class ApplicantNameForm(ApplicantNameForm):
	pass


class PermanentAddressForm(forms.ModelForm):
	permanent_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	permanent_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	permanent_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))
	
	class Meta:
		model = PermanentAddress
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

class PersonalDataForm(forms.ModelForm):
	birth_place = forms.CharField()
	class Meta:
		model = PersonalData
		fields = '__all__'
		exclude = ('name', 'birth_place','permanent_address', 'current_address')

	def save(self, commit=True):
		birthplace = self.cleaned_data['birth_place']
		permanent_address = ApplicationFormPermanentAddress.objects.latest('id')
		current_address = ApplicationFormCurrentAddress.objects.latest('id')
		personal_data = super(PersonalDataForm, self).save(commit=False)
		birth_place = BirthPlace.objects.get_or_create({'birth_place':birthplace}, birth_place__iexact=birthplace)
		if birth_place:
			birth_place = BirthPlace.objects.get(birth_place__iexact=birthplace)
		personal_data.birth_place = birth_place
		personal_data.permanent_address = permanent_address
		personal_data.current_address = current_address
		personal_data.save()

class SpouseForm(forms.ModelForm):
	spouse_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"}, required=False)
	class Meta:
		model = Spouse
		fields = '__all__'

	def save(self, commit=True):
		print self.cleaned_data
		spouse = super(SpouseForm, self).save(commit=False)
		spouse.save()

class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = '__all__'

class HighSchoolForm(forms.ModelForm):
	highschool = forms.CharField()
	class Meta:
		model = HighSchool
		fields = '__all__'
		exclude = ('highschool', )

	def save(self, commit=True):
		highschool_name = self.cleaned_data['highschool']
		highschool = super(HighSchoolForm, self).save(commit=False)
		highschools = HighSchools.objects.get_or_create({'highschool_name':highschool_name}, highschool_name__iexact=highschool_name)
		if highschools:
			highschools = HighSchools.objects.get(highschool_name__iexact=highschool_name)
		highschool.highschool = highschools
		highschool.save()

class VocationalForm(forms.ModelForm):
	vocational = forms.CharField(required=False)
	class Meta:
		model = Vocational
		fields = '__all__'
		exclude = ('vocational', )

	def save(self, commit=True):
		vocational_name = self.cleaned_data['vocational']
		vocational = super(VocationalForm, self).save(commit=False)
		vocationals = Vocationals.objects.get_or_create({'vocational_name':vocational_name}, vocational_name__iexact=vocational_name)
		if vocationals:
			vocationals = Vocationals.objects.get(vocational_name__iexact=vocational_name)
		vocational.vocational = vocationals
		vocational.save()

class PrimarySchoolForm(forms.ModelForm):
	primaryschool = forms.CharField(required=False)
	class Meta:
		model = PrimarySchool
		fields = '__all__'
		exclude = ('primaryschool', )

	def save(self, commit=True):
		primaryschool_name = self.cleaned_data['primaryschool']
		primaryschool = super(PrimarySchoolForm, self).save(commit=False)
		primaryschools = PrimarySchools.objects.get_or_create({'primaryschool_name':primaryschool_name}, primaryschool_name__iexact=primaryschool_name)
		if primaryschools:
			primaryschools = PrimarySchools.objects.get(primaryschool_name__iexact=primaryschool_name)
		primaryschool.primaryschool = primaryschools
		primaryschool.save()

class ReferenceForm(forms.ModelForm):
	class Meta:
		model = Reference
		exclude = '__all__'