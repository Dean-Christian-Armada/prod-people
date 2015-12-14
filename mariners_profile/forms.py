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

class MarinersChangePosition(forms.ModelForm):
	class Meta:
		model = MarinersProfile
		fields = ('position', )

	def __init__(self, rank_id, *args, **kwargs):
		super(MarinersChangePosition, self).__init__(*args, **kwargs)
		try:
			rank = Rank.objects.get(id=rank_id)
			queryset = Rank.objects.filter(department=rank.department)
			self.fields['position'] = forms.ModelChoiceField(queryset)
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

class MarinersChangePicture(forms.ModelForm):
	class Meta:
		model = MarinersProfile
		fields = ('picture', 'picture_last_modified')

class ApplicantNameForm(ApplicantNameForm):
	class Meta:
		model = UserProfile
		fields = ('last_name', 'first_name', 'middle_name', 'code')

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
	birth_place = forms.CharField(required=False)
	dialect = forms.CharField(widget=autocomplete_light.TextWidget('DialectAutocomplete', attrs={'placeholder': ''}), required=False)
	mobile_1 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"})
	mobile_2 = forms.RegexField(widget=forms.NumberInput(attrs={'min':0}), initial=None, regex=r'^([0-9]{10})$', error_messages={'invalid': "Please input right mobile format. Example: 9171234567"}, required=False)
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
	age = forms.IntegerField(required=False)
	class Meta:
		model = PersonalData
		fields = '__all__'
		exclude = ('name', 'birth_place','permanent_address', 'current_address', 'dialect', 'availability_date',  'father_last_name', 'father_first_name', 'father_middle_name', 'mother_last_name', 'civil_status', 'mother_first_name', 'nationality', 'mother_middle_name')

	def save(self, commit=True):
		print (self.cleaned_data)
		birthplace = self.cleaned_data['birth_place']
		dialects = self.cleaned_data['dialect']
		# permanent_address = ApplicationFormPermanentAddress.objects.latest('id')
		# current_address = ApplicationFormCurrentAddress.objects.latest('id')
		personal_data = super(PersonalDataForm, self).save(commit=False)
		birth_place = BirthPlace.objects.get_or_create({'birth_place':birthplace}, birth_place__iexact=birthplace)
		if birth_place:
			birth_place = BirthPlace.objects.get(birth_place__iexact=birthplace)
		dialect = Dialect.objects.get_or_create({'dialect':dialects}, dialect__iexact=dialects)
		if dialect:
			dialect = Dialect.objects.get(dialect__iexact=dialects)
		personal_data.birth_place = birth_place
		personal_data.dialect = dialect
		personal_data.save()

class PersonalDataCivilStatusForm(forms.ModelForm):
	class Meta:
		model = PersonalData
		fields = ('civil_status', )

class PersonalDataFatherForm(forms.ModelForm):
	class Meta:
		model = PersonalData
		fields = ('father_last_name', 'father_first_name', 'father_middle_name', )

class PersonalDataMotherForm(forms.ModelForm):
	class Meta:
		model = PersonalData
		fields = ('mother_last_name', 'mother_first_name', 'mother_middle_name', )

class SpouseForm(PersonalDataCivilStatusForm):
	# spouse_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"}, required=False)
	class Meta:
		model = Spouse
		fields = '__all__'

