from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Sum, Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.core import serializers

from easy_pdf.rendering import render_to_pdf_response

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
		principal_object = Principal.objects.get(principal__iexact=principal)
		principal_flags = principal_object.flags_standard.all()
		flag_document = FlagDocuments.objects.get(user=user_profile)
		flag_documents = FlagDocumentsDetailed.objects.filter(flags_documents=flag_document).filter(flags__in=principal_flags)
		flag_documents_valid = FlagDocumentsDetailed.objects.filter(flags_documents=flag_document).filter(~Q(sbook_number=None))
		principal_trainings_certificate = principal_object.trainings_certificate_standard.all()
		trainings_certificate_document = TrainingCertificateDocuments.objects.get(user=user_profile)
		trainings_certificate_documents = TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificate_documents=trainings_certificate_document).filter(trainings_certificates__in=principal_trainings_certificate)
		
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
		sea_service = SeaService.objects.filter(user=id)
		history = MarinerStatusHistory.objects.filter(user=id).order_by('-id')
		try:
			current_history = history[0]
		except:
			current_history = ""
		reference = Reference.objects.filter(user=id)

		# Script to get the flags issuing authority of the other seaman's book
		flag_books = []
		for flag_document in flag_documents_valid:
			flag_books.append(flag_document.flags.flags)
		flag_books = ', '.join(flag_books)

		# Script to get the duration of the current rank via year with conditional of days if less than
		# Used for Ionic application form
		rank_sea_service_duration = []
		rank_sea_service = sea_service.filter(rank=mariners_profile.position)
		for rank_sea_services in rank_sea_service:
			duration = rank_sea_services.date_left - rank_sea_services.date_joined
			rank_sea_service_duration.append(duration.days)
		rank_sea_service_duration = sum(rank_sea_service_duration)
		rank_sea_duration = rank_sea_service_duration / 365
		rank_sea_duration_days_remainder = rank_sea_service_duration % 365
		if rank_sea_duration:
			if rank_sea_duration_days_remainder:
				rank_sea_duration_days_remainder = "and %s days" % rank_sea_duration_days_remainder
			else:
				rank_sea_duration_days_remainder = ""
			rank_sea_service_duration = "%s year %s" % (rank_sea_duration, rank_sea_duration_days_remainder)
		else:
			rank_sea_service_duration = "%s days" % rank_sea_service_duration

		sea_service_duration = []
		for sea_services in sea_service:
			duration = sea_services.date_left - sea_services.date_joined
			sea_service_duration.append(duration.days)
		sea_service_duration = sum(sea_service_duration)
		sea_duration = sea_service_duration / 365
		sea_duration_days_remainder = sea_service_duration % 365
		if sea_duration:
			if sea_duration_days_remainder:
				sea_duration_days_remainder = "and %s days" % sea_duration_days_remainder
			else:
				sea_duration_days_remainder = ""
			sea_service_duration = "%s year %s" % (sea_duration, sea_duration_days_remainder)
		else:
			sea_service_duration = "%s days" % sea_service_duration

		# Script to get the duration of in dry cargo carriers via year with conditional of days if less than
		dry_vessel_types = VesselType.objects.filter(Q(vessel_type__iexact='Bulk') | Q(vessel_type__iexact='Container') | Q(vessel_type__iexact='Log Bulk'))
		dry_vessel_types_duration = []
		dry_vessel_type_sea_service = sea_service.filter(vessel_type__in=dry_vessel_types)

		for dry_vessel_type_sea_services in dry_vessel_type_sea_service:
			duration = dry_vessel_type_sea_services.date_left - dry_vessel_type_sea_services.date_joined
			dry_vessel_types_duration.append(duration.days)
		dry_vessel_types_duration = sum(dry_vessel_types_duration)
		dry_vessel_duration = dry_vessel_types_duration / 365
		dry_vessel_types_duration_days_remainder = dry_vessel_types_duration % 365
		if dry_vessel_duration:
			if dry_vessel_types_duration_days_remainder:
				dry_vessel_types_duration_days_remainder = "and %s days" % dry_vessel_types_duration_days_remainder
			else:
				dry_vessel_types_duration_days_remainder = ""
			dry_vessel_types_duration = "%s year %s" % (dry_vessel_duration, dry_vessel_types_duration_days_remainder)
		else:
			dry_vessel_types_duration = "%s days" % dry_vessel_types_duration

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

		# START ATHENIAN TRAINING CERTIFICATES
		btoc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BTOC')
		atot = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ATOT')
		bt = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BT')
		psrc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='PSRC')
		aff = TrainingCertificates.objects.get(trainings_certificates_abbreviation='AFF')
		mefa = TrainingCertificates.objects.get(trainings_certificates_abbreviation='MEFA')
		meca = TrainingCertificates.objects.get(trainings_certificates_abbreviation='MECA')
		arpa = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ARPA')
		hazmat = TrainingCertificates.objects.get(trainings_certificates_abbreviation='HAZMAT')
		bms = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BMS')
		ers_erm = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ERS / ERM')
		ecdis_jrc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ECDIS JRC')
		acni = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ACNI')
		sso = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SSO')
		ism = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ISM')

		try:
			btoc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=btoc))
		except:
			btoc_documents = ""
		try:
			atot_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=atot))
		except:
			atot_documents = ""
		try:
			bt_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=bt))
		except:
			bt_documents = ""
		try:
			psrc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=psrc))
		except:
			psrc_documents = ""
		try:
			aff_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=aff))
		except:
			aff_documents = ""
		try:
			mefa_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=mefa))
		except:
			mefa_documents = ""
		try:
			meca_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=meca))
		except:
			meca_documents = ""
		try:
			arpa_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=arpa))
		except:
			arpa_documents = ""
		try:
			hazmat_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=hazmat))
		except:
			hazmat_documents = ""
		try:
			bms_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=bms))
		except:
			bms_documents = ""
		try:
			ers_erm_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ers_erm))
		except:
			ers_erm_documents = ""
		try:
			ecdis_jrc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ecdis_jrc))
		except:
			ecdis_jrc_documents = ""
		try:
			acni_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=acni))
		except:
			acni_documents = ""
		try:
			sso_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=sso))
		except:
			sso_documents = ""
		try:
			ism_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ism))
		except:
			ism_documents = ""		
		# END ATHENIAN TRAINING CERTIFICATES

		application_received_form = ApplicationReceivedForm()

		template = "principals-application-form/%s.html" % (principal)
		title = ("%s application form" % (principal)).upper()
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
		context_dict['sea_service'] = sea_service
		context_dict['history'] = history
		context_dict['reference'] = reference

		context_dict['spouse'] = spouse
		context_dict['vocational'] = vocational
		context_dict['primaryschool'] = primaryschool
		context_dict['stcw_endorsement'] = stcw_endorsement
		context_dict['stcw_certificate'] = stcw_certificate
		context_dict['ntc_license'] = ntc_license
		context_dict['evaluation'] = evaluation

		context_dict['application_received_form'] = application_received_form

		context_dict['sea_service_duration'] = sea_service_duration
		context_dict['rank_sea_service_duration'] = rank_sea_service_duration
		context_dict['dry_vessel_types_duration'] = dry_vessel_types_duration
		context_dict['flag_books'] = flag_books

		# START ATHENIAN TRAINING CERTIFICATES
		context_dict['btoc_documents'] = btoc_documents
		context_dict['atot_documents'] = atot_documents
		context_dict['bt_documents'] = bt_documents
		context_dict['psrc_documents'] = psrc_documents
		context_dict['aff_documents'] = aff_documents
		context_dict['mefa_documents'] = mefa_documents
		context_dict['meca_documents'] = meca_documents
		context_dict['arpa_documents'] = arpa_documents
		context_dict['hazmat_documents'] = hazmat_documents
		context_dict['bms_documents'] = bms_documents
		context_dict['ers_erm_documents'] = ers_erm_documents
		context_dict['ecdis_jrc_documents'] = ecdis_jrc_documents
		context_dict['acni_documents'] = acni_documents
		context_dict['sso_documents'] = sso_documents
		context_dict['ism_documents'] = ism_documents
		# END ATHENIAN TRAINING CERTIFICATES

		return render(request, template, context_dict)
		# return HttpResponse(template)

