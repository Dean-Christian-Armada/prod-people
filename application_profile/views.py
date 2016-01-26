try:
    from people.asynchronous_mail import send_mail
except:
    from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.formsets import formset_factory
from django.template.loader import render_to_string, get_template
from django.template import Context, Template, RequestContext
from django.db.models import Q
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings

# from easy_pdf.rendering import render_to_pdf_response

from mariners_profile.models import *
from mariners_profile.forms import *

from application_form.models import *
from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm
from application_form.templatetags.pdf_image import get64

from notifications.models import *
from application_profile.forms import ApplicantsDataTables, PrincipalSelectForm, DynamicPrincipalVesselTypeSelectForm
from globals_declarations.variables import now, today
from globals_declarations.methods import crew_retrieve_manipulation

# from wkhtmltopdf.views import PDFTemplateView
# from markdown import markdown
# from weasyprint import HTML, CSS

import sys, urllib, base64

@login_required()
def index(request):
	from globals_declarations.variables import crew_on_table, per_page_list # global declaration on pages
	param_connector = "?"
	count = 0

	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=0)
	search = ApplicantsDataTables
	# START Sets are used for dynamic value filtering
	vessel_type = set()
	rank = set()
	barangay = set()
	municipality = set()
	status_choices = set()
	num = set()
	# END Sets are used for dynamic value filtering
	params = {} # Used for doing the primary filters
	params2 = {} # Used for extra filters

	if request.method == 'POST':
		# used for multiple returns
		params, url = crew_retrieve_manipulation(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		# manipulates number of crew displayed 
		if 'crew_on_table' in request.GET:
			_crew_on_table = request.GET['crew_on_table']
			crew_on_table = int(_crew_on_table)
			remove = per_page_list.index(crew_on_table)
			per_page_list.pop(remove)
			per_page_list.insert(0, crew_on_table)
		
		if 'vessel_type' in request.GET:
			_vessel_type = VesselType.objects.get(vessel_type__iexact=request.GET['vessel_type'])
			params['preferred_vessel_type'] = _vessel_type
		if 'rank' in request.GET:
			_rank = Rank.objects.get(rank__iexact=request.GET['rank'])
			params2['position'] = _rank
		if 'municipality' in request.GET:
			_municipality = Municipality.objects.get(municipality__iexact=request.GET['municipality'])
			_municipality = Zip.objects.filter(municipality=_municipality)
			_municipality = CurrentAddress.objects.filter(current_zip__in=_municipality)
			params['current_address__in'] = _municipality
		if 'us_visa' in request.GET:
			us_choice_visa = request.GET['us_visa']
			# To enable False boolean on the variable
			us_choice_visa = us_choice_visa in ['YES']
			mariners_profile = USVisa.objects.filter(user__in=mariners_profile.values('user')).filter(us_visa=us_choice_visa)

		if 'schengen_visa' in request.GET:
			schengen_choice_visa = request.GET['schengen_visa']
			# To enable False boolean on the variable
			schengen_choice_visa = schengen_choice_visa in ['YES']
			mariners_profile = SchengenVisa.objects.filter(user__in=mariners_profile.values('user')).filter(schengen_visa=schengen_choice_visa)

		if 'status' in request.GET:
			_status = Status.objects.get(status__iexact=request.GET['status'])
			mariners_profile = ApplicationForm.objects.filter(user__in=mariners_profile.values('user')).filter(status=_status)

	if request.method == 'GET' and 'search' in request.GET:
		try:
			searches = request.GET['search']
			searches = searches.partition(' ')[0]
			x = UserProfile.objects.filter(Q(first_name__icontains=searches) | Q(last_name__icontains=searches) | Q(middle_name__icontains=searches))
			mariners_profile = MarinersProfile.objects.filter(user__in=x)
		except:
			print ("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

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

	# Applicant Status Dynamic Filtering
	status = ApplicationForm.objects.filter(user__in=mariners_profile.values('user')).order_by('-id')

	# Zipped is used for the table data
	zipped_data = zip(mariners_profile, personal_data, us_visa, schengen_visa, status)

	for x, y, z, xx, zz in zipped_data:
		count += 1
		vessel_type.add(y.preferred_vessel_type.vessel_type)
		municipality.add(y.current_address.current_zip.municipality.municipality)
		rank.add(x.position.rank)
		status_choices.add(zz.status)
		num.add(count)

	# START Script to paginate the query and retrieve all the parameters to the URL
	# Script to retrieve all the parameters to a variable
	params, url = crew_retrieve_manipulation(request, "GET")

	# Script to paginate the query
	paginator = Paginator(mariners_profile, crew_on_table)

	if 'page' in request.GET:
		page = int(request.GET.get('page'))
	else:
		page=1

	if 'page' not in request.GET:
		params = params.replace('?', '')

	try:
		mariners_profile = paginator.page(page)
	except PageNotAnInteger:
		mariners_profile = paginator.page(1)
	except EmptyPage:
		mariners_profile = paginator.page(paginator.num_pages)

	try:
		next_next_page = mariners_profile.next_page_number()+1
		next_next_page_try = paginator.page(next_next_page)
	except:
		print ("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
		next_next_page = ''
	try:
		previous_previous_page = mariners_profile.previous_page_number()-1
		previous_previous_page_try = paginator.page(previous_previous_page)
	except:
		print ("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
		previous_previous_page = ''
	# END Script to paginate the query and retrieve all the parameters to the URL

	# Zipped is used for the table data
	zipped_data = zip(mariners_profile, personal_data, us_visa, schengen_visa, sorted(num, reverse=True))

	template = "application-profile/index.html"

	context_dict = {"title": "MANSHIP Applicants"}
	context_dict['personaldata'] = personal_data
	context_dict['mariners_profile'] = mariners_profile
	context_dict['name'] = name
	context_dict['user'] = user
	context_dict['zipped_data'] = zipped_data
	context_dict['search'] = search
	context_dict['vessel_type'] = sorted(vessel_type)
	context_dict['rank'] = sorted(rank)
	context_dict['municipality'] = sorted(municipality)

	# used for dynamic choices in us visa and schengen visa
	context_dict['us_visa'] = us_visa_choices
	context_dict['schengen_visa'] = schengen_visa_choices

	# used for dynamic choices in us visa
	context_dict['status'] = status_choices

	# used to retrieve all the parameters on the page links
	context_dict['params'] = params
	context_dict['param_connector'] = param_connector

	context_dict['per_page_list'] = per_page_list
	context_dict['next_next_page'] = next_next_page
	context_dict['previous_previous_page'] = previous_previous_page
	
	return render(request, template, context_dict)

@login_required()
def profile(request, slug):
	if slug:
		domain_url = request.scheme
		domain_url += "://"
		domain_url += request.META['HTTP_HOST']

		try:
			user_profile = UserProfile.objects.get(slug=slug)
		except:
			template = "errors/profiles.html"
			context_dict = {'profile':'applicant', 'title':"Applicant Doesn't Exist"}
			return render(request, template, context_dict)
		current_user = UserProfile.objects.get(user=request.user)
		id = user_profile.id
		personal_data = ApplicationFormPersonalData.objects.get(name=id)
		num_extra = 0 # Used in evaluation for controlling inline formset
		principal_select_form = PrincipalSelectForm()

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
			if len(reference) == 1:
				num_extra = 1
			elif len(reference) < 1:
				num_extra = 2
			elif len(reference) > 1:
				num_extra = 0
			ReferenceFormSet = inlineformset_factory(UserProfile, Reference, fk_name='user', extra=num_extra, can_delete=True, form=ReferenceForm )
			reference_form = ReferenceFormSet(request.POST or None, instance=user_profile )
		except:
			print ("%s - %s at line: %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
		
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
		sea_service = ApplicationFormSeaService.objects.filter(user=id)
		mariners_profile = MarinersProfile.objects.get(user=id)
		department = mariners_profile.position.department
		application_form = ApplicationForm.objects.get(user=id)
		try:
			application_form_last_status = ApplicationFormStatusLog.objects.filter(application_form=application_form)[0]
		except:
			application_form_last_status = ''
		current_status = application_form.status
		status_listed = Status.objects.filter(listed=True)
		status = StatusForm(initial={'status':str(application_form.status.id)})

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
			print (vocational_form.errors)
			print (primaryschool_form.errors)
			# Used for management form error in status request
			try:
				print (reference_form.errors)
			except:
				pass
			print (evaluation_form.errors)

		# START, script to change the status and code 
		if request.GET and 'status' in request.GET:
			_status = request.GET['status']
			_status = Status.objects.get(id=_status)
			application_form.status = _status
			# mariners_profile.status_last_modified = now
			mariners_profile.save()
			application_form.save()
			ApplicationFormStatusLog.objects.create(application_form=application_form, user=current_user, old_status=current_status, new_status=_status.status)

			if str(application_form.status).upper() == 'PASSED' or str(application_form.status).upper() == 'PASS':
				#  START, Script to update the code
				# [0] is used to make it a string
				first_name = user_profile.first_name[0].lower()
				middle_name = user_profile.middle_name[0].lower()
				last_name = user_profile.last_name[0].lower()
				letter = "a"
				first_three_letter_name = "%s%s%s" % (last_name, first_name, middle_name)
				code = UserProfile.objects.filter(code__istartswith=first_three_letter_name)
				initial_code = first_three_letter_name+letter
				codes = [x.code for x in code]
				while initial_code in codes:
				 letter = chr(ord(letter)+1)
				 initial_code = first_three_letter_name[:3]+letter
				 initial_code
				user_profile.code=initial_code
				user_profile.save()
				#  END, Script to update the code
				mariners_profile.status = 1
				mariners_profile.date_hired = today
				mariners_profile.save()
				# mariner_status_comment = "New Mariner in the Pool"
				# _mariner_status_comment = MarinerStatusComment.objects.get_or_create(mariner_status_comment=mariner_status_comment)
				# if _mariner_status_comment:
				# 	_mariner_status_comment = MarinerStatusComment.objects.get(mariner_status_comment=mariner_status_comment)
				# mariners_history = MarinerStatusHistory.objects.get_or_create(user=user_profile, since=today, mariner_status_comment=_mariner_status_comment)
				mariners_history = MarinerStatusHistory.objects.get_or_create(user=user_profile, since=today)
				notification_status = NotificationStatus.objects.get(status='Mariner Passed')
				notification = Notification.objects.create(status=notification_status, user=user_profile)
				notification = Notification.objects.filter(status=notification_status, user=user_profile)[0]
				user_notification_receivers = UserNotificationReceivers.objects.get(status=notification.status)
				receivers = user_notification_receivers.receiver.all()
				
				# START SEND EMAIL SCRIPT
				email_notification = EmailNotification.objects.get(notification_status=notification_status)
				mariners_count = MarinersProfile.objects.filter(status=1).count()

				# START HTML rendering from the database to email
				status_template = Template(email_notification.notification_status.label)
				status = Context({})
				status = status_template.render(status)
				greetings_template = Template(email_notification.greetings)
				greetings = Context({'count': mariners_count, 'name': user_profile, 'link': "%s%s%s" % (domain_url, email_notification.notification_status.base_url.base_url, user_profile.slug) })
				greetings = greetings_template.render(greetings)
				message_template = Template(email_notification.message)
				message = Context({'code':user_profile.code, 'mobile':personal_data.prefix_mobile_1(), 'landline':personal_data.landline_1, 'rank_duration':mariners_profile.rank_sea_service_duration(), 'position':mariners_profile.position, 'application_source':application_form.application_source, 'us_visa':us_visa.determine_us_visa(), 'schengen_visa':schengen_visa.determine_schengen_visa(), 'vessel_type':personal_data.preferred_vessel_type, 'age':personal_data.age()})
				message = message_template.render(message)
				
				email_data = {}
				email_data['email_title'] = status
				email_data['email_greetings'] = greetings
				email_data['email_body'] = message
				# email_data serves as a dictionary with key value pairs to be used to store data fetched from the database
				msg_html = render_to_string('email-templates/notifications.html', email_data)
				# END HTML rendering from the database to email

				email_receievers = ['adgc@manship.com']
				
				for x in receivers:
					NotificationHistory.objects.create(notification=notification, received=x)
					email_receievers.append(x.departmental_email)
					email_receievers.append(x.user.email)
				# SEND EMAIL SYNTAX
				# send_mail(email_notification.notification_status.label, '', settings.EMAIL_HOST_USER, email_receievers, fail_silently=False, html_message=msg_html)
				# END SEND EMAIL SCRIPT
				return HttpResponseRedirect('/mariners-profile/'+user_profile.slug)
			else:
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		# END, script to change the status and code 

		template = "application-profile/profile.html"

		context_dict = {}
		context_dict['title'] = "Applicant's Profile - "+str(personal_data).upper()
		context_dict['user_profile'] = user_profile
		context_dict['user'] = current_user
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
		context_dict['sea_service'] = sea_service
		context_dict['sea_service_num_label'] = sea_service.count()
		context_dict['application_form'] = application_form
		context_dict['application_form_last_status'] = application_form_last_status
		context_dict['mariners_profile'] = mariners_profile
		context_dict['department'] = department.department
		context_dict['flags'] = flags
		context_dict['trainings_certificates'] = trainings_certificates
		context_dict['status'] = status
		context_dict['status_listed'] = status_listed
		context_dict['count_words'] = application_form.essay_count()

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

		department = application_form.position_applied.department

		flags = ApplicationFormFlagDocuments.objects.get(user=user_profile)
		certificates_documents = ApplicationFormTrainingCertificateDocuments.objects.get(user=user_profile)
		
		flags = flags.flags.filter()
		for flag in flags:
			_flags.add(flag.flags)
		
		flags_all = Flags.objects.filter(company_standard=1)
		for flags in flags_all:
			_flags_all.add(flags.flags)
		flags_all_by_3 = list(zip(*(iter(_flags_all),) * 3))
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

		certificates_all = TrainingCertificates.objects.filter(departments=department)
		for certificates in certificates_all:
			_certificates_all.add(certificates.trainings_certificates)
		certificates_all_by_3 = list(zip(*(iter(_certificates_all),) * 3))
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

		template = get_template('application_form/pdf-report.html')
		context_dict = { "appform":application_form, "personaldata":personal_data, "emergency":emergency_contact, "domain":domain, "picture":picture , "signature":signature, "check":check, "uncheck":uncheck, "logo":logo, "count_words":application_form.essay_count()}
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


		# return render_to_pdf_response(request, template, context_dict)
		# rendered_html = template.render(RequestContext(request, context_dict)).encode(encoding="UTF-8")
		# pdf_file = HTML(string=rendered_html).write_pdf()
		# http_response = HttpResponse(pdf_file, content_type='application/pdf')
		# http_response['Content-Disposition'] = 'filename="report.pdf"'
		# return http_response
		return HttpResponse("Temporarily waiting for xhtml2pdf compatibility")

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