class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = '__all__'

	def save(self, commit=True):
		# Script to solve the blank fields
		college = super(CollegeForm, self).save(commit=False)
		college
		try:
			college.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

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
		try:
			primaryschool_name = self.cleaned_data['primaryschool']
			primaryschool = super(PrimarySchoolForm, self).save(commit=False)
			primaryschools = PrimarySchools.objects.get_or_create({'primaryschool_name':primaryschool_name}, primaryschool_name__iexact=primaryschool_name)
			if primaryschools:
				primaryschools = PrimarySchools.objects.get(primaryschool_name__iexact=primaryschool_name)
			primaryschool.primaryschool = primaryschools
			primaryschool.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class ReferenceForm(forms.ModelForm):
	company = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Company"}), required=False)
	person_contacted = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Person Contacted"}), required=False)
	# Try is used in case the database was deleted
	try:
		verified_by = Userlevel.objects.get(userlevel='crewing')
		verified_by = forms.ModelChoiceField(widget=forms.Select, queryset=UserProfile.objects.filter(userlevel=verified_by))
	except:
		pass
	class Meta:
		model = Reference
		fields = '__all__'

	def clean(self):
		company = self.cleaned_data['company']
		_company = Company.objects.get_or_create({'company':company}, company__iexact=company)
		if _company:
			_company = Company.objects.get(company__iexact=company)
		self.cleaned_data['company'] = _company

		person_contacted = self.cleaned_data['person_contacted']
		_person_contacted = PersonReference.objects.get_or_create({'person_reference':person_contacted}, person_reference__iexact=person_contacted)
		if _person_contacted:
			_person_contacted = PersonReference.objects.get(person_reference__iexact=person_contacted)
		self.cleaned_data['person_contacted'] = _person_contacted

		
	def save(self, commit=True):
		try:
			company = self.cleaned_data['company']
			person_contacted = self.cleaned_data['person_contacted']
			reference = super(ReferenceForm, self).save(commit=False)

			reference.company = company
			reference.person_contacted = person_contacted
			reference.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class LandEmploymentForm(forms.ModelForm):
	land_position = forms.CharField(widget=autocomplete_light.TextWidget('LandPositionAutocomplete'), required=False)
	employer_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}), required=False)
	employer_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'), required=False)
	employer_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'), required=False)
	# spouse_contact = forms.RegexField(regex=r'^([0-9]{7}|[0-9]{11})$', error_messages={'invalid': "Telephone(xx-xxx-xx) and Mobile Numbers(09xx-xxxx-xxx) are only allowed"}, required=False)

	class Meta:
		model = Reference
		fields = '__all__'

	def clean(self):
		try:
			land_position = self.cleaned_data['land_position']
			_land_position = LandPosition.objects.get_or_create({'land_position':land_position}, land_position__iexact=land_position)
			if _land_position:
				_land_position = LandPosition.objects.get(land_position__iexact=land_position)
			self.cleaned_data['land_position'] = _land_position

			zip = self.cleaned_data['employer_zip']
			_zip = Zip.objects.get_or_create({'zip':zip}, zip__iexact=zip)
			if _zip:
				_zip = Zip.objects.get(zip__iexact=zip)
			self.cleaned_data['employer_zip'] = _zip

			barangay = self.cleaned_data['employer_barangay']
			_barangay = Barangay.objects.get_or_create({'barangay':barangay}, barangay__iexact=barangay)
			if _barangay:
				_barangay = Barangay.objects.get(barangay__iexact=barangay)
			self.cleaned_data['employer_barangay'] = _barangay

			municipality = self.cleaned_data['employer_municipality']
			_municipality = Municipality.objects.get_or_create({'municipality':municipality}, municipality__iexact=municipality)
			if _municipality:
				_municipality = Municipality.objects.get(municipality__iexact=municipality)
			self.cleaned_data['employer_municipality'] = _municipality
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

	def save(self, commit=True):
		try:
			land_position = self.cleaned_data['land_position']
			employer_zip = str(self.cleaned_data['employer_zip'])
			employer_barangay = self.cleaned_data['employer_barangay']
			employer_municipality = self.cleaned_data['employer_municipality']
			land_employment = super(LandEmploymentForm, self).save(commit=False)

			municipality = Municipality.objects.get_or_create({'municipality':employer_municipality}, municipality__iexact=employer_municipality)
			if municipality:
				municipality = Municipality.objects.get(municipality__iexact=employer_municipality)
			barangay = Barangay.objects.get_or_create({'barangay':employer_barangay}, barangay__iexact=employer_barangay)
			if barangay:
				barangay = Barangay.objects.get(barangay__iexact=employer_barangay)
			try:
				zip = Zip.objects.get_or_create(zip=employer_zip, barangay=barangay, municipality=municipality)[0]	
			except:
				zip = Zip.objects.get(zip=employer_zip)

			print ("armada")
			land_employment.employer_zip = zip
			land_employment.land_position = land_position

			land_employment.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class BeneficiaryForm(forms.ModelForm):
	class Meta:
		model = Beneficiary
		fields = '__all__'

	# def clean(self):
	# 	relationship = self.cleaned_data['beneficiary_relationship']
	# 	_relationship = Relationship.objects.get_or_create({'relationship':relationship}, relationship__iexact=relationship)
	# 	if _relationship:
	# 		_relationship = Relationship.objects.get(relationship__iexact=relationship)
	# 	self.cleaned_data['beneficiary_relationship'] = _relationship

		
	def save(self, commit=True):
		try:
			# relationship = self.cleaned_data['relationship']
			beneficiary = super(BeneficiaryForm, self).save(commit=False)

			# beneficiary.beneficiary_relationship = relationship
			beneficiary.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class AlloteeForm(forms.ModelForm):
	allotee_zip = forms.IntegerField(widget=forms.TextInput(attrs={'min':0}), required=False)
	allotee_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'), required=False)
	allotee_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'), required=False)

	class Meta:
		model = Reference
		fields = '__all__'

	def clean(self):

		print (self.cleaned_data)
		barangay = self.cleaned_data['allotee_barangay']
		_barangay = Barangay.objects.get_or_create({'barangay':barangay}, barangay__iexact=barangay)
		if _barangay:
			_barangay = Barangay.objects.get(barangay__iexact=barangay)

		municipality = self.cleaned_data['allotee_municipality']
		_municipality = Municipality.objects.get_or_create({'municipality':municipality}, municipality__iexact=municipality)
		if _municipality:
			_municipality = Municipality.objects.get(municipality__iexact=municipality)
		
		print ("--------------")
		zip = self.cleaned_data['allotee_zip']
		try:
			_zip = Zip.objects.get_or_create(zip=zip, barangay=_barangay, municipality=_municipality)[0]
		except:
			_zip = Zip.objects.get(zip=zip)
		self.cleaned_data['allotee_zip'] = _zip
		print (self.cleaned_data['allotee_zip'])

		
	def save(self, commit=True):
		try:
			# relationship = self.cleaned_data['allotee_relationship']
			# bank = self.cleaned_data['bank']
			allotee_zip = str(self.cleaned_data['allotee_zip'])
			allotee = super(AlloteeForm, self).save(commit=False)

			# allotee.allotee_relationship = relationship
			# allotee.bank = bank
			allotee.zip = zip
			allotee.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class EmergencyContactForm(forms.ModelForm):
	# relationship = forms.CharField(widget=autocomplete_light.TextWidget('RelationshipAutocomplete'), required=False)
	emergency_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	emergency_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	emergency_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))

	class Meta:
		model = EmergencyContact
		fields = '__all__'

	def clean(self):
		# relationship = self.cleaned_data['relationship']
		# _relationship = Relationship.objects.get_or_create({'relationship':relationship}, relationship__iexact=relationship)
		# if _relationship:
		# 	_relationship = Relationship.objects.get(relationship__iexact=relationship)
		# self.cleaned_data['relationship'] = _relationship

		barangay = self.cleaned_data['emergency_barangay']
		_barangay = Barangay.objects.get_or_create({'barangay':barangay}, barangay__iexact=barangay)
		if _barangay:
			_barangay = Barangay.objects.get(barangay__iexact=barangay)

		municipality = self.cleaned_data['emergency_municipality']
		_municipality = Municipality.objects.get_or_create({'municipality':municipality}, municipality__iexact=municipality)
		if _municipality:
			_municipality = Municipality.objects.get(municipality__iexact=municipality)
		
		zip = self.cleaned_data['emergency_zip']
		try:
			_zip = Zip.objects.get_or_create(zip=zip, barangay=_barangay, municipality=_municipality)[0]
		except:
			_zip = Zip.objects.get(zip=zip)
		self.cleaned_data['emergency_zip'] = _zip

		
	def save(self, commit=True):
		try:
			# relationship = self.cleaned_data['relationship']
			emergency_zip = str(self.cleaned_data['emergency_zip'])
			emergency = super(EmergencyContactForm, self).save(commit=False)

			# emergency.relationship = relationship
			emergency.zip = zip
			emergency.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

