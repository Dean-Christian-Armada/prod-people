from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Q
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

from login.models import UserProfile
from . models import *

from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm, DynamicTrainingCertificateForm

from mariners_profile.forms import *

import sys

def sample_only(request):
	print request.user

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
	barangay = set()
	municipality = set()
	params = {}
	params2 = {}

	template = "mariner-profile/index.html"
	context_dict = {"title": "MARINER Profiles"}

	choice_visa = ''

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		if 'vessel_type' in request.GET:
			_vessel_type = VesselType.objects.get(vessel_type__iexact=request.GET['vessel_type'])
			params['preferred_vessel_type'] = _vessel_type
		if 'rank' in request.GET:
			_rank = Rank.objects.get(rank__iexact=request.GET['rank'])
			params2['position'] = _rank
		# if 'barangay' in request.GET:
		# 	_barangay = Barangay.objects.get(barangay__iexact=request.GET['barangay'])
		# 	_barangay = Zip.objects.filter(barangay=_barangay)
		# 	_barangay = CurrentAddress.objects.filter(current_zip=_barangay)
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
			x = UserProfile.objects.filter(Q(first_name__icontains=searches) | Q(last_name__icontains=searches) | Q(middle_name__icontains=searches) | Q(code__iexact=searches))
			mariners_profile = MarinersProfile.objects.filter(user__in=x)
		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

	
	personal_data = PersonalData.objects.filter(name__in=mariners_profile.values('user')).filter(**params).order_by('-id')
	mariners_profile = MarinersProfile.objects.filter(user__in=personal_data.values('name')).filter(**params2).order_by('-id')

	# Change in age filtering synatx because age is now a custom model method
	# if 'age' in request.GET:
	# 	age = request.GET['age']
	# 	print age
	# 	personal_data = PersonalData.objects.filter()
	# 	personal_data_ids = [o.id for o in personal_data if o.age() == age]
	# 	personal_data = PersonalData.objects.filter(id__in=personal_data_ids).order_by('-id')
	# 	print personal_data
	
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
		# barangay.add(y.current_address.current_zip.barangay)
		municipality.add(y.current_address.current_zip.municipality)
		rank.add(x.position)

	
	# [0] is put to break the instance into the unicode value
	try:
		context_dict['personaldata'] = personal_data
		context_dict['mariners_profile'] = mariners_profile
		context_dict['name'] = name
		context_dict['nick_name'] = user.nick_name
		context_dict['zipped_data'] = zipped_data
		context_dict['search'] = search
		context_dict['age'] = sorted(age)
		context_dict['vessel_type'] = sorted(vessel_type)
		context_dict['rank'] = sorted(rank)
		# context_dict['barangay'] = sorted(barangay)
		context_dict['municipality'] = sorted(municipality)
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
		current_user = UserProfile.objects.get(user=request.user)
		mariners_profile = MarinersProfile.objects.get(user=user_profile)
		personal_data = PersonalData.objects.get(name=id)
		flag_documents = FlagDocuments.objects.get(user=user_profile)
		trainings_certificate_documents = TrainingCertificateDocuments.objects.get(user=user_profile)

		# START, variables used to prepopulate inlineformset for flags
		flags_standard = Flags.objects.filter(company_standard=1)
		flags_standard_num = len(flags_standard)
		flags_num = len(FlagDocumentsDetailed.objects.filter(flags_documents=flag_documents))
		if(flags_standard_num != flags_num):
			for flags in flags_standard:
				flag = Flags.objects.get(flags=flags.flags)
				FlagDocumentsDetailed.objects.get_or_create(flags_documents=flag_documents, flags=flag)
		# END
		# START, variables used to prepopulate inlineformset for training and certificates
		rank = Rank.objects.get(id=mariners_profile.position.id)
		
		trainings_certificate_standard = TrainingCertificates.objects.filter(departments=rank.department).filter(company_standard=1)
		trainings_certificate_standard_num = len(trainings_certificate_standard)
		trainings_certificate_num = len(TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificate_documents=trainings_certificate_documents))
		if(trainings_certificate_standard_num != trainings_certificate_num):
			for trainings_certificate in trainings_certificate_standard:
				training_certificate = TrainingCertificates.objects.get(trainings_certificates=trainings_certificate.trainings_certificates)
				TrainingCertificateDocumentsDetailed.objects.get_or_create(trainings_certificate_documents=trainings_certificate_documents, trainings_certificates=training_certificate)
		# END

		# Used for formset updating / inlineformset_factory
		college = College.objects.filter(user=id)
		emergency_contact = EmergencyContact.objects.filter(user=id)

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

		applicant_name_form = ApplicantNameForm(instance=user_profile)
		personal_data_form = PersonalDataForm(instance=personal_data, initial={'birth_place':personal_data.birth_place, 'preferred_vessel_type':personal_data.preferred_vessel_type, 'dialect':personal_data.dialect})
		permanent_address_form = PermanentAddressForm(instance=personal_data.permanent_address, initial={'permanent_zip':personal_data.permanent_address.permanent_zip.zip, 'permanent_barangay':personal_data.permanent_address.permanent_zip.barangay, 'permanent_municipality':personal_data.permanent_address.permanent_zip.municipality})
		current_address_form = CurrentAddressForm(instance=personal_data.current_address, initial={'current_zip':personal_data.current_address.current_zip.zip, 'current_barangay':personal_data.current_address.current_zip.barangay, 'current_municipality':personal_data.current_address.current_zip.municipality})

		try:
			spouse = Spouse.objects.get(user=id)
			spouse_form = SpouseForm(request.POST or None, instance=spouse)
		except:
			spouse = ''
			spouse_form = SpouseForm(request.POST or None, initial={'user':personal_data.name, } )

		# Used for formset updating / inlineformset_factory
		CollegeFormSet = inlineformset_factory(UserProfile, College, extra=0, can_delete=False, form=CollegeForm )
		college_form = CollegeFormSet(request.POST or None, instance=user_profile)

		# sample = [{'emergency_municipality':'Quezon City', 'emergency_barangay':'Holy Spirit', 'emergency_zip':1127}]
		EmergencyContactFormSet = inlineformset_factory(UserProfile, EmergencyContact, extra=0, can_delete=False, form=EmergencyContactForm )
		emergency_contact_form = EmergencyContactFormSet(instance=user_profile)

		dependents = Dependents.objects.filter(user=id)
		if len(dependents) < 1:
			dependents_num_extra = 1
			dependents_num_label = "No dependets yet"
		else:
			dependents_num_extra = 0
			dependents_num_label = len(dependents)
		DependentsFormSet = inlineformset_factory(UserProfile, Dependents, extra=0, can_delete=False, form=DependentsForm )
		dependents_form = DependentsFormSet(instance=user_profile)

		FlagFormSet = inlineformset_factory(FlagDocuments, FlagDocumentsDetailed, extra=0, can_delete=False, form=FlagForm)
		flag_form = FlagFormSet(request.POST or None, instance=flag_documents)

		TrainingCertificateFormSet = inlineformset_factory(TrainingCertificateDocuments, TrainingCertificateDocumentsDetailed, extra=0, can_delete=False, form=TrainingCertificateForm)
		trainings_certificate_form = TrainingCertificateFormSet(request.POST or None, instance=trainings_certificate_documents)

		SeaServiceFormSet = inlineformset_factory(UserProfile, SeaService, extra=0, can_delete=False, form=SeaServiceForm )
		sea_service_form = SeaServiceFormSet(instance=user_profile)

		try:
			vocational = Vocational.objects.get(user=id)
			vocational_form = VocationalForm(request.POST or None, instance=vocational, initial={'vocational':vocational.vocational})
		except:
			vocational = ''
			vocational_form = VocationalForm(request.POST or None, initial={'user': personal_data.name} )

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
			AlloteeFormSet = inlineformset_factory(UserProfile, Allotee, fk_name='user', extra=num_extra, can_delete=True, form=AlloteeForm )
			allotee_form = AlloteeFormSet(request.POST or None, instance=user_profile )

		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

		highschool_form = HighSchoolForm(request.POST or None, instance=highschool, initial={'highschool':highschool.highschool})

		try:
			primaryschool = PrimarySchool.objects.get(user=id)
			primaryschool_form = PrimarySchoolForm(request.POST or None, instance=primaryschool, initial={'primaryschool':primaryschool.primaryschool})
		except:
			primaryschool_form = PrimarySchoolForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			stcw_endorsement = STCWEndorsement.objects.get(user=id)
			stcw_endorsement_form = STCWEndorsementForm(request.POST or None, instance=stcw_endorsement, initial={'stcw_endorsement_rank':stcw_endorsement.stcw_endorsement_rank})
		except:
			stcw_endorsement_form = STCWEndorsementForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			stcw_certificate = STCWCertificate.objects.get(user=id)
			stcw_certificate_form = STCWCertificateForm(request.POST or None, instance=stcw_certificate, initial={'stcw_certificate_rank':stcw_certificate.stcw_certificate_rank})
		except:
			stcw_certificate_form = STCWCertificateForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			ntc_license = NTCLicense.objects.get(user=id)
			ntc_license_form = NTCLicenseForm(request.POST or None, instance=ntc_license, initial={'ntc_license_rank':ntc_license.ntc_license_rank})
		except:
			ntc_license_form = NTCLicenseForm(request.POST or None, initial={'user': personal_data.name} )

		try:
			# evaluation = Evaluation.objects.get(user=id)
			evaluation = Evaluation.objects.filter(user=id).order_by('-id')
			current_evaluation = evaluation[0]
			evaluations = evaluation[1:]
			evaluation_form = EvaluationForm(request.POST or None, instance=current_evaluation, initial={'evaluation':current_evaluation.evaluation, 'evaluated_by': current_user})
		except:
			evaluation = ''
			current_evaluation = ''
			evaluations = ''
			evaluation_form = EvaluationForm(initial={'user': personal_data.name, 'evaluated_by': current_user} )
		
		try:
			history = MarinerStatusHistory.objects.filter(user=id).order_by('-id')
			current_history = history[0]
			histories = history[1:]
			mariner_status_form = MarinerStatusForm(request.POST or None, instance=current_history, initial={'mariner_status_comment':current_history.mariner_status_comment.mariner_status_comment, 'updated_by': current_user})
		except:
			history = ''
			current_history = ''
			histories = ''
			mariner_status_form = MarinerStatusForm(request.POST or None, initial={'user': personal_data.name, 'updated_by': current_user})

		print "-------------"
		print coc
		passport_form = PassportForm(request.POST or None, instance=passport, initial={'passport_place_issued':passport.passport_place_issued})
		sbook_form = SBookForm(request.POST or None, instance=sbook, initial={'sbook_place_issued':sbook.sbook_place_issued})
		us_visa_form = USVisaForm(request.POST or None, instance=us_visa, initial={'us_visa':us_visa.us_visa, 'us_visa_place_issued':us_visa.us_visa_place_issued})
		schengen_visa_form = SchengenVisaForm(request.POST or None, instance=schengen_visa, initial={'schengen_visa':schengen_visa.schengen_visa, 'schengen_visa_place_issued':schengen_visa.schengen_visa_place_issued})
		yellow_fever_form = YellowFeverForm(request.POST or None, instance=yellow_fever, initial={'yellow_fever_place_issued':yellow_fever.yellow_fever_place_issued})
		license_form = LicenseForm(request.POST or None, instance=license, initial={'license_place_issued':license.license_place_issued, 'license_rank':license.license_rank})
		coc_form = COCForm(request.POST or None, instance=coc, initial={'coc_place_issued':coc.coc_place_issued, 'coc_rank':coc.coc_rank})
		src_form = SRCForm(request.POST or None, instance=src, initial={'src_rank':src.src_rank})
		goc_form = GOCForm(request.POST or None, instance=goc, initial={'goc_rank':goc.goc_rank})
		mariners_position_form = MarinersChangePosition(mariners_profile.position.id, request.POST or None, instance=mariners_profile)

		

		
		template = "mariner-profile/profile.html"

		context_dict = {}

		# form variables
		context_dict['applicant_name_form'] = applicant_name_form
		context_dict['personal_data_form'] = personal_data_form
		context_dict['permanent_address_form'] = permanent_address_form
		context_dict['current_address_form'] = current_address_form
		context_dict['spouse_form'] = spouse_form
		context_dict['emergency_contact_form'] = emergency_contact_form
		context_dict['dependents_form'] = dependents_form
		context_dict['passport_form'] = passport_form
		context_dict['sbook_form'] = sbook_form
		context_dict['us_visa_form'] = us_visa_form
		context_dict['schengen_visa_form'] = schengen_visa_form
		context_dict['yellow_fever_form'] = yellow_fever_form
		context_dict['license_form'] = license_form
		context_dict['ntc_license_form'] = ntc_license_form
		context_dict['coc_form'] = coc_form
		context_dict['src_form'] = src_form
		context_dict['goc_form'] = goc_form
		context_dict['college_form'] = college_form
		context_dict['vocational_form'] = vocational_form
		context_dict['highschool_form'] = highschool_form
		context_dict['primaryschool_form'] = primaryschool_form
		context_dict['land_employment_form'] = land_employment_form
		context_dict['beneficiary_form'] = beneficiary_form
		context_dict['allotee_form'] = allotee_form
		context_dict['stcw_endorsement_form'] = stcw_endorsement_form
		context_dict['stcw_certificate_form'] = stcw_certificate_form
		context_dict['flag_form'] = flag_form
		context_dict['trainings_certificate_form'] = trainings_certificate_form
		context_dict['evaluation_form'] = evaluation_form
		context_dict['sea_service_form'] = sea_service_form
		context_dict['mariner_status_form'] = mariner_status_form
		context_dict['mariners_position_form'] = mariners_position_form

		# queryset variables
		context_dict['user_profile'] = user_profile
		context_dict['mariners_profile'] = mariners_profile
		context_dict['current_history'] = current_history
		context_dict['histories'] = histories
		context_dict['current_evaluation'] = current_evaluation
		context_dict['evaluations'] = evaluations

		context_dict['title'] = "MARINER'S Profile - "+str(personal_data)
		context_dict['dependents_num_label'] = dependents_num_label

		if request.method == "POST":
			print "DEAN"
			print request.POST

			if 'highschool' in request.POST and 'vocational' in request.POST and 'primaryschool' in request.POST:
				if vocational_form.is_valid():
					vocational_form.save()
				else:
					print vocational_form.errors

				if highschool_form.is_valid():
					highschool_form.save()
				else:
					print highschool_form.errors

				if primaryschool_form.is_valid():
					primaryschool_form.save()
				else:
					print primaryschool_form.errors

				if college_form.is_valid():
					for college in college_form:
						college.save()
				else:
					print college_form.errors

				template = "mariner-profile/ajax-update-sub-profiles/educational-information.html"
				return render(request, template, context_dict)
			
			if 'landemployment_set-0-user' in request.POST:
				if land_employment_form.is_valid():
					for land_employment in land_employment_form:
						land_employment.save()
				else:
					print land_employment_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/land-employment.html"
				return render(request, template, context_dict)

			if 'beneficiary_set-0-user' in request.POST:
				if beneficiary_form.is_valid():
					for beneficiary in beneficiary_form:
						beneficiary.save()
				else:
					print beneficiary_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/beneficiary.html"
				return render(request, template, context_dict)

			if 'allotee_set-0-user' in request.POST:
				if allotee_form.is_valid():
					for allotee in allotee_form:
						allotee.save()
				else:
					print allotee_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/allotment.html"
				return render(request, template, context_dict)

			if 'evaluation' in request.POST:
				if evaluation_form.is_valid():
					evaluation_form.save()
				else:
					print evaluation_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/evaluation.html"
				return render(request, template, context_dict)

			if 'mariner_status' in request.POST:
				if mariner_status_form.is_valid():
					mariner_status_form.save()
				else:
					print mariner_status_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/mariner-status.html"
				return render(request, template, context_dict)

			if 'flagdocumentsdetailed_set-0-flags_documents' in request.POST:
				if flag_form.is_valid():
					for flag in flag_form:
						flag.save()
				else:
					print flag_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/flags.html"
				return render(request, template, context_dict)
			
			if 'passport' in request.POST and 'sbook' in request.POST and 'yellow_fever' in request.POST and 'license' in request.POST and 'ntc_license' in request.POST and 'goc' in request.POST and 'src' in request.POST and 'stcw_endorsement' in request.POST and 'stcw_certificate' in request.POST:
				if passport_form.is_valid():
					passport_form.save()
				else:
					print passport_form.errors
				if sbook_form.is_valid():
					sbook_form.save()
				else:
					print sbook_form.errors

				if yellow_fever_form.is_valid():
					yellow_fever_form.save()
				else:
					print yellow_fever_form.errors

				if license_form.is_valid():
					license_form.save()
				else:
					print license_form.errors

				if ntc_license_form.is_valid():
					ntc_license_form.save()
				else:
					print ntc_license_form.errors	

				if goc_form.is_valid():
					goc_form.save()
				else:
					print goc_form.errors	

				if src_form.is_valid():
					src_form.save()
				else:
					print src_form.errors	

				if stcw_endorsement_form.is_valid():
					stcw_endorsement_form.save()
				else:
					print stcw_endorsement_form.errors

				if stcw_certificate_form.is_valid():
					stcw_certificate_form.save()
				else:
					print stcw_certificate_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/licenses.html"
				return render(request, template, context_dict)

			if 'us_visa' in request.POST and 'coc' in request.POST and 'schengen_visa' in request.POST:
				if us_visa_form.is_valid():
					us_visa_form.save()		
				else:
					print us_visa_form.errors

				if schengen_visa_form.is_valid():
					schengen_visa_form.save()
				else:
					print schengen_visa_form.errors

				if coc_form.is_valid():
					coc_form.save()
				else:
					print coc_form.errors
				template = "mariner-profile/ajax-update-sub-profiles/coc_visas.html"
				return render(request, template, context_dict)

			if 'trainingcertificatedocumentsdetailed_set-0-trainings_certificate_documents' in request.POST:
				if trainings_certificate_form.is_valid():
					for trainings_certificate in trainings_certificate_form:
						trainings_certificate.save()
				else:
					print trainings_certificate_form.errors
				if request.POST['param']:
					if request.POST['param'] == 'National':
						html = 'national-certificates'
					else:
						html = 'certificates'
				print html
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			else:
				return HttpResponse('FAIL CATCH')

			# if sea_service_form.is_valid():
			# 	for sea_service in sea_service_form:
			# 		sea_service.save()
			# else:
			# 	print sea_service_form.errors

			

			# if applicant_name_form.is_valid():
			# 	applicant_name_form.save()
			# else:
			# 	print applicant_name_form.errors

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

			# if emergency_contact_form.is_valid():
			# 	for emergency_contact in emergency_contact_form:
			# 		emergency_contact.save()
			# else:
			# 	print emergency_contact_form.errors

			# if dependents_form.is_valid():
			# 	for dependents in dependents_form:
			# 		dependents.save()
			# else:
			# 	print dependents_form.errors

			# # Travel Documents Testing
			# if passport_form.is_valid() and sbook_form.is_valid() and us_visa_form.is_valid() and schengen_visa_form.is_valid() and yellow_fever_form.is_valid():
			# 		passport_form.save()
			# 		sbook_form.save()
			# 		us_visa_form.save()
			# 		schengen_visa_form.save()
			# 		yellow_fever_form.save()
			# else:
			# 	passport_form.errors
			# 	sbook_form.errors
			# 	us_visa_form.errors
			# 	schengen_visa_form.errors
			# 	yellow_fever_form.errors


			# # LICENSES
			# if license_form.is_valid() and coc_form.is_valid():
			# 	license_form.save()
			# 	coc_form.save()
			# else:
			# 	print license_form.errors
			# 	print coc_form.errors

		return render(request, template, context_dict)

# Real Time delete on a formset
@login_required()
def delete_on_form_set(request):
	id=request.GET['id']
	if id:	
		college = College.objects.get(id=id)
		college.delete()
	return HttpResponse('')