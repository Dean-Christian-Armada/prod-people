from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q

from easy_pdf.rendering import render_to_pdf_response

from mariners_profile.models import *
from mariners_profile.forms import *

from application_form.models import *
from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm
from application_form.templatetags.pdf_image import get64

from . forms import ApplicantsDataTables, PrincipalSelectForm, DynamicPrincipalVesselTypeSelectForm

import sys, urllib, cStringIO, base64

def xyz(request, method):
	if method == "POST": request_method = request.POST
	elif method == "GET": request_method = request.GET

	# returns full url
	url = request.scheme
	url += "://"
	url += request.META['HTTP_HOST']
	url += request.get_full_path()

	params = "?"

	for x in request_method:
		if x != 'csrfmiddlewaretoken' and x != 'submit' and x != 'page':
			if request_method[x]:
				params += "&"+x+"="+request_method[x]

	return (params, url)

@login_required()
def index(request):
	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=0)
	search = ApplicantsDataTables
	# Sets are used for dynamic value filtering
	age = set()
	vessel_type = set()
	rank = set()
	params = {}
	params2 = {}

	template = "application-profile/index.html"
	context_dict = {"title": "APPLICANT PROFILES"}

	choice_visa = ''

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		# if 'age' in request.GET:
		# 	params['age'] = request.GET['age']
		if 'vessel_type' in request.GET:
			_vessel_type = VesselType.objects.get(vessel_type__iexact=request.GET['vessel_type'])
			params['preferred_vessel_type'] = _vessel_type
		if 'rank' in request.GET:
			_rank = Rank.objects.get(rank__iexact=request.GET['rank'])
			params2['position'] = _rank
		if 'us_visa' in request.GET:
			us_choice_visa = request.GET['us_visa']
			# To enable False boolean on the variable
			us_choice_visa = us_choice_visa in ['YES']
			mariners_profile = USVisa.objects.filter(user__in=mariners_profile.values('user')).filter(us_visa=us_choice_visa)
			us_choice_visa = int(mariners_profile.values('us_visa').distinct()[0]['us_visa'])
		if 'schengen_visa' in request.GET:
			schengen_choice_visa = request.GET['schengen_visa']
			# To enable False boolean on the variable
			schengen_choice_visa = schengen_choice_visa in ['YES']
			mariners_profile = SchengenVisa.objects.filter(user__in=mariners_profile.values('user')).filter(schengen_visa=schengen_choice_visa)
			schengen_choice_visa = int(mariners_profile.values('schengen_visa').distinct()[0]['schengen_visa'])

	if request.method == 'GET' and 'search' in request.GET:
		try:
			searches = request.GET['search']
			searches = searches.partition(' ')[0]
			x = UserProfile.objects.filter(Q(first_name__icontains=searches) | Q(last_name__icontains=searches) | Q(middle_name__icontains=searches))
			mariners_profile = MarinersProfile.objects.filter(user__in=x)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

	
	personal_data = PersonalData.objects.filter(name__in=mariners_profile.values('user')).filter(**params).order_by('-id')
	mariners_profile = MarinersProfile.objects.filter(user__in=personal_data.values('name')).filter(**params2).order_by('-id')
	
	# US Visa Dynamic Filtering
	us_visa_choices_values = USVisa.objects.filter(user__in=mariners_profile.values('user')).values_list('us_visa', flat=True).distinct().order_by('us_visa')
	us_visa_choices = us_visa_choices_values
	us_visa = USVisa.objects.filter(user__in=mariners_profile.values('user')).order_by('-id')

	# Schengen Visa Dynamic Filtering
	schengen_visa_choices_values = SchengenVisa.objects.filter(user__in=mariners_profile.values('user')).values_list('schengen_visa', flat=True).distinct().order_by('schengen_visa')
	schengen_visa_choices = schengen_visa_choices_values
	schengen_visa = SchengenVisa.objects.filter(user__in=mariners_profile.values('user')).order_by('-id')


	# Zipped is used for the table data
	zipped_data = zip(mariners_profile, personal_data, us_visa, schengen_visa)

	for x, y, z, xx in zipped_data:
		age.add(y.age)
		vessel_type.add(y.preferred_vessel_type)
		rank.add(x.position)

	
	# [0] is put to break the instance into the unicode value
	print age
	try:
		context_dict['personaldata'] = personal_data
		context_dict['mariners_profile'] = mariners_profile
		context_dict['name'] = name
		context_dict['zipped_data'] = zipped_data
		context_dict['search'] = search
		context_dict['age'] = sorted(age)
		context_dict['vessel_type'] = sorted(vessel_type)
		context_dict['rank'] = sorted(rank)
	except:
		print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

	# used for dynamic choices in us visa
	context_dict['us_visa'] = us_visa_choices

	# used for dynamic choices in us visa
	context_dict['schengen_visa'] = schengen_visa_choices
	

	return render(request, template, context_dict)