class EvaluationForm(forms.ModelForm):
	evaluation = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Evaluation"}), required=False)
	class Meta:
		model = Evaluation
		fields = '__all__'

	def save(self, commit=True):
		evaluated_by = self.cleaned_data['evaluated_by']
		evaluation = self.cleaned_data['evaluation']
		user = self.cleaned_data['user']
		evaluation_form = super(EvaluationForm, self).save(commit=False)
		_evaluation = Evaluation.objects.get_or_create(evaluation=evaluation, user=user, evaluated_by=evaluated_by)
		if _evaluation:
			_evaluation = Evaluation.objects.get(evaluation=evaluation, user=user, evaluated_by=evaluated_by)
		evaluation_form.evaluation = _evaluation
		self.cleaned_data['evaluation'] = _evaluation
		value = self.cleaned_data
		Evaluation.objects.get_or_create(**value)

class PassportForm(forms.ModelForm):
	passport_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('PassportPlaceIssuedAutocomplete'), required=False)
	class Meta:
		model = Passport
		fields = '__all__'
		exclude = ('passport_place_issued', 'user')

	def save(self, commit=True):
		passport_place_issued = self.cleaned_data['passport_place_issued']
		passport = super(PassportForm, self).save(commit=False)
		passports_place_issued = PassportPlaceIssued.objects.get_or_create({'passport_place':passport_place_issued}, passport_place__iexact=passport_place_issued)
		if passports_place_issued:
			passports_place_issued = PassportPlaceIssued.objects.get(passport_place__iexact=passport_place_issued)
		passport.passport_place_issued = passports_place_issued
		passport.save()

