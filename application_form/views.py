from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory, inlineformset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.core import serializers

# from easy_pdf.rendering import render_to_pdf_response

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
	from application_form.models import ApplicationForm
	if id:
		user_profile = UserProfile.objects.get(id=id)
		mariners_profile = MarinersProfile.objects.get(user=user_profile)
		application_form = ApplicationForm.objects.get(user=user_profile)
		personal_data = PersonalData.objects.get(name=id)
		current_address = CurrentAddress.objects.get(personaldata=personal_data.id)
		permanent_address = PermanentAddress.objects.get(personaldata=personal_data.id)
		flag_documents = FlagDocuments.objects.get(user=user_profile)
		flag_documents = FlagDocumentsDetailed.objects.filter(flags_documents=flag_documents)
		trainings_certificate_documents = TrainingCertificateDocuments.objects.get(user=user_profile)
		
		highschool = HighSchool.objects.get(user=id)
		passport = Passport.objects.get(user=id)
		sbook = Sbook.objects.get(user=id)
		us_visa = USVisa.objects.get(user=id)
		schengen_visa = SchengenVisa.objects.get(user=id)
		yellow_fever = YellowFever.objects.get(user=id)
		license = License.objects.get(user=id)
		coc = COC.objects.get(user=id)
		src = SRC.objects.get(user=id)
		goc = GOC.objects.get(user=id)

		college = College.objects.filter(user=id)
		emergency_contact = EmergencyContact.objects.filter(user=id)
		dependents = Dependents.objects.filter(user=id)
		land_employment = LandEmployment.objects.filter(user=id)
		beneficiary = Beneficiary.objects.filter(user=id)
		allotee = Allotee.objects.filter(user=id)
		history = MarinerStatusHistory.objects.filter(user=id).order_by('-id')
		current_history = history[0]

		try:
			spouse = Spouse.objects.get(user=id)
		except:
			spouse = ''
		try:
			vocational = Vocational.objects.get(user=id)
		except:
			vocational = ''
		try:
			primaryschool = PrimarySchool.objects.get(user=id)
		except:
			primaryschool = ''
		try:
			stcw_endorsement = STCWEndorsement.objects.get(user=id)
		except:
			stcw_endorsement = ''
		try:
			stcw_certificate = STCWCertificate.objects.get(user=id)
		except:
			stcw_certificate = ''

		try:
			ntc_license = NTCLicense.objects.get(user=id)
		except:
			ntc_license = ''

		try:
			evaluation = Evaluation.objects.get(user=id)
		except:
			evaluation = ''

		template = "principals-application-form/%s.html" % (principal)
		title = ("%s application form" % (principal)).title()
		context_dict = {}
		context_dict['title'] = title

		context_dict['user_profile'] = user_profile
		context_dict['mariners_profile'] = mariners_profile
		context_dict['application_form'] = application_form
		context_dict['personal_data'] = personal_data
		context_dict['current_address'] = current_address
		context_dict['permanent_address'] = permanent_address
		context_dict['flag_documents'] = flag_documents
		context_dict['trainings_certificate_documents'] = trainings_certificate_documents

		context_dict['highschool'] = highschool
		context_dict['passport'] = passport
		context_dict['sbook'] = sbook
		context_dict['us_visa'] = us_visa
		context_dict['schengen_visa'] = schengen_visa
		context_dict['yellow_fever'] = yellow_fever
		context_dict['license'] = license
		context_dict['coc'] = coc
		context_dict['src'] = src
		context_dict['goc'] = goc

		context_dict['college'] = college
		context_dict['emergency_contact'] = emergency_contact
		context_dict['dependents'] = dependents
		context_dict['land_employment'] = land_employment
		context_dict['beneficiary'] = beneficiary
		context_dict['allotee'] = allotee
		context_dict['history'] = history

		context_dict['spouse'] = spouse
		context_dict['vocational'] = vocational
		context_dict['primaryschool'] = primaryschool
		context_dict['stcw_endorsement'] = stcw_endorsement
		context_dict['stcw_certificate'] = stcw_certificate
		context_dict['ntc_license'] = ntc_license
		context_dict['evaluation'] = evaluation

		return render(request, template, context_dict)
		# return HttpResponse(template)