@login_required()
def manship_form(request, id):
	user_profile = UserProfile.objects.get(id=id)

	template = "manship/index.html"
	context_dict = {}
	context_dict['user_profile'] = user_profile
	return render(request, template, context_dict)

@login_required()
def pdf_complete_form(request, id):
	if id:
		flags_html = ""
		certificates_html = ""

		domain = request.scheme
		domain += "://"
		# returns domain name
		domain += request.META["HTTP_HOST"]
		media = domain+"/media/"
		check = domain+"/static/img/check.jpg"
		uncheck = domain+"/static/img/uncheck.jpg"
		logo = domain+"/static/img/small_logo.png"

		_flags_all = set()
		_flags = set()

		_certificates_all = set()
		_certificates = set()

		td_count_flags_and_certificates_and_per_row = range(3)

		user_profile = UserProfile.objects.get(id=id)
		personal_data = ApplicationFormPersonalData.objects.get(name=id)
		try:
			spouse = ApplicationFormSpouse.objects.get(user=id)
		except:
			spouse = ''
		college = ApplicationFormCollege.objects.filter(user=id)
		highschool = ApplicationFormHighSchool.objects.get(user=id)
		emergency_contact = ApplicationFormEmergencyContact.objects.filter(user=id)
		visa_application = ApplicationFormVisaApplication.objects.get(user=id)
		detained = ApplicationFormDetained.objects.get(user=id)
		disciplinary_action = ApplicationFormDisciplinaryAction.objects.get(user=id)
		charged_offense = ApplicationFormChargedOffense.objects.get(user=id)
		termination = ApplicationFormTermination.objects.get(user=id)
		passport = ApplicationFormPassport.objects.get(user=id)
		sbook = ApplicationFormSbook.objects.get(user=id)
		coc = ApplicationFormCOC.objects.get(user=id)
		license = ApplicationFormLicense.objects.get(user=id)
		src = ApplicationFormSRC.objects.get(user=id)
		goc = ApplicationFormGOC.objects.get(user=id)
		us_visa = ApplicationFormUSVisa.objects.get(user=id)
		schengen_visa = ApplicationFormSchengenVisa.objects.get(user=id)
		yellow_fever = ApplicationFormYellowFever.objects.get(user=id)

		# Variables for application form object
		application_form = ApplicationForm.objects.get(user=id)
		picture = media+str(application_form.picture)
		signature = media+str(application_form.signature)
		# count essay words
		count_words = ''.join(c if c.isalnum() else ' ' for c in application_form.essay.essay).split()
		count_words = len(count_words)
		department = application_form.position_applied.department


		flags = ApplicationFormFlagDocuments.objects.get(user=user_profile)
		certificates_documents = ApplicationFormTrainingCertificateDocuments.objects.get(user=user_profile)

		
		flags = flags.flags.filter()
		for flag in flags:
			_flags.add(flag.flags)
		
		flags_all = Flags.objects.filter(company_standard=1)
		for flags in flags_all:
			_flags_all.add(flags.flags)
		flags_all_by_3 = zip(*(iter(_flags_all),) * 3)
		count_flags_all_by_3 = range(len(flags_all_by_3))
		
		# Script for parsing and returning a multi-dimensioned array of the flags filter in a 3x3 matrix
		for k in count_flags_all_by_3:
			flags_html += '<tr><td style="padding: 0px;"><table border="1">'
			for l in td_count_flags_and_certificates_and_per_row:
				checkbox = get64('', uncheck)
				if flags_all_by_3[k-1][l-1] in _flags:
					checkbox = get64('', check)
				flags_html += '<td style="padding-bottom:5px;"><img src = "%s"> %s</td>' % (checkbox, flags_all_by_3[k-1][l-1])
			flags_html += '</table></td></tr>' 


		certificates = certificates_documents.trainings_certificates.filter(departments=department)
		for certificate in certificates:
			_certificates.add(certificate.trainings_certificates)

		certificates_all = TrainingCertificates.objects.filter()
		for certificates in certificates_all:
			_certificates_all.add(certificates.trainings_certificates)
		certificates_all_by_3 = zip(*(iter(_certificates_all),) * 3)
		count_certificates_all_by_3 = range(len(certificates_all_by_3))

		# Script for parsing and returning a multi-dimensioned array of the certificates filtered with department in a 3x3 matrix
		for k in count_certificates_all_by_3:
			certificates_html += '<tr><td style="padding: 0px;"><table border="1">'
			for l in td_count_flags_and_certificates_and_per_row:
				checkbox = get64('', uncheck)
				if certificates_all_by_3[k-1][l-1] in _certificates:
					checkbox = get64('', check)
				certificates_html += '<td style="padding-bottom:5px;"><img src = "%s"> %s</td>' % (checkbox, certificates_all_by_3[k-1][l-1])
			certificates_html += '</table></td></tr>' 

		if str(personal_data.civil_status) == "Domestic Partner":
			partner = "Live-In"
		else:
			partner = "Spouse"

		template = "application_form/pdf-report-complete.html"
		context_dict = { "appform":application_form, "personaldata":personal_data, "emergency":emergency_contact, "domain":domain, "picture":picture , "signature":signature, "check":check, "uncheck":uncheck, "logo":logo, "count_words":count_words}
		context_dict['user_profile'] = user_profile
		context_dict['spouse'] = spouse
		context_dict['college'] = college
		context_dict['highschool'] = highschool
		context_dict['visa_application'] = visa_application
		context_dict['detained'] = detained
		context_dict['disciplinary_action'] = disciplinary_action
		context_dict['charged_offense'] = charged_offense
		context_dict['termination'] = termination
		context_dict['passport'] = passport
		context_dict['sbook'] = sbook
		context_dict['coc'] = coc
		context_dict['license'] = license
		context_dict['src'] = src
		context_dict['goc'] = goc
		context_dict['us_visa'] = us_visa
		context_dict['schengen_visa'] = schengen_visa
		context_dict['yellow_fever'] = yellow_fever

		# Partner is used for dynamic variable and parameter for spouse or live-in
		context_dict['partner'] = partner

		context_dict['flags_html'] = flags_html
		context_dict['certificates_html'] = certificates_html

		context_dict['department'] = department.department


		return render_to_pdf_response(request, template, context_dict)
		# return render(request, template, context_dict)
	else:
		raise Http404("System Error.")