class SBookForm(forms.ModelForm):
	sbook_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('SBookPlaceIssuedAutocomplete'), required=False)
	class Meta:
		model = Sbook
		fields = '__all__'
		exclude = ('sbook_place_issued', 'user')

	def save(self, commit=True):
		sbook_place_issued = self.cleaned_data['sbook_place_issued']
		sbook = super(SBookForm, self).save(commit=False)
		sbooks_place_issued = SBookPlaceIssued.objects.get_or_create({'sbook_place':sbook_place_issued}, sbook_place__iexact=sbook_place_issued)
		if sbooks_place_issued:
			sbooks_place_issued = SBookPlaceIssued.objects.get(sbook_place__iexact=sbook_place_issued)
		sbook.sbook_place_issued = sbooks_place_issued
		sbook.save()

class USVisaForm(forms.ModelForm):
	CHOICES = (
			(True, 'Yes'),
			(False, 'No'),
		)
	us_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))
	us_visa_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('USVisaPlaceIssuedAutocomplete'), required=False)
	class Meta:
		model = USVisa
		fields = '__all__'
		exclude = ('us_visa_place_issued', 'user')

	def save(self, commit=True):
		us_visa_place_issued = self.cleaned_data['us_visa_place_issued']
		us_visa = super(USVisaForm, self).save(commit=False)
		us_visas_place_issued = USVisaPlaceIssued.objects.get_or_create({'us_visa_place':us_visa_place_issued}, us_visa_place__iexact=us_visa_place_issued)
		if us_visas_place_issued:
			us_visas_place_issued = USVisaPlaceIssued.objects.get(us_visa_place__iexact=us_visa_place_issued)
		us_visa.us_visa_place_issued = us_visas_place_issued
		us_visa.save()

class SchengenVisaForm(forms.ModelForm):
	CHOICES = (
		(True, 'Yes'),
		(False, 'No'),
	)
	schengen_visa = forms.NullBooleanField(widget=forms.RadioSelect(choices=CHOICES, renderer=HorizontalRadioRenderer))	
	schengen_visa_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('SchengenVisaPlaceIssuedAutocomplete'), required=False)
	class Meta:
		model = SchengenVisa
		fields = '__all__'
		exclude = ('schengen_visa_place_issued', 'user')

	def save(self, commit=True):
		schengen_visa_place_issued = self.cleaned_data['schengen_visa_place_issued']
		schengen_visa = super(SchengenVisaForm, self).save(commit=False)
		schengen_visas_place_issued = SchengenVisaPlaceIssued.objects.get_or_create({'schengen_visa_place':schengen_visa_place_issued}, schengen_visa_place__iexact=schengen_visa_place_issued)
		if schengen_visas_place_issued:
			schengen_visas_place_issued = SchengenVisaPlaceIssued.objects.get(schengen_visa_place__iexact=schengen_visa_place_issued)
		schengen_visa.schengen_visa_place_issued = schengen_visas_place_issued
		schengen_visa.save()

