from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q

from easy_pdf.rendering import render_to_pdf_response

from mariners_profile.models import *
from application_form.models import *
from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm

from . forms import ApplicantsDataTables

import sys

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

# def abc(request, getparam, model, student):
# 	if getparam in request.GET:
# 		params = request.GET[getparam]
# 		params = {getparam:param}
# 		params = model.objects.get(**param)
# 		return params
# 	else:
# 		params = {}
# 		return params

@login_required()
def index(request):
	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=0)
	search = ApplicantsDataTables
	age = set()
	vessel_type = set()
	rank = set()
	params = {}
	params2 = {}

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		if 'age' in request.GET:
			params['age'] = request.GET['age']
		if 'vessel_type' in request.GET:
			_vessel_type = VesselType.objects.get(vessel_type=request.GET['vessel_type'])
			params['preferred_vessel_type'] = _vessel_type
		if 'rank' in request.GET:
			_rank = Rank.objects.get(rank=request.GET['rank'])
			params2['position'] = _rank

	if request.method == 'GET' and 'search' in request.GET:
		try:
			searches = request.GET['search']
			# print searches
			searches = searches.partition(' ')[0]
			print searches
			x = UserProfile.objects.filter(Q(first_name__icontains=searches) | Q(last_name__icontains=searches) | Q(middle_name__icontains=searches))
			print x
			mariners_profile = MarinersProfile.objects.filter(user__in=x)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

	personal_data = PersonalData.objects.filter(name__in=mariners_profile.values('user')).filter(**params).order_by('-id')
	mariners_profile = MarinersProfile.objects.filter(user__in=personal_data.values('name')).filter(**params2).order_by('-id')
	zipped_data = zip(mariners_profile, personal_data)

	for x, y in zipped_data:
		age.add(y.age)
		vessel_type.add(y.preferred_vessel_type)
		rank.add(x.position)

	template = "application-profile/index.html"
	context_dict = {"title": "Applicants Profile"}
	# [0] is put to break the instance into the unicode value
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
		pass
	return render(request, template, context_dict)


@login_required()
def profile(request, id):
	if id:
		user_profile = UserProfile.objects.get(id=id)
		personal_data = PersonalData.objects.get(name=id)
		try:
			spouse = Spouse.objects.get(user=id)
		except:
			spouse = ''
		college = College.objects.filter(user=id)
		highschool = HighSchool.objects.get(user=id)
		emergency_contact = EmergencyContact.objects.filter(user=id)
		visa_application = VisaApplication.objects.get(user=id)
		detained = Detained.objects.get(user=id)
		disciplinary_action = DisciplinaryAction.objects.get(user=id)
		charged_offense = ChargedOffense.objects.get(user=id)
		termination = Termination.objects.get(user=id)
		passport = Passport.objects.get(user=id)
		sbook = Sbook.objects.get(user=id)
		coc = COC.objects.get(user=id)
		license = License.objects.get(user=id)
		src = SRC.objects.get(user=id)
		goc = GOC.objects.get(user=id)
		us_visa = USVisa.objects.get(user=id)
		schengen_visa = SchengenVisa.objects.get(user=id)
		yellow_fever = YellowFever.objects.get(user=id)
		# FlagDocuments = FlagDocuments.objects.get(user=id)
		# FlagDocumentsDetailed = FlagDocumentsDetailed.objects.get(user=id)
		# TrainingCertificateDocuments = TrainingCertificateDocuments.objects.get(user=id)
		# TrainingCertificateDocumentsDetailed = TrainingCertificateDocumentsDetailed.objects.get(user=id)
		sea_service = SeaService.objects.filter(user=id)
		mariners_profile = MarinersProfile.objects.get(user=id)
		application_form = ApplicationForm.objects.get(user=id)

		try:
			flag_documents = FlagDocuments.objects.get(user=user_profile)
			flag_list = []
			flags = get_list_or_404(FlagDocumentsDetailed, flags_documents=flag_documents.id)
			# print flags
			for flag in flags:
				# print flag.id
				flag_list.append(flag.flags.id)
			flags = {'flags': flag_list}
			flags = FlagForm(initial=flags)
		except:
			flags = ''

		training_certificate_documents = TrainingCertificateDocuments.objects.get(user=user_profile)
		training_certificate_list = []
		training_certificates = get_list_or_404(TrainingCertificateDocumentsDetailed, trainings_certificate_documents=training_certificate_documents.id)
		# print training_certificates
		for training_certificate in training_certificates:
			# print training_certificate.id
			# print training_certificate.trainings_certificates.id
			training_certificate_list.append(training_certificate.trainings_certificates.id)
		training_certificates = {'trainings_certificates': training_certificate_list}
		trainings_certificates = TrainingCertificateForm(initial=training_certificates)

		if request.POST:
			# print request.POST
			_status = request.POST['status']
			_status = Status.objects.get(id=_status)
			application_form.status = _status
			application_form.save()
			mariners_profile.status = 1
			mariners_profile.save()
			if str(application_form.status) == 'Passed':
				print "dean"
				return HttpResponseRedirect('/mariners-profile/'+id)

		status = StatusForm(initial={'status':str(application_form.status.id)})
		
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
		context_dict['title'] = "Applicants Profile - "+str(personal_data)
		# context_dict['FlagDocuments'] = FlagDocuments
		# context_dict['FlagDocumentsDetailed'] = FlagDocumentsDetailed
		# context_dict['TrainingCertificateDocuments'] = TrainingCertificateDocuments
		# context_dict['TrainingCertificateDocumentsDetailed'] = TrainingCertificateDocumentsDetailed
		context_dict['sea_service'] = sea_service
		context_dict['application_form'] = application_form
		context_dict['mariners_profile'] = mariners_profile

		context_dict['flags'] = flags
		context_dict['trainings_certificates'] = trainings_certificates
		context_dict['status'] = status

		context_dict['count_words'] = count_words

		return render(request, template, context_dict)