@login_required
def pdf_fleet_application_form(request, principal, id):
	if id:
		from application_form.models import ApplicationForm
		
		domain = request.scheme
		domain += "://"
		# returns domain name
		domain += request.META["HTTP_HOST"]
		media = domain+"/media/"
		check = domain+"/static/img/check.jpg"
		uncheck = domain+"/static/img/uncheck.jpg"
		logo = domain+"/static/img/pdf-logos/%s.png" % principal

		user_profile = UserProfile.objects.get(id=id)
		mariners_profile = MarinersProfile.objects.get(user=user_profile)
		application_form = ApplicationForm.objects.get(user=user_profile)
		picture = media+str(application_form.picture)
		signature = media+str(application_form.signature)
		personal_data = PersonalData.objects.get(name=id)
		current_address = CurrentAddress.objects.get(personaldata=personal_data.id)
		permanent_address = PermanentAddress.objects.get(personaldata=personal_data.id)
		principal_object = Principal.objects.get(principal__iexact=principal)
		principal_flags = principal_object.flags_standard.all()
		flag_document = FlagDocuments.objects.get(user=user_profile)

		# Soon to be fixed
		flag_document_instance = FlagDocuments.objects.get(user=user_profile)

		flag_documents = FlagDocumentsDetailed.objects.filter(flags_documents=flag_document).filter(flags__in=principal_flags)
		flag_documents_valid = FlagDocumentsDetailed.objects.filter(flags_documents=flag_document).filter(~Q(sbook_number=None))
		principal_trainings_certificate = principal_object.trainings_certificate_standard.all()
		trainings_certificate_document = TrainingCertificateDocuments.objects.get(user=user_profile)
		trainings_certificate_documents = TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificate_documents=trainings_certificate_document).filter(trainings_certificates__in=principal_trainings_certificate)
		
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
		emergency_contact = EmergencyContact.objects.filter(user=id).order_by('-id')[0]
		dependents = Dependents.objects.filter(user=id)
		land_employment = LandEmployment.objects.filter(user=id)
		beneficiary = Beneficiary.objects.filter(user=id)
		allotee = Allotee.objects.filter(user=id)
		sea_service = SeaService.objects.filter(user=id)
		history = MarinerStatusHistory.objects.filter(user=id).order_by('-id')
		try:
			current_history = history[0]
		except:
			current_history = ""
		reference = Reference.objects.filter(user=id)

		# Script to get the flags issuing authority of the other seaman's book
		flag_books = []
		for flag_document in flag_documents_valid:
			flag_books.append(flag_document.flags.flags)
		flag_books = ', '.join(flag_books)

		# Script to get the duration of the current rank via year with conditional of days if less than
		# Used for Ionic application form
		rank_sea_service_duration = []
		rank_sea_service = sea_service.filter(rank=mariners_profile.position)
		for rank_sea_services in rank_sea_service:
			duration = rank_sea_services.date_left - rank_sea_services.date_joined
			rank_sea_service_duration.append(duration.days)
		rank_sea_service_duration = sum(rank_sea_service_duration)
		rank_sea_duration = rank_sea_service_duration / 365
		rank_sea_duration_days_remainder = rank_sea_service_duration % 365
		if rank_sea_duration:
			if rank_sea_duration_days_remainder:
				rank_sea_duration_days_remainder = "and %s days" % rank_sea_duration_days_remainder
			else:
				rank_sea_duration_days_remainder = ""
			rank_sea_service_duration = "%s year %s" % (rank_sea_duration, rank_sea_duration_days_remainder)
		else:
			rank_sea_service_duration = "%s days" % rank_sea_service_duration

		sea_service_duration = []
		for sea_services in sea_service:
			duration = sea_services.date_left - sea_services.date_joined
			sea_service_duration.append(duration.days)
		sea_service_duration = sum(sea_service_duration)
		sea_duration = sea_service_duration / 365
		sea_duration_days_remainder = sea_service_duration % 365
		if sea_duration:
			if sea_duration_days_remainder:
				sea_duration_days_remainder = "and %s days" % sea_duration_days_remainder
			else:
				sea_duration_days_remainder = ""
			sea_service_duration = "%s year %s" % (sea_duration, sea_duration_days_remainder)
		else:
			sea_service_duration = "%s days" % sea_service_duration

		# Script to get the duration of in dry cargo carriers via year with conditional of days if less than
		dry_vessel_types = VesselType.objects.filter(Q(vessel_type__iexact='Bulk') | Q(vessel_type__iexact='Container') | Q(vessel_type__iexact='Log Bulk'))
		dry_vessel_types_duration = []
		dry_vessel_type_sea_service = sea_service.filter(vessel_type__in=dry_vessel_types)

		for dry_vessel_type_sea_services in dry_vessel_type_sea_service:
			duration = dry_vessel_type_sea_services.date_left - dry_vessel_type_sea_services.date_joined
			dry_vessel_types_duration.append(duration.days)
		dry_vessel_types_duration = sum(dry_vessel_types_duration)
		dry_vessel_duration = dry_vessel_types_duration / 365
		dry_vessel_types_duration_days_remainder = dry_vessel_types_duration % 365
		if dry_vessel_duration:
			if dry_vessel_types_duration_days_remainder:
				dry_vessel_types_duration_days_remainder = "and %s days" % dry_vessel_types_duration_days_remainder
			else:
				dry_vessel_types_duration_days_remainder = ""
			dry_vessel_types_duration = "%s year %s" % (dry_vessel_duration, dry_vessel_types_duration_days_remainder)
		else:
			dry_vessel_types_duration = "%s days" % dry_vessel_types_duration

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


		# START INDIVIDUAL FLAGS
		marshall_islands = Flags.objects.get(flags='Marshall Islands')
		liberia = Flags.objects.get(flags='Liberia')
		bahamas = Flags.objects.get(flags='Bahamas')

		try:
			marshall_islands_documents = FlagDocumentsDetailed.objects.get(Q(flags_documents=flag_document_instance) & Q(flags=marshall_islands))
		except:
			marshall_islands_documents = ""
		try:
			liberia_documents = FlagDocumentsDetailed.objects.get(Q(flags_documents=flag_document_instance) & Q(flags=liberia))
		except:
			liberia_documents = ""
		try:
			bahamas_documents = FlagDocumentsDetailed.objects.get(Q(flags_documents=flag_document_instance) & Q(flags=bahamas))
		except:
			bahamas_documents = ""
		# END INDIVIDUAL FLAGS

		# START ATHENIAN TRAINING CERTIFICATES
		btoc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BTOC')
		atot = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ATOT')
		bt = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BT')
		psrc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='PSRC')
		pfrc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='PFRC')
		aff = TrainingCertificates.objects.get(trainings_certificates_abbreviation='AFF')
		mefa = TrainingCertificates.objects.get(trainings_certificates_abbreviation='MEFA')
		meca = TrainingCertificates.objects.get(trainings_certificates_abbreviation='MECA')
		arpa = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ARPA')
		hazmat = TrainingCertificates.objects.get(trainings_certificates_abbreviation='HAZMAT')
		bms = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BMS')
		ers_erm = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ERS / ERM')
		ecdis_jrc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ECDIS JRC')
		ecdis_furuno = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ECDIS Furuno')
		ecdis = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ECDIS')
		acni = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ACNI')
		sso = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SSO')
		ism = TrainingCertificates.objects.get(trainings_certificates_abbreviation='ISM')
		btm = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BTM')
		brm = TrainingCertificates.objects.get(trainings_certificates_abbreviation='BRM')
		gmdss = TrainingCertificates.objects.get(trainings_certificates_abbreviation='GMDSS')
		marpol = TrainingCertificates.objects.get(trainings_certificates_abbreviation='MARPOL I-VI')
		sh = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SH')
		soc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SOC')
		dwk_ewk = TrainingCertificates.objects.get(trainings_certificates_abbreviation='DWK/EWK')
		rsc = TrainingCertificates.objects.get(trainings_certificates_abbreviation='RSC')
		scs_nc_i = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SCSNC I')
		scs_nc_ii = TrainingCertificates.objects.get(trainings_certificates_abbreviation='SCSNC II')


		try:
			print trainings_certificate_document
			btoc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=btoc))
		except:
			btoc_documents = ""
		try:
			atot_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=atot))
		except:
			atot_documents = ""
		try:
			bt_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=bt))
		except:
			bt_documents = ""
		try:
			psrc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=psrc))
		except:
			psrc_documents = ""
		try:
			pfrc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=pfrc))
		except:
			pfrc_documents = ""
		try:
			aff_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=aff))
		except:
			aff_documents = ""
		try:
			mefa_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=mefa))
		except:
			mefa_documents = ""
		try:
			meca_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=meca))
		except:
			meca_documents = ""
		try:
			arpa_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=arpa))
		except:
			arpa_documents = ""
		try:
			hazmat_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=hazmat))
		except:
			hazmat_documents = ""
		try:
			bms_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=bms))
		except:
			bms_documents = ""
		try:
			ers_erm_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ers_erm))
		except:
			ers_erm_documents = ""
		try:
			ecdis_jrc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ecdis_jrc))
		except:
			ecdis_jrc_documents = ""
		try:
			ecdis_furuno_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ecdis_furuno))
		except:
			ecdis_furuno_documents = ""
		try:
			ecdis_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ecdis))
		except:
			ecdis_documents = ""
		try:
			acni_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=acni))
		except:
			acni_documents = ""
		try:
			sso_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=sso))
		except:
			sso_documents = ""
		try:
			ism_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=ism))
		except:
			ism_documents = ""
		try:
			btm_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=btm))
		except:
			btm_documents = ""
		try:
			brm_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=brm))
		except:
			brm_documents = ""
		try:
			gmdss_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=gmdss))
		except:
			gmdss_documents = ""
		try:
			marpol_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=marpol))
		except:
			marpol_documents = ""
		try:
			sh_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=sh))
		except:
			sh_documents = ""
		try:
			soc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=soc))
		except:
			soc_documents = ""
		try:
			dwk_ewk_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=dwk_ewk))
		except:
			dwk_ewk_documents = ""
		try:
			rsc_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=rsc))
		except:
			rsc_documents = ""
		try:
			scs_nc_i_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=scs_nc_i))
		except:
			scs_nc_i_documents = ""
		try:
			scs_nc_ii_documents = TrainingCertificateDocumentsDetailed.objects.get(Q(trainings_certificate_documents=trainings_certificate_document) & Q(trainings_certificates=scs_nc_ii))
		except:
			scs_nc_ii_documents = ""
		# END ATHENIAN TRAINING CERTIFICATES

		application_received_form = ApplicationReceivedForm()

		template = "principals-application-form/pdf/%s.html" % (principal)
		title = ("%s application form" % (principal)).upper()
		context_dict = {"domain":domain, "picture":picture , "signature":signature, "check":check, "uncheck":uncheck, "logo":logo}
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
		context_dict['sea_service'] = sea_service
		context_dict['history'] = history
		context_dict['reference'] = reference

		context_dict['spouse'] = spouse
		context_dict['vocational'] = vocational
		context_dict['primaryschool'] = primaryschool
		context_dict['stcw_endorsement'] = stcw_endorsement
		context_dict['stcw_certificate'] = stcw_certificate
		context_dict['ntc_license'] = ntc_license
		context_dict['evaluation'] = evaluation

		context_dict['application_received_form'] = application_received_form

		context_dict['sea_service_duration'] = sea_service_duration
		context_dict['rank_sea_service_duration'] = rank_sea_service_duration
		context_dict['dry_vessel_types_duration'] = dry_vessel_types_duration
		context_dict['flag_books'] = flag_books

		# START ATHENIAN TRAINING CERTIFICATES
		context_dict['btoc_documents'] = btoc_documents
		context_dict['atot_documents'] = atot_documents
		context_dict['bt_documents'] = bt_documents
		context_dict['psrc_documents'] = psrc_documents
		context_dict['pfrc_documents'] = pfrc_documents
		context_dict['aff_documents'] = aff_documents
		context_dict['mefa_documents'] = mefa_documents
		context_dict['meca_documents'] = meca_documents
		context_dict['arpa_documents'] = arpa_documents
		context_dict['hazmat_documents'] = hazmat_documents
		context_dict['bms_documents'] = bms_documents
		context_dict['ers_erm_documents'] = ers_erm_documents
		context_dict['ecdis_jrc_documents'] = ecdis_jrc_documents
		context_dict['ecdis_furuno_documents'] = ecdis_furuno_documents
		context_dict['ecdis_documents'] = ecdis_documents
		context_dict['acni_documents'] = acni_documents
		context_dict['sso_documents'] = sso_documents
		context_dict['ism_documents'] = ism_documents
		context_dict['btm_documents'] = btm_documents
		context_dict['brm_documents'] = brm_documents
		context_dict['gmdss_documents'] = gmdss_documents
		context_dict['marpol_documents'] = marpol_documents
		context_dict['sh_documents'] = sh_documents
		context_dict['soc_documents'] = soc_documents
		context_dict['dwk_ewk_documents'] = dwk_ewk_documents
		context_dict['rsc_documents'] = rsc_documents
		context_dict['scs_nc_i_documents'] = scs_nc_i_documents
		context_dict['scs_nc_ii_documents'] = scs_nc_ii_documents
		
		# END ATHENIAN TRAINING CERTIFICATES
		# START INDIVIDUAL FLAGS
		context_dict['marshall_islands_documents'] = marshall_islands_documents
		context_dict['liberia_documents'] = liberia_documents
		context_dict['bahamas_documents'] = bahamas_documents
		# END INDIVIDUAL FLAGS

		return render_to_pdf_response(request, template, context_dict)
		# return HttpResponse(template)