class YellowFeverForm(forms.ModelForm):
	yellow_fever_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('YellowFeverPlaceIssuedAutocomplete'), required=False)
	class Meta:
		model = YellowFever
		fields = '__all__'
		exclude = ('yellow_fever_place_issued', 'user')

	def save(self, commit=True):
		yellow_fever_place_issued = self.cleaned_data['yellow_fever_place_issued']
		yellow_fever = super(YellowFeverForm, self).save(commit=False)
		yellow_fevers_place_issued = YellowFeverPlaceIssued.objects.get_or_create({'yellow_fever_place':yellow_fever_place_issued}, yellow_fever_place__iexact=yellow_fever_place_issued)
		if yellow_fevers_place_issued:
			yellow_fevers_place_issued = YellowFeverPlaceIssued.objects.get(yellow_fever_place__iexact=yellow_fever_place_issued)
		yellow_fever.yellow_fever_place_issued = yellow_fevers_place_issued
		yellow_fever.save()

class COCForm(forms.ModelForm):
	coc_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('COCPlaceIssuedAutocomplete'), initial='dasda', required=False)
	coc_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)
	class Meta:
		model = COC
		fields = '__all__'
		exclude = ('coc_place_issued', 'coc_rank', 'user')

	def save(self, commit=True):
		rank = self.cleaned_data['coc_rank']
		coc_place_issued = self.cleaned_data['coc_place_issued']
		coc = super(COCForm, self).save(commit=False)
		cocs_place_issued = COCPlaceIssued.objects.get_or_create({'coc_place':coc_place_issued}, coc_place__iexact=coc_place_issued)
		coc_rank = COCRank.objects.get_or_create({'coc_rank':rank}, coc_rank__iexact=rank)
		if cocs_place_issued:
			cocs_place_issued = COCPlaceIssued.objects.get(coc_place__iexact=coc_place_issued)
		if coc_rank:
			coc_rank = COCRank.objects.get(coc_rank__iexact=rank)
		coc.coc_rank = coc_rank
		coc.coc_place_issued = cocs_place_issued
		coc.save()

class LicenseForm(forms.ModelForm):
	license_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('LicensePlaceIssuedAutocomplete'), required=False)
	license_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)
	class Meta:
		model = License
		fields = '__all__'
		exclude = ('license_place_issued', 'license_rank', 'user')

	def save(self, commit=True):
		rank = self.cleaned_data['license_rank']
		license_place_issued = self.cleaned_data['license_place_issued']
		license = super(LicenseForm, self).save(commit=False)
		licenses_place_issued = LicensePlaceIssued.objects.get_or_create({'license_place':license_place_issued}, license_place__iexact=license_place_issued)
		license_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if licenses_place_issued:
			licenses_place_issued = LicensePlaceIssued.objects.get(license_place__iexact=license_place_issued)
		if license_rank:
			license_rank = Rank.objects.get(rank__iexact=rank)
		license.license_rank = license_rank	
		license.license_place_issued = licenses_place_issued
		license.save()

class SRCForm(forms.ModelForm):
	src_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)
	
	class Meta:
		model = SRC
		fields = ('src', 'src_date_issued', 'src_expiry', )

	def save(self, commit=True):
		rank = self.cleaned_data['src_rank']
		src = super(SRCForm, self).save(commit=False)
		src_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if src_rank:
			src_rank = Rank.objects.get(rank__iexact=rank)
		src.src_rank = src_rank	
		src.save()

class STCWEndorsementForm(forms.ModelForm):
	stcw_endorsement_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)

	class Meta:
		model =  STCWEndorsement
		fields = ('stcw_endorsement', 'stcw_endorsement_date_issued', 'stcw_endorsement_date_expiry',  'user', )

	def save(self, commit=True):
		rank = self.cleaned_data['stcw_endorsement_rank']
		stcw_endorsement = super(STCWEndorsementForm, self).save(commit=False)
		stcw_endorsement_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if stcw_endorsement_rank:
			stcw_endorsement_rank = Rank.objects.get(rank__iexact=rank)
		stcw_endorsement.stcw_endorsement_rank = stcw_endorsement_rank	
		stcw_endorsement.save()

class STCWCertificateForm(forms.ModelForm):
	stcw_certificate_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)

	class Meta:
		model =  STCWCertificate
		fields = ('stcw_certificate', 'stcw_certificate_date_issued', 'stcw_certificate_date_expiry',  'user', )

	def save(self, commit=True):
		rank = self.cleaned_data['stcw_certificate_rank']
		stcw_certificate = super(STCWCertificateForm, self).save(commit=False)
		stcw_certificate_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if stcw_certificate_rank:
			stcw_certificate_rank = Rank.objects.get(rank__iexact=rank)
		stcw_certificate.stcw_certificate_rank = stcw_certificate_rank	
		stcw_certificate.save()

