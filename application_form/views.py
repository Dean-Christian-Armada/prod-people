from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory, inlineformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings

# from easy_pdf.rendering import render_to_pdf_response

from django.core.files.base import ContentFile

from . forms import *

import os, shutil, datetime, random, string, urllib, ast



# Create your views here.
# Take notes Logic of form save is in the forms.py save method of own FormObjects


# Enables field required on formset even without filling up a singlefield
# class RequiredFormSet(BaseFormSet):
#     def __init__(self, *args, **kwargs):
#         super(RequiredFormSet, self).__init__(*args, **kwargs)
#         for form in self.forms:
#             form.empty_permitted = False

# Enables field required on the first form
class FirstRequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(FirstRequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False

@login_required()
def form(request):
	scheme = request.scheme
	http_host = request.META['HTTP_HOST']
	today = date.today()
	today = today.strftime("%m/%d/%y")
	count_college_errors = 0
	count_emergency_errors = 0
	request_training_certificates = ''


	applicant_name = ApplicantNameForm()
	personal_data = PersonalDataForm()
	permanent_address = PermanentAddressForm()
	current_address = CurrentAddressForm()
	spouse = SpouseForm()
	college = formset_factory(CollegeForm, extra=5, formset=FirstRequiredFormSet)
	highschool = HighSchoolForm()
	emergency_contact = formset_factory(EmergencyContactForm, extra=5, formset=FirstRequiredFormSet)
	visa_application = VisaApplicationForm()
	detained = DetainedForm()
	disciplinary_action = DisciplinaryActionForm()
	charged_offense = ChargedOffenseForm()
	termination = TerminationForm()
	passport = PassportForm()
	sbook = SbookForm()
	coc = COCForm()
	license = LicenseForm()
	src = SRCForm()
	goc = GOCForm()
	us_visa = USVisaForm()
	schengen_visa = SchengenVisaForm()
	yellow_fever = YellowFeverForm()
	flags = FlagForm()
	trainings_certificates = TrainingCertificateForm()
	sea_service = formset_factory(SeaServiceForm, extra=20)
	application = ApplicationForm(initial={'scheme': scheme, 'http_host': http_host, 'application_date': today})

	if request.method == "POST":
		print request.POST
		applicant_name = ApplicantNameForm(request.POST)
		permanent_address = PermanentAddressForm(request.POST)
		current_address = CurrentAddressForm(request.POST)
		personal_data = PersonalDataForm(request.POST)
		spouse = SpouseForm(request.POST)
		college = college(request.POST)
		highschool = HighSchoolForm(request.POST)
		emergency_contact = emergency_contact(request.POST)
		visa_application = VisaApplicationForm(request.POST)
		detained = DetainedForm(request.POST)
		disciplinary_action = DisciplinaryActionForm(request.POST)
		charged_offense = ChargedOffenseForm(request.POST)
		termination = TerminationForm(request.POST)
		passport = PassportForm(request.POST)
		sbook = SbookForm(request.POST)
		coc = COCForm(request.POST)
		license = LicenseForm(request.POST)
		src = SRCForm(request.POST)
		goc = GOCForm(request.POST)
		us_visa = USVisaForm(request.POST)
		schengen_visa = SchengenVisaForm(request.POST)
		yellow_fever = YellowFeverForm(request.POST)
		flags = FlagForm(request.POST)
		trainings_certificates = TrainingCertificateForm(request.POST)
		sea_service = sea_service(request.POST)
		application = ApplicationForm(request.POST)

		request_training_certificates = request.POST.getlist('trainings_certificates')
		request_training_certificates = [int(x) for x in request_training_certificates]

		if applicant_name.is_valid() and personal_data.is_valid() and permanent_address.is_valid() and current_address.is_valid() and spouse.is_valid() and college.is_valid() and highschool.is_valid() and emergency_contact.is_valid() and visa_application.is_valid() and detained.is_valid() and disciplinary_action.is_valid() and charged_offense.is_valid() and termination.is_valid() and passport.is_valid() and sbook.is_valid()and coc.is_valid()and license.is_valid()and src.is_valid()and goc.is_valid()and us_visa.is_valid()and schengen_visa.is_valid()and yellow_fever.is_valid() and flags.is_valid() and trainings_certificates.is_valid() and sea_service.is_valid() and application.is_valid():
			applicant_name.save()
			permanent_address.save()
			current_address.save()
			personal_data.save()
			spouse.save()
			for college_form in college:
				college_form.save()
			highschool.save()
			for emergency_contact_form in emergency_contact:
				emergency_contact_form.save()
			# emergency_contact.save()
			visa_application.save()
			detained.save()
			disciplinary_action.save()
			charged_offense.save()
			termination.save()
			passport.save()
			sbook.save()
			coc.save()
			license.save()
			src.save()
			goc.save()
			us_visa.save()
			schengen_visa.save()
			yellow_fever.save()
			flags.save()
			flags.save_m2m()
			trainings_certificates.save()
			trainings_certificates.save_m2m()
			for sea_service_form in sea_service:
				sea_service_form.save()
			application.save()
			return HttpResponseRedirect('/application-form/success/')
		else:
			# For formset validations on error validations html
			# To uncount empty dictionary errors made by the formset
			for college_errors in college.errors:
				if college_errors != {}:
					count_college_errors+=1

			for emergency_errors in emergency_contact.errors:
				if emergency_errors != {}:
					count_emergency_errors+=1
			print applicant_name.errors
			print permanent_address.errors
			print current_address.errors
			print personal_data.errors
			print spouse.errors
			print college.errors
			print highschool.errors
			print emergency_contact.errors
			print visa_application.errors
			print detained.errors
			print disciplinary_action.errors
			print charged_offense.errors
			print termination.errors
			print passport.errors
			print sbook.errors
			print coc.errors
			print license.errors
			print src.errors
			print goc.errors
			print us_visa.errors
			print schengen_visa.errors
			print yellow_fever.errors
			print flags.errors
			print trainings_certificates.errors
			print sea_service.errors
			print application.errors


	template = "application_form/index.html"
	context_dict = {"title": "Application Form"}
	context_dict['applicant_name'] = applicant_name
	context_dict['permanent_address'] = permanent_address
	context_dict['current_address'] = current_address
	context_dict['personal_data'] = personal_data
	context_dict['spouse_form'] = spouse
	context_dict['college'] = college
	context_dict['count_college_errors'] = count_college_errors
	context_dict['highschool_form'] = highschool
	context_dict['emergency'] = emergency_contact
	context_dict['count_emergency_errors'] = count_emergency_errors
	context_dict['visa_application'] = visa_application
	context_dict['detained'] = detained
	context_dict['disciplinary_action'] = disciplinary_action
	context_dict['charged_offense'] = charged_offense
	context_dict['termination'] = termination
	context_dict['passport_form'] = passport
	context_dict['sbook_form'] = sbook 
	context_dict['coc_form'] = coc 
	context_dict['license_form'] = license 
	context_dict['src_form'] = src 
	context_dict['goc_form'] = goc 
	context_dict['usvisa_form'] = us_visa 
	context_dict['schengenvisa_form'] = schengen_visa 
	context_dict['yellowfever_form'] = yellow_fever
	context_dict['flags'] = flags
	context_dict['trainings_certificates'] = trainings_certificates
	context_dict['seaservice_form'] = sea_service
	context_dict['application'] = application
	
	context_dict['request_training_certificates'] = request_training_certificates

	return render(request, template, context_dict)


@login_required
def success(request):
	template = "application_form/success.html"
	context_dict = {"title": "Thank You For Applying at Manship"}
	return render(request, template, context_dict)

@csrf_exempt
@login_required
def tmp_image(request):
	if request.method == 'POST':
		tmp_image_name = ''.join(random.choice(string.lowercase) for i in range(10))
		# request file coming from the webcamjs
		files = request.FILES['webcam']
		# Script that convert the inmemoryupload to a file
		files = ContentFile(files.read())
		x = 'photos/tmp/'+tmp_image_name+'.jpg'
		# script saving to a folder
		path = default_storage.save(x, files)
		scheme = request.scheme
		http_host = request.META['HTTP_HOST']
		return HttpResponse(scheme+"://"+http_host+"/media/"+x)
	else:
		return HttpResponse("No data")

@login_required
def trainings_certificates(request):
	id = request.GET['id']
	requests = request.GET.get('request', '')
	# ast.literal_eval converts the whole unicode list structure into an actual list
	if requests:
		requests = ast.literal_eval(requests)
	if id:
		form = DynamicTrainingCertificateForm(id, initial={'trainings_certificates': requests})
	else:
		form = "Please Select the Applied Position First for the Certificates and Trainigns to show"

	template = "application_form/training-certificates.html"
	context_dict = { "form":form }
	return render(request, template, context_dict)


# def fleet_application_form(request, principal, vessel_type):
@login_required
def fleet_application_form(request, principal, id):
	from mariners_profile.forms import *

	user_profile = UserProfile.objects.get(id=id)
	personal_data = PersonalData.objects.get(name=id)

	# Used for formset updating / inlineformset_factory
	college = College.objects.filter(user=id)

	# Script to get the latest college
	# college = College.objects.filter(user=id).order_by('-id').values('id')[0]['id']
	# college =  College.objects.get(id=college)
	#  Script to get the latest college

	# Script to get the latest emergency contact
	emergency_contact = EmergencyContact.objects.filter(user=id).order_by('-id').values('id')[0]['id']
	emergency_contact =  EmergencyContact.objects.get(id=emergency_contact)
	#  Script to get the latest emergency contact

	highschool = HighSchool.objects.get(user=id)
	passport = Passport.objects.get(user=id)
	sbook = Sbook.objects.get(user=id)
	us_visa = USVisa.objects.get(user=id)
	schengen_visa = SchengenVisa.objects.get(user=id)
	yellow_fever = YellowFever.objects.get(user=id)
	license = License.objects.get(user=id)
	coc = COC.objects.get(user=id)

	applicant_name_form = ApplicantNameForm(request.POST or None, instance=user_profile)
	personal_data_form = PersonalDataForm(request.POST or None, instance=personal_data, initial={'birth_place':personal_data.birth_place, 'preferred_vessel_type':personal_data.preferred_vessel_type, 'dialect':personal_data.dialect})
	permanent_address_form = PermanentAddressForm(request.POST or None, instance=personal_data.permanent_address, initial={'permanent_zip':personal_data.permanent_address.permanent_zip.zip, 'permanent_barangay':personal_data.permanent_address.permanent_zip.barangay, 'permanent_municipality':personal_data.permanent_address.permanent_zip.municipality})
	current_address_form = CurrentAddressForm(request.POST or None, instance=personal_data.current_address, initial={'current_zip':personal_data.current_address.current_zip.zip, 'current_barangay':personal_data.current_address.current_zip.barangay, 'current_municipality':personal_data.current_address.current_zip.municipality})

	try:
		
		spouse = Spouse.objects.get(user=id)
		spouse_form = SpouseForm(request.POST or None, instance=spouse)
	except:
		spouse = ''
		spouse_form = SpouseForm(request.POST or None, initial={'user':personal_data.name, } )


	# CollegeFormSet = modelformset_factory(College, form=CollegeForm)
	# college_form = CollegeFormSet(request.POST or None, queryset=college)

	# Used for formset updating / inlineformset_factory
	CollegeFormSet = inlineformset_factory(UserProfile, College, extra=0, can_delete=False, form=CollegeForm )
	college_form = CollegeFormSet(request.POST or None, instance=user_profile)

	try:
		vocational = Vocational.objects.get(user=id)
		vocational_form = VocationalForm(request.POST or None, instance=vocational, initial={'vocational':vocational.vocational})
	except:
		vocational = ''
		vocational_form = VocationalForm(request.POST or None, initial={'user': personal_data.name} )

	# Script to get the latest college
	# college_form = CollegeForm(request.POST or None, instance=college, initial={'college':college.college, 'degree':college.degree})

	try:
		land_employment = LandEmployment.objects.filter(user=id)
		if len(land_employment) == 1:
			num_extra = 1
		elif len(land_employment) < 1:
			num_extra = 2
		LandEmploymentFormSet = inlineformset_factory(UserProfile, LandEmployment, fk_name='user', extra=1, can_delete=True, form=LandEmploymentForm )
		land_employment_form = LandEmploymentFormSet(request.POST or None, instance=user_profile )

	except:
		print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])


	try:
		beneficiary = Beneficiary.objects.filter(user=id)
		if len(beneficiary) == 1:
			num_extra = 1
		elif len(beneficiary) < 1:
			num_extra = 2
		BeneficiaryFormSet = inlineformset_factory(UserProfile, Beneficiary, fk_name='user', extra=1, can_delete=True, form=BeneficiaryForm )
		beneficiary_form = BeneficiaryFormSet(request.POST or None, instance=user_profile )

	except:
		print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

	try:
		allotee = Allotee.objects.filter(user=id)
		if len(allotee) == 1:
			num_extra = 1
		elif len(allotee) < 1:
			num_extra = 2
		AlloteeFormSet = inlineformset_factory(UserProfile, Allotee, fk_name='user', extra=1, can_delete=True, form=AlloteeForm )
		allotee_form = AlloteeFormSet(request.POST or None, instance=user_profile )

	except:
		print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])


	# Script to get the latest emergency contact
	emergency_contact_form = EmergencyContactForm(request.POST or None, instance=emergency_contact, initial={'relationship':emergency_contact.relationship, 'emergency_zip':emergency_contact.emergency_zip, 'emergency_municipality':emergency_contact.emergency_zip.municipality, 'emergency_barangay':emergency_contact.emergency_zip.barangay, })

	# Used for formset updating / inlineformset_factory
	# EmergencyContactFormSet = inlineformset_factory(UserProfile, EmergencyContact, fields='__all__', extra=0, can_delete=True )
	# emergency_contact_form = EmergencyContactFormSet(request.POST or None, instance=user_profile)

	highschool_form = HighSchoolForm(request.POST or None, instance=highschool, initial={'highschool':highschool.highschool})

	try:
		primaryschool = PrimarySchool.objects.get(user=id)
		primaryschool_form = PrimarySchoolForm(request.POST or None, instance=primaryschool, initial={'primaryschool':primaryschool.primaryschool})
	except:
		primaryschool = ''
		primaryschool_form = PrimarySchoolForm(request.POST or None, initial={'user': personal_data.name} )


	passport_form = PassportForm(request.POST or None, instance=passport, initial={'passport_place_issued':passport.passport_place_issued})
	sbook_form = SBookForm(request.POST or None, instance=sbook, initial={'sbook_place_issued':sbook.sbook_place_issued})
	us_visa_form = USVisaForm(request.POST or None, instance=us_visa, initial={'us_visa':us_visa.us_visa, 'us_visa_place_issued':us_visa.us_visa_place_issued})
	schengen_visa_form = SchengenVisaForm(request.POST or None, instance=schengen_visa, initial={'schengen_visa':schengen_visa.schengen_visa, 'schengen_visa_place_issued':schengen_visa.schengen_visa_place_issued})
	yellow_fever_form = YellowFeverForm(request.POST or None, instance=yellow_fever, initial={'yellow_fever_place_issued':yellow_fever.yellow_fever_place_issued})
	license_form = LicenseForm(request.POST or None, instance=license, initial={'license_place_issued':license.license_place_issued, 'license_rank':license.license_rank})
	coc_form = COCForm(request.POST or None, instance=coc, initial={'coc_place_issued':coc.coc_place_issued, 'coc_rank':coc.coc_rank})

	# if applicant_name_form.is_valid():
	# 	applicant_name_form.save()
	# else:
	# 	applicant_name_form.errors

	# if personal_data_form.is_valid():
	# 	personal_data_form.save()
	# else:
	# 	print personal_data_form.errors

	# if permanent_address_form.is_valid():
	# 	permanent_address_form.save()
	# else:
	# 	print permanent_address_form.errors

	# if current_address_form.is_valid():
	# 	current_address_form.save()
	# else:
	# 	print current_address_form.errors

	# if spouse_form.is_valid():
	# 	spouse_form.save()
	# else:
	# 	print spouse_form.errors

	# if college_form.is_valid():
	# 	for college in college_form:
	# 		college.save()
	# else:
	# 	print college_form.errors

	# if vocational_form.is_valid():
	# 	vocational_form.save()
	# else:
	# 	print vocational_form.errors

	# if highschool_form.is_valid():
	# 	highschool_form.save()
	# else:
	# 	print highschool_form.errors

	# if primaryschool_form.is_valid():
	# 	primaryschool_form.save()
	# else:
	# 	print primaryschool_form.errors

	# if land_employment_form.is_valid():
	# 	for land_employment in land_employment_form:
	# 		land_employment.save()
	# else:
	# 	print land_employment_form.errors

	# if beneficiary_form.is_valid():
	# 	for beneficiary in beneficiary_form:
	# 		beneficiary.save()
	# else:
	# 	print beneficiary_form.errors

	if allotee_form.is_valid():
		for allotee in allotee_form:
			allotee.save()
	else:
		print allotee_form.errors

	# Travel Documents Testing
	# if passport_form.is_valid() and sbook_form.is_valid() and us_visa_form.is_valid() and schengen_visa_form.is_valid() and yellow_fever_form.is_valid():
	# 		passport_form.save()
	# 		sbook_form.save()
	# 		us_visa_form.save()
	# 		schengen_visa_form.save()
	# 		yellow_fever_form.save()
	# else:
		# passport_form.errors
		# sbook_form.errors
		# us_visa_form.errors
		# schengen_visa_form.errors
		# yellow_fever_form.errors


	# LICENSES
	# if license_form.is_valid() and coc_form.is_valid():
	# 	license_form.save()
	# 	coc_form.save()
	# else:
	# 	license_form.errors
	# 	coc_form.errors


	# template = "principals-application-form/%s-%s.html" % (principal, vessel_type)
	template = "principals-application-form/%s.html" % (principal)
	context_dict = {}
	context_dict['applicant_name_form'] = applicant_name_form
	context_dict['personal_data_form'] = personal_data_form
	context_dict['permanent_address_form'] = permanent_address_form
	context_dict['current_address_form'] = current_address_form
	context_dict['spouse_form'] = spouse_form
	context_dict['emergency_contact_form'] = emergency_contact_form
	context_dict['passport_form'] = passport_form
	context_dict['sbook_form'] = sbook_form
	context_dict['us_visa_form'] = us_visa_form
	context_dict['schengen_visa_form'] = schengen_visa_form
	context_dict['yellow_fever_form'] = yellow_fever_form
	context_dict['license_form'] = license_form
	context_dict['coc_form'] = coc_form
	# context_dict['college_form'] = college_form
	context_dict['vocational_form'] = vocational_form
	context_dict['highschool_form'] = highschool_form
	context_dict['primaryschool_form'] = primaryschool_form
	# context_dict['land_employment_form'] = land_employment_form
	# context_dict['beneficiary_form'] = beneficiary_form
	context_dict['allotee_form'] = allotee_form

	return render(request, template, context_dict)
	# return HttpResponse(template)