@login_required()
def profile(request, id):
	if id:
		user_profile = UserProfile.objects.get(id=id)
		personal_data = ApplicationFormPersonalData.objects.get(name=id)
		num_extra = 0 # Used in evaluation for controlling inline formset
		principal_select_form = PrincipalSelectForm()
		today = date.today()

		try:
			spouse = ApplicationFormSpouse.objects.get(user=id)
			spouse_form = SpouseForm(request.POST or None, instance=spouse)
		except:
			spouse = ''
			spouse_form = SpouseForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			vocational = Vocational.objects.get(user=id)
			vocational_form = VocationalForm(request.POST or None, instance=vocational, initial={'vocational':vocational.vocational})
		except:
			vocational = ''
			vocational_form = VocationalForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			primaryschool = PrimarySchool.objects.get(user=id)
			primaryschool_form = PrimarySchoolForm(request.POST or None, instance=primaryschool, initial={'primaryschool':primaryschool.primaryschool})
		except:
			primaryschool = ''
			primaryschool_form = PrimarySchoolForm(request.POST or None, initial={'user': personal_data.name} )
		try:
			reference = Reference.objects.filter(user=id)
			# print len(reference)
			if len(reference) == 1:
				num_extra = 1
			elif len(reference) < 1:
				num_extra = 2
			elif len(reference) > 1:
				num_extra = 0
			ReferenceFormSet = inlineformset_factory(UserProfile, Reference, fk_name='user', extra=num_extra, can_delete=True, form=ReferenceForm )
			# reference_form = ReferenceFormSet(request.POST or None, )
			reference_form = ReferenceFormSet(request.POST or None, instance=user_profile )

		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])
		try:
			evaluation = Evaluation.objects.get(user=id)
			evaluation_form = EvaluationForm(request.POST or None, instance=evaluation, initial={'evaluation':evaluation.evaluation})
		except:
			evaluation = ''
			evaluation_form = EvaluationForm(request.POST or None, initial={'user': personal_data.name} )

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
		sea_service = ApplicationFormSeaService.objects.filter(user=id).order_by('-date_left')
		mariners_profile = MarinersProfile.objects.get(user=id)
		department = mariners_profile.position.department
		application_form = ApplicationForm.objects.get(user=id)

		# Queries out the list of flags
		try:
			flag_documents = ApplicationFormFlagDocuments.objects.get(user=user_profile)
			flag_list = []
			flags = flag_documents.flags.filter()
			for flag in flags:
				flag_list.append(flag.id)
			flags = {'flags': flag_list}
			flags = FlagForm(initial=flags)
		except:
			flags = FlagForm()

		training_certificate_documents = ApplicationFormTrainingCertificateDocuments.objects.get(user=user_profile)
		training_certificate_list = []
		training_certificates = training_certificate_documents.trainings_certificates.filter()
		for training_certificate in training_certificates:
			training_certificate_list.append(training_certificate.id)
		training_certificates = {'trainings_certificates': training_certificate_list}
		trainings_certificates = DynamicTrainingCertificateForm(mariners_profile.position_id, initial=training_certificates)

		if vocational_form.is_valid() and primaryschool_form.is_valid() and reference_form.is_valid() and evaluation_form.is_valid():
			vocational_form.save()
			primaryschool_form.save()
			evaluation_form.save()
			for reference in reference_form:
				reference.save()
			return HttpResponseRedirect('')
		else:
			print vocational_form.errors
			print primaryschool_form.errors
			# Used for management form error in status request
			try:
				print reference_form.errors
			except:
				pass
			print evaluation_form.errors

		if request.GET and 'status' in request.GET:
			print request.GET
			_status = request.GET['status']
			_status = Status.objects.get(id=_status)
			application_form.status = _status
			application_form.save()
			mariners_profile.status = 1
			mariners_profile.date_hired = today
			mariners_profile.save()
			if str(application_form.status) == 'Passed':
				return HttpResponseRedirect('/mariners-profile/'+id)

		status = StatusForm(initial={'status':str(application_form.status.id)})
		
		# Script used to count essay words
		count_words = ''.join(c if c.isalnum() else ' ' for c in application_form.essay.essay).split()
		count_words = len(count_words)

		template = "application-profile/profile.html"

		context_dict = {}
		context_dict['user_profile'] = user_profile
		context_dict['personal_data'] = personal_data
		context_dict['spouse'] = spouse
		context_dict['college'] = college
		context_dict['highschool'] = highschool
		context_dict['emergency_contact'] = emergency_contact
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
		
		context_dict['vocational_form'] = vocational_form
		context_dict['primaryschool_form'] = primaryschool_form
		context_dict['evaluation_form'] = evaluation_form
		context_dict['reference_form'] = reference_form
		context_dict['principal_select_form'] = principal_select_form

		context_dict['title'] = "Applicants Profile - "+str(personal_data).upper()
		context_dict['sea_service'] = sea_service
		context_dict['application_form'] = application_form
		context_dict['mariners_profile'] = mariners_profile
		context_dict['department'] = department.department

		context_dict['flags'] = flags
		context_dict['trainings_certificates'] = trainings_certificates
		context_dict['status'] = status

		context_dict['count_words'] = count_words

		return render(request, template, context_dict)

@login_required()
def pdf(request, id):
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

		template = "application_form/pdf-report.html"
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
def pdf_sea_services(request, id):
	if id:
		sea_service = ApplicationFormSeaService.objects.filter(user=id)
		sea_service_count = len(sea_service)
		template = "application_form/pdf-report-sea-service.html"
		context_dict = {}
		context_dict['sea_service'] = sea_service
		context_dict['sea_service_count'] = sea_service_count
		return render_to_pdf_response(request, template, context_dict)
	else:
		raise Http404("System Error.")

@login_required
def dynamic_vessel_types_via_principal(request):
	principal = request.GET['principal']
	if principal:
		pass
		dynamic_principal_vessel_type_form = DynamicPrincipalVesselTypeSelectForm(principal)
	else:
		dynamic_principal_vessel_type_form = ""

	template = "application-profile/vessel_types.html"
	context_dict = { "dynamic_principal_vessel_type_form": dynamic_principal_vessel_type_form }
	return render(request, template, context_dict)