class GOCForm(forms.ModelForm):
	goc_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)

	class Meta:
		model = GOC
		fields = ('goc', 'goc_date_issued', 'goc_expiry', )

	def save(self, commit=True):
		rank = self.cleaned_data['goc_rank']
		goc = super(GOCForm, self).save(commit=False)
		goc_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if goc_rank:
			goc_rank = Rank.objects.get(rank__iexact=rank)
		goc.goc_rank = goc_rank	
		goc.save()

class NTCLicenseForm(forms.ModelForm):
	ntc_license_rank = forms.CharField(widget=autocomplete_light.TextWidget('RankAutocomplete'), required=False)

	class Meta:
		model = NTCLicense
		fields = ('ntc_license', 'ntc_license_date_issued', 'ntc_license_date_expiry',  'user', )

	def save(self, commit=True):
		rank = self.cleaned_data['ntc_license_rank']
		ntc_license = super(NTCLicenseForm, self).save(commit=False)
		ntc_license_rank = Rank.objects.get_or_create({'rank':rank}, rank__iexact=rank)
		if ntc_license_rank:
			ntc_license_rank = Rank.objects.get(rank__iexact=rank)
		ntc_license.ntc_license_rank = ntc_license_rank	
		ntc_license.save()

class FlagForm(forms.ModelForm):
	class Meta:
		model = FlagDocumentsDetailed
		fields = '__all__'

	def save(self, commit=True):
		try:
			flags = super(FlagForm, self).save(commit=False)
			flags.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

class TrainingCertificateForm(forms.ModelForm):
	place_trained = forms.CharField(widget=autocomplete_light.TextWidget('TrainingCenterAutocomplete'), required=False)
	training_place_issued = forms.CharField(widget=autocomplete_light.TextWidget('TrainingPlaceIssuedAutocomplete'), required=False)
	trainings_certificates  = forms.ModelChoiceField(queryset=TrainingCertificates.objects.filter(), required=False)
	class Meta:
		model = TrainingCertificateDocumentsDetailed
		fields = '__all__'

	def clean(self):
		place_trained = self.cleaned_data['place_trained']
		_place_trained = TrainingCenter.objects.get_or_create({'training_center':place_trained}, training_center__iexact=place_trained)
		if _place_trained:
			_place_trained = TrainingCenter.objects.get(training_center__iexact=place_trained)
		self.cleaned_data['place_trained'] = _place_trained

		training_place_issued = self.cleaned_data['training_place_issued']
		_training_place_issued = TrainingPlaceIssued.objects.get_or_create({'training_place':training_place_issued}, training_place__iexact=training_place_issued)
		if _training_place_issued:
			_training_place_issued = TrainingPlaceIssued.objects.get(training_place__iexact=training_place_issued)
		self.cleaned_data['training_place_issued'] = _training_place_issued

	def save(self, commit=True):
		try:
			place_trained = self.cleaned_data['place_trained']
			training_place_issued = self.cleaned_data['training_place_issued']
			trainings_certificates = super(TrainingCertificateForm, self).save(commit=False)
			
			trainings_certificates.place_trained = place_trained
			trainings_certificates.training_place_issued = training_place_issued
			trainings_certificates.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

class DependentsForm(forms.ModelForm):
	# dependent_relationship = forms.CharField(widget=autocomplete_light.TextWidget('RelationshipAutocomplete'), required=False)
	dependent_zip = forms.IntegerField(widget=forms.NumberInput(attrs={'min':0}))
	dependent_barangay = forms.CharField(widget=autocomplete_light.TextWidget('BarangayAutocomplete'))
	dependent_municipality = forms.CharField(widget=autocomplete_light.TextWidget('MunicipalityAutocomplete'))

	class Meta:
		model = Dependents
		fields = '__all__'

	def clean(self):
		barangay = self.cleaned_data['dependent_barangay']
		_barangay = Barangay.objects.get_or_create({'barangay':barangay}, barangay__iexact=barangay)
		if _barangay:
			_barangay = Barangay.objects.get(barangay__iexact=barangay)

		municipality = self.cleaned_data['dependent_municipality']
		_municipality = Municipality.objects.get_or_create({'municipality':municipality}, municipality__iexact=municipality)
		if _municipality:
			_municipality = Municipality.objects.get(municipality__iexact=municipality)
		
		zip = self.cleaned_data['dependent_zip']
		try:
			_zip = Zip.objects.get_or_create(zip=zip, barangay=_barangay, municipality=_municipality)[0]
		except:
			_zip = Zip.objects.get(zip=zip)
		self.cleaned_data['dependent_zip'] = _zip

		
	def save(self, commit=True):
		try:
			# relationship = self.cleaned_data['dependent_relationship']
			dependent_zip = str(self.cleaned_data['dependent_zip'])
			dependent = super(DependentsForm, self).save(commit=False)

			# dependent.dependent_relationship = relationship
			dependent.zip = zip
			dependent.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]) )

class SeaServiceForm(forms.ModelForm):
	vessel_name = forms.CharField(widget=autocomplete_light.TextWidget('ManshipVesselNameAutocomplete'))
	flag = forms.ModelChoiceField(queryset=Flags.objects.filter())
	principal = forms.CharField(widget=autocomplete_light.TextWidget('ManshipPrincipalAutocomplete'))
	manning_agency = forms.ModelChoiceField(queryset=ManningAgency.objects.filter(), initial=ManningAgency.objects.get(manning_agency='MANSHIP'))
	trade_area = forms.CharField(widget=autocomplete_light.TextWidget('TradeAreaAutocomplete'), required=False)
	class Meta:
		model = SeaService
		fields = '__all__'

	def clean(self):
		trade_area = self.cleaned_data['trade_area']
		_trade_area = TradeArea.objects.get_or_create({'trade_area':trade_area}, trade_area__iexact=trade_area)
		if _trade_area:
			_trade_area = TradeArea.objects.get(trade_area__iexact=trade_area)
		self.cleaned_data['trade_area'] = _trade_area

		vessel_name = self.cleaned_data['vessel_name']
		_vessel_name = VesselName.objects.get_or_create({'vessel_name':vessel_name, 'manship_standard':True}, vessel_name__iexact=vessel_name)
		if _vessel_name:
			_vessel_name = VesselName.objects.get(vessel_name__iexact=vessel_name)
		self.cleaned_data['vessel_name'] = _vessel_name

		principal = self.cleaned_data['principal']
		_principal =Principal.objects.get_or_create({'principal':principal, 'manship_standard':True}, principal__iexact=principal)
		if _principal:
			_principal = Principal.objects.get(principal__iexact=principal)
		self.cleaned_data['principal'] = _principal

	def save(self, commit=True):
		try:
			trade_area = self.cleaned_data['trade_area']
			vessel_name = self.cleaned_data['vessel_name']
			principal = self.cleaned_data['principal']
			sea_services = super(SeaServiceForm, self).save(commit=False)
			sea_services.trade_area = trade_area
			sea_services.vessel_name = vessel_name
			sea_services.principal = principal
			sea_services.save()
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))

class MarinerStatusForm(forms.ModelForm):
	# mariner_status_comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)
	mariner_principal = forms.ModelChoiceField(queryset=Principal.objects.filter(manship_standard=1))
	class Meta:
		model = MarinerStatusHistory
		fields = '__all__'
		# exclude = ('mariner_status_comment', )

	# Script create if there is a change otherwise none
	def save(self, commit=True):
		# mariner_status_comment = self.cleaned_data['mariner_status_comment']
		mariner_status_form = super(MarinerStatusForm, self).save(commit=False)
		# _mariner_status_comment = MarinerStatusComment.objects.get_or_create(mariner_status_comment=mariner_status_comment)
		# if _mariner_status_comment:
			# _mariner_status_comment = MarinerStatusComment.objects.get(mariner_status_comment=mariner_status_comment)
		# mariner_status_form.mariner_status_comment = _mariner_status_comment
		# self.cleaned_data['mariner_status_comment'] = _mariner_status_comment
		value = self.cleaned_data
		MarinerStatusHistory.objects.get_or_create(**value)
		# mariner_status_form.save()

class ScannedDocumentsForm(forms.ModelForm):
	pass
	# class Meta:
	# 	model = ScannedDocuments
	# 	fields = ('user', 'folder_path', 'scan', 'uploaded_by')