@login_required()
def pdf(request, id):
	if id:
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
		application_form = ApplicationForm.objects.get(user=id)

		flags = ApplicationFormFlagDocuments.objects.get(user=user_profile)
		certificates_documents = ApplicationFormTrainingCertificateDocuments.objects.get(user=user_profile)
			
		cayman_islands = flags.flags.filter(flags='Cayman Islands')
		marshall_islands = flags.flags.filter(flags='Marshall Islands')
		liberia = flags.flags.filter(flags='Liberia')
		cyprus = flags.flags.filter(flags='Cyprus')
		singapore = flags.flags.filter(flags='Singapore')
		greek = flags.flags.filter(flags='Greek')
		barbados = flags.flags.filter(flags='Barbados')
		german = flags.flags.filter(flags='German')
		bahamas = flags.flags.filter(flags='Bahamas')

		cop_bt = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Basic Training')
		cop_btoc = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Basic Training for Oil and Chemical Tanker')
		cop_atot = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Training for Oil Tanker')
		cop_atct = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Training for Chemical Tanker')
		cop_pfrb = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Proficiency in Fast Rescue Boat')
		cop_aff = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Advance Fire Fighting')
		cop_mefa = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Medical Emergency First Aid')
		cop_meca = certificates_documents.trainings_certificates.filter(trainings_certificates='	Certificate of Proficiency / Meical Care')
		cop_sso = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Ship Security Officer')
		cop_pscrb = certificates_documents.trainings_certificates.filter(trainings_certificates='	Certificate of Proficiency / Proficiency in Survival Craft and Rescue Boat')
		cop_ssa_sdsd = certificates_documents.trainings_certificates.filter(trainings_certificates='Certificate of Proficiency / Ship Security Awareness / Seafarers with Designated Security Duties')
		bt = certificates_documents.trainings_certificates.filter(trainings_certificates='Basic Training')
		pscrb = certificates_documents.trainings_certificates.filter(trainings_certificates='Proficiency in Survival Craft and Recue Boat')
		aff = certificates_documents.trainings_certificates.filter(trainings_certificates='Advance Fire Fighting')
		mefa = certificates_documents.trainings_certificates.filter(trainings_certificates='Medical Emergency First Aid')
		meca = certificates_documents.trainings_certificates.filter(trainings_certificates='Medical Care')
		pfrb = certificates_documents.trainings_certificates.filter(trainings_certificates='Proficiency in Fast Rescue Boat')
		ssbt = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Simulator and Bridge Team Work')
		brm = certificates_documents.trainings_certificates.filter(trainings_certificates='Bridge Resource Management')
		btm = certificates_documents.trainings_certificates.filter(trainings_certificates='Bridge Team Management')
		btoc = certificates_documents.trainings_certificates.filter(trainings_certificates='Basic Training for Oil and Chemical Tanker Cargo Operations')
		sbff = certificates_documents.trainings_certificates.filter(trainings_certificates='Shore Based Fire Fighting')
		atot = certificates_documents.trainings_certificates.filter(trainings_certificates='Advance Training for Oil Tanker')
		atct = certificates_documents.trainings_certificates.filter(trainings_certificates='Advance Training for Chemical Tanker')
		inmarsat = certificates_documents.trainings_certificates.filter(trainings_certificates='International Maritime Satellite')
		gmdss = certificates_documents.trainings_certificates.filter(trainings_certificates='Global Maritime Distress and Safety System')
		padams = certificates_documents.trainings_certificates.filter(trainings_certificates='Prevention of Alcohol and Drug Abuse in the Maritime Sector')
		hazmat = certificates_documents.trainings_certificates.filter(trainings_certificates='Hazardous Material')
		cow_igs = certificates_documents.trainings_certificates.filter(trainings_certificates='Crude Oil Washing / Inert Gas System')
		ers_erm = certificates_documents.trainings_certificates.filter(trainings_certificates='Engine Room Simulator with Engine Room Management')
		srroc = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Restricted Radiotelephone Operator Course')
		framo = certificates_documents.trainings_certificates.filter(trainings_certificates='FRAMO')
		sos = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Security Officer')
		soc = certificates_documents.trainings_certificates.filter(trainings_certificates='Safety Officer Course')
		bwk_ewk = certificates_documents.trainings_certificates.filter(trainings_certificates='Deck Watch Keeping / Engine Watch Keeping')
		rsc = certificates_documents.trainings_certificates.filter(trainings_certificates='Radar Simulator Course')
		ism = certificates_documents.trainings_certificates.filter(trainings_certificates='International Safety Management')
		ssmep = certificates_documents.trainings_certificates.filter(trainings_certificates='Shipboard Managerial Skills Enhancement Program')
		acni = certificates_documents.trainings_certificates.filter(trainings_certificates='Accident and Near-miss Investigation')
		ssa_sdsd = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Security Awareness / Seafarers with Designated Security Duties')
		arpa_ropa = certificates_documents.trainings_certificates.filter(trainings_certificates='Radar Navigation / Radar Plotting and use of ARPA ROPA')
		ecdis_generic = certificates_documents.trainings_certificates.filter(trainings_certificates='Electronic Chart Display and Information System')
		mlc_deck = certificates_documents.trainings_certificates.filter(trainings_certificates='Management Level Course - Deck')
		marpol = certificates_documents.trainings_certificates.filter(trainings_certificates='Marine Pollution I-VI')
		mlc_engine = certificates_documents.trainings_certificates.filter(trainings_certificates='Management Level Course - Engine')
		ecdis_specific = certificates_documents.trainings_certificates.filter(trainings_certificates='Electronic Chart Display and Information System Specific')
		ship_vetting = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Vetting')
		ship_handling = certificates_documents.trainings_certificates.filter(trainings_certificates='Ship Handling')
		maritime_eng = certificates_documents.trainings_certificates.filter(trainings_certificates='Maritime Eng.')

		domain = request.scheme
		domain += "://"
		# returns domain name
		domain += request.META["HTTP_HOST"]
		media = domain+"/media/"
		picture = media+str(application_form.picture)
		signature = media+str(application_form.signature)
		check = domain+"/static/img/check.jpg"
		uncheck = domain+"/static/img/uncheck.jpg"
		logo = domain+"/static/img/small_logo.png"

		# count essay words
		count_words = ''.join(c if c.isalnum() else ' ' for c in application_form.essay.essay).split()
		count_words = len(count_words)

		if str(personal_data.civil_status) == "Domestic Partner":
			partner = "Live-In"
		else:
			partner = "Spouse"

		template = "application_form/pdf-report.html"
		context_dict = { "appform":application_form, "personaldata":personal_data, "emergency":emergency_contact, "domain":domain, "picture":picture , "signature":signature, "check":check, "uncheck":uncheck, "logo":logo, "cayman_islands": cayman_islands, "marshall_islands": marshall_islands, "liberia":liberia, "cyprus":cyprus, "singapore":singapore, "greek":greek, "cop_bt":cop_bt, "cop_btoc":cop_btoc, "cop_atot":cop_atot, "cop_atct":cop_atct, "cop_pfrb":cop_pfrb, "cop_aff":cop_aff, "cop_mefa":cop_mefa, "cop_meca":cop_meca, "cop_sso":cop_sso, "cop_pscrb":cop_pscrb, "cop_ssa_sdsd":cop_ssa_sdsd, "bt":bt, "pscrb":pscrb, "aff":aff, "mefa":mefa, "meca":meca, "pfrb":pfrb, "ssbt":ssbt, "brm":brm, "btm":btm, "btoc":btoc, "sbff":sbff, "atot":atot, "atct":atct, "inmarsat":inmarsat, "gmdss":gmdss, "padams":padams, "hazmat":hazmat, "cow_igs":cow_igs, "ers_erm":ers_erm, "srroc":srroc, "framo":framo, "sos":sos, "soc":soc, "bwk_ewk":bwk_ewk, "rsc":rsc, "ism":ism, "ssmep":ssmep, "acni":acni, "ssa_sdsd":ssa_sdsd, "arpa_ropa":arpa_ropa, "ecdis_generic":ecdis_generic, "mlc_deck":mlc_deck, "marpol":marpol, "mlc_engine":mlc_engine, "ecdis_specific":ecdis_specific, "ship_vetting":ship_vetting, "ship_handling":ship_handling, "maritime_eng":maritime_eng, "count_words":count_words}
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
		context_dict['partner'] = partner
		return render_to_pdf_response(request, template, context_dict)
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