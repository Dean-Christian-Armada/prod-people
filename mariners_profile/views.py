from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q

from login.models import UserProfile
from . models import *

from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm

from mariners_profile.forms import MarinersDataTables

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

# Create your views here.
@login_required()
def index(request):
	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=1)
	search = MarinersDataTables
	# Sets are used for dynamic value filtering
	age = set()
	vessel_type = set()
	rank = set()
	params = {}
	params2 = {}

	template = "mariner-profile/index.html"
	context_dict = {"title": "Mariners Profile"}

	choice_visa = ''

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		if 'age' in request.GET:
			params['age'] = request.GET['age']
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
			print "dean"
		except:
			flags = FlagForm()

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

		template = "mariner-profile/profile.html"

		context_dict = {}
		# Database querysets variables
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
		context_dict['title'] = "Mariners Profile - "+str(personal_data)
		# context_dict['FlagDocuments'] = FlagDocuments
		# context_dict['FlagDocumentsDetailed'] = FlagDocumentsDetailed
		# context_dict['TrainingCertificateDocuments'] = TrainingCertificateDocuments
		# context_dict['TrainingCertificateDocumentsDetailed'] = TrainingCertificateDocumentsDetailed
		context_dict['sea_service'] = sea_service
		context_dict['mariners_profile'] = mariners_profile

		# Many-to-many variables
		context_dict['flags'] = flags
		context_dict['trainings_certificates'] = trainings_certificates

		return render(request, template, context_dict)

# Real Time delete on a formset
@login_required()
def delete_on_form_set(request):
	id=request.GET['id']
	if id:	
		college = College.objects.get(id=id)
		college.delete()
	return HttpResponse('')