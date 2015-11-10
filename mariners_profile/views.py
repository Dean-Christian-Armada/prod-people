from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
from django.db.models import Q
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetime import datetime as now

from login.models import UserProfile
from cms.models import Folder, SubFolder, File, Fields, FileFieldValue
from . models import *

from application_form.forms import FlagForm, TrainingCertificateForm, StatusForm, DynamicTrainingCertificateForm

from mariners_profile.forms import *

import sys

now = now.now()

def xyz(request, method):
	if method == "POST": request_method = request.POST
	elif method == "GET": request_method = request.GET

	# returns full url
	url = request.scheme
	url += "://"
	url += request.META['HTTP_HOST']
	url += request.get_full_path()

	params = "?"

	if 'page' in request.GET and len(request.GET) > 0:
		params = ""

	for x in request_method:
		if x != 'csrfmiddlewaretoken' and x != 'submit' and x != 'page':
			if request_method[x]:
				params += "&"+x+"="+request_method[x]

	return (params, url)

# Create your views here.
@login_required()
def index(request):
	crew_on_table = 2
	per_page_list = [2, 1, 3, 4]
	param_connector = "?"
	count = 0

	user = UserProfile.objects.get(user=request.user)
	name = "%s %s %s" % (user.first_name, user.middle_name, user.last_name )
	mariners_profile = MarinersProfile.objects.filter(status=1)
	search = MarinersDataTables
	# Sets are used for dynamic value filtering
	age = set()
	vessel_type = set()
	rank = set()
	principal_choices = set()
	status_choices = set()
	barangay = set()
	municipality = set()
	num = set()
	params = {}
	params2 = {}

	template = "mariner-profile/index.html"
	context_dict = {"title": "MANSHIP Mariners"}

	choice_visa = ''

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
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

		if 'status' in request.GET:
			_status = MarinerStatus.objects.get(mariner_status__iexact=request.GET['status'])
			# Used Group By Like SQL QUERY
			# Query Set that gets the latest status for each user filtered
			mariners_profile = MarinerStatusHistory.objects.filter(id__in=MarinerStatusHistory.objects.filter(user__in=mariners_profile.values('user')).order_by().values('user').annotate(max_id=models.Max('id')).values('max_id')).filter(mariner_status=_status)

		if 'principal' in request.GET:
			_principal = Principal.objects.get(principal__iexact=request.GET['principal'])
			# Used Group By Like SQL QUERY
			# Query Set that gets the latest principal for each user filtered
			mariners_profile = MarinerStatusHistory.objects.filter(id__in=MarinerStatusHistory.objects.filter(user__in=mariners_profile.values('user')).order_by().values('user').annotate(max_id=models.Max('id')).values('max_id')).filter(mariner_principal=_principal)


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
	schengen_visa = SchengenVisa.objects.filter(user__in=mariners_profile.values('user')).order_by('-id').distinct()

	# Mariner Status and Principal Dynamic Filtering
	# mariner_status_history = MarinerStatusHistory.objects.filter(user__in=mariners_profile.values('user')).order_by('-id').distinct()
	# Used Group By Like SQL QUERY
	# Query Set that gets the latest principal for each user filtered
	mariner_status_history = MarinerStatusHistory.objects.filter(id__in=MarinerStatusHistory.objects.filter(user__in=mariners_profile.values('user')).order_by().values('user').annotate(max_id=models.Max('id')).values('max_id'))

	# Fills the options of the selectbox for principals and status
	for w in mariner_status_history:
		principal_choices.add(w.mariner_principal)
		status_choices.add(w.mariner_status)

	# Zipped is used for the table data
	zipped_data = zip(mariners_profile, personal_data, us_visa, schengen_visa)

	for x, y, z, xx in zipped_data:
		count += 1
		age.add(y.age)
		vessel_type.add(y.preferred_vessel_type)
		barangay.add(y.current_address.current_zip.barangay)
		municipality.add(y.current_address.current_zip.municipality)
		rank.add(x.position)
		num.add(count)

	# START Script to paginate the query and retrieve all the parameters to the URL
	# Script to retrieve all the parameters to a variable
	params, url = xyz(request, "GET")

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
	# END Script to paginate the query and retrieve all the parameters to the URL

	# Zipped is used for the table data
	zipped_data = zip(mariners_profile, personal_data, us_visa, schengen_visa, sorted(num, reverse=True))

	
	# [0] is put to break the instance into the unicode value
	try:
		context_dict['personaldata'] = personal_data
		context_dict['mariners_profile'] = mariners_profile
		context_dict['name'] = name
		context_dict['user'] = user
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

	# used for dynamic choices in status
	context_dict['status'] = status_choices

	# used for dynamic choices in principal
	context_dict['principal'] = principal_choices

	# used to retrieve all the parameters on the page links
	context_dict['params'] = params
	context_dict['param_connector'] = param_connector

	context_dict['per_page_list'] = per_page_list
	

	return render(request, template, context_dict)

@login_required()
def profile(request, slug):
	if slug:
		user_profile = UserProfile.objects.get(slug=slug)
		id = user_profile.id
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
				try:
					FlagDocumentsDetailed.objects.get_or_create(flags_documents=flag_documents, flags=flag)
				except:
					pass
		# END
		# START, variables used to prepopulate inlineformset for training and certificates
		rank = Rank.objects.get(id=mariners_profile.position.id)
		
		trainings_certificate_standard = TrainingCertificates.objects.filter(departments=rank.department).filter(company_standard=1)
		trainings_certificate_standard_num = len(trainings_certificate_standard)
		trainings_certificate_num = len(TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificate_documents=trainings_certificate_documents))
		if(trainings_certificate_standard_num != trainings_certificate_num):
			for trainings_certificate in trainings_certificate_standard:
				training_certificate = TrainingCertificates.objects.get(trainings_certificates=trainings_certificate.trainings_certificates)
				try:
					TrainingCertificateDocumentsDetailed.objects.get_or_create(trainings_certificate_documents=trainings_certificate_documents, trainings_certificates=training_certificate)
				except:
					pass
		# END

		try:
			picture_age_indicator = (now.date() - mariners_profile.picture_last_modified.date()).days
		except:
			picture_age_indicator = ""

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

		# START Objects for scanning documents
		from django.middleware.csrf import get_token
		scanned_document_html = ''
		scanned_document_html = ''
		scanned_js = ''
		scanned_js += 'img="/static/img/updating.gif";'
		scanned_js += 'url = window.location;'
		scanned_js += 'var check_count = 0;' # Used to check if the delete button should be shown
		scanned_js += 'var value_list = [];'
		scanned_js += '$("body").on("change", "input[type=\'checkbox\'].scanned_delete_checkbox", function(){' # START OF checkbox change event
		scanned_js += 'if($(this).is(":checked")){' # START  OF is checked conditional
		scanned_js += 'check_count++;'
		scanned_js += 'value_list.push($(this).val());'
		# scanned_js += '$(this).closest(".panel-collapse").css("background-color", "#ccc");'
		scanned_js += '}else{'
		scanned_js += 'check_count--;'
		scanned_js += 'value_list.splice(value_list.indexOf($(this).val()),1);'
		scanned_js += '}'
		scanned_js += '$(this).parent().parent().siblings($(".delete-id-list")).val(value_list);'
		scanned_js += 'if(check_count > 0){'
		scanned_js += '$(this).closest(".panel-collapse").siblings("p.cursor-pointer").find(".archive-process-button").removeClass("hide");'
		scanned_js += '}else{'
		scanned_js += '$(this).closest(".panel-collapse").siblings("p.cursor-pointer").find(".archive-process-button").addClass("hide");'
		scanned_js += '}'
		scanned_js += '});' # END of checkboxchange event
		scanned_js += '$(".archive-process-button").click(function(){' # START of put to archive process button event
		scanned_js += 'delete_id_list = $(this).parent().next().find(".delete-id-list").val();'
		scanned_js += 'var json_archive_ids = {csrfmiddlewaretoken: "%s"};' % get_token(request)
		scanned_js += 'json_archive_ids["delete_id_list"] = delete_id_list;'
		# scanned_js += 'console.log(json_archive_ids);'
		scanned_js += 'var this_object = $(this);'
		scanned_js += 'var parent_next = $(this).parent().next();'
		scanned_js += 'parent_next.html("<div class=\'text-center\'><img src=\'"+img+"\'></div>");'
		scanned_js += '$.post(url, json_archive_ids, function(result){' # START of json_archive_ids AJAX POST call
		scanned_js += 'this_object.addClass("hide");'
		scanned_js += 'parent_next.html(result);'
		scanned_js += '});' # END of json_archive_ids AJAX POST call
		scanned_js += '});' # END of put to archive process button event
		scanned_js += '$(".archive-show-button").click(function(){' # START of put to archive show button event
		scanned_js += '$(this).siblings(".archive-process-button").addClass("hide");'
		scanned_js += 'archive_location = $(this).attr("data-location");'
		scanned_js += 'archive_condition = $(this).attr("data-params");'
		scanned_js += 'get_params = {};'
		scanned_js += 'get_params["location"] = archive_location;'
		scanned_js += 'get_params["folder"] = "archive";'
		scanned_js += 'get_params["condition"] = archive_condition;'
		scanned_js += 'var this_object = $(this);'
		scanned_js += 'var parent_next = $(this).parent().next();'
		scanned_js += 'parent_next.html("<div class=\'text-center\'><img src=\'"+img+"\'></div>");'
		scanned_js += '$.get(url, get_params, function(result){' # START of get_params AJAX GET call
		scanned_js += 'parent_next.html(result);'
		scanned_js += '});' # END of get_params AJAX GET call
		scanned_js += '$(this).addClass("hide");'
		scanned_js += 'if(archive_condition == "True"){'
		scanned_js += '$(this).next().removeClass("hide");'
		scanned_js += '}else{'
		scanned_js += '$(this).prev().removeClass("hide");'
		scanned_js += '};'
		scanned_js += '});' # END of put to archive show button event
		scanned_js += '$("body").on("click", ".scanned-document-editables", function(){' # START scanned-document-editables click event 
		scanned_js += 'data_id = $(this).attr("data-id");'
		scanned_js += 'data_classes = $(this).attr("data-classes");'
		scanned_js += 'data_type = $(this).attr("data-type");'
		scanned_js += 'text = $(this).text();'
		scanned_js += '$(".tooltip").remove();'
		scanned_js += 'if(data_type != "select"){'
		scanned_js += '$(this).parent().append("<input name=\'field-value-updates\' data-classes=\'"+data_classes+"\' class=\'scanned-document-editing "+data_classes+"\' type=\'"+data_type+"\' data-id=\'"+data_id+"\' value=\'"+text+"\'>");'      
		scanned_js += '}else{'
		scanned_js += '}'
		scanned_js += '$(this).next().focus();'
		scanned_js += '$(this).remove();'
		scanned_js += '});' # END scanned-document-editables click event
		scanned_js += '$("body").on("focusout", ".scanned-document-editing", function(){' # START scanned-document-editing focustout event
		scanned_js += '_this = $(this);'
		scanned_js += 'type = $(this).attr("type");'
		scanned_js += 'data_classes = $(this).attr("data-classes");'
		scanned_js += 'data_id = $(this).attr("data-id");'
		scanned_js += 'setTimeout(function(){'
		scanned_js += 'val = _this.val();'
		scanned_js += 'var _confirm = confirm("Proceed to Update?");'
		scanned_js += 'if( _confirm ==  true ){'
		scanned_js += '_this.parent().append("<u class=\'scanned-document-editables\' data-toggle=\'tooltip\' title=\'Click to Update\' data-id=\'"+data_id+"\' data-classes=\'"+data_classes+"\' data-type=\'"+type+"\'>"+val+"</u>");'
		scanned_js += '_this.remove();'

		scanned_js += 'get_value = {csrfmiddlewaretoken: "%s"};' % get_token(request)
		scanned_js += 'get_value["update_value_id"] = data_id;'
		scanned_js += 'get_value["update_value"] = val;'
		scanned_js += '$.post(url, get_value, function(result){'
		scanned_js += '$("#updated-modal").modal("show");'
		scanned_js += '});'
		scanned_js += '}else{'
		scanned_js += '};'
		scanned_js += '}, 300);';
		scanned_js += '});' # END scanned-document-editing focustout event 
		
		scanned_folders = Folder.objects.filter(~Q(name=''))

		for folders in scanned_folders:
			scanned_sub_folders = SubFolder.objects.filter(Q(folder=folders) & Q(extra_sub_folder__name=' '))
			scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false"><strong>%s</strong></p>' % (folders.slug_name().lower(), folders)
			scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % str(folders).lower() # START of Class PANEL
			scanned_document_html += '<div class="panel-body padding-top-bottom-negator">'
			for sub_folders in scanned_sub_folders: # START of Class PANEL-BODY
				scanned_upload_button = ""
				uploads = ""
				archive_button = ""
				if sub_folders.upload == True:
					scanned_upload_button = '<button class="btn btn-primary event-propagation modal-show-id-based" id="%s-upload">UPLOAD</button>' % sub_folders.slug_name().lower()
					uploads = File.objects.filter(user=user_profile).filter(location=sub_folders).filter(archive=False)
				archives = File.objects.filter(user=user_profile).filter(location=sub_folders).filter(archive=True)
				if archives:
					archive_button = '<button class="btn btn-warning event-propagation archive-show-button" data-location="%s" data-params="True">ARCHIVES</button> <button class="btn btn-success event-propagation archive-show-button hide" data-location="%s" data-params="False">UNARCHIVED</button>' % (sub_folders.id, sub_folders.id )
				scanned_document_html += '<div class="panel-body padding-top-bottom-negator">' # START class.panel-body
				scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false" style="background:#006400"><strong>%s</strong> %s %s <button class="btn btn-danger event-propagation archive-process-button hide">ARCHIVE SELECTED FILES</button> </p>' % ( sub_folders.slug_name().lower(), sub_folders.name, scanned_upload_button, archive_button)
				if uploads:
					scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % sub_folders.slug_name().lower() # START class.panel-collapse
					scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
					scanned_document_html += '<h4 style="color:#00aeef;">NOTE: <i>To update simply click the underlined value</i></h4>'
					for upload in uploads:
						scanned_document_html += '<div class="col-md-3 text-center">'
						scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
						scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'
						scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
						scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
						scanned_document_html += '<h5>%s</h5>' % upload.file_name()
						file_infos = FileFieldValue.objects.filter(file=upload)
						for file_info in file_infos:
							scanned_document_html += '<h5>%s: <u class="scanned-document-editables" data-toggle="tooltip" title="Click to Update" data-id="%s" data-classes="%s" data-type="%s">%s</u></h5>' % (file_info.field.name, file_info.id, file_info.field.classes, file_info.field.type, file_info.value)
						scanned_document_html += '<h5>Updated By: %s</h5>' % upload.uploaded_by.code
						scanned_document_html += '<h5>Uploaded Date:%s</h5>' % upload.uploaded_date
						scanned_document_html += '</div>'
						scanned_document_html += '</div>'
					scanned_document_html += '</div>' # END class.panel-collapse
				scanned_document_html += '<div class="modal fade modal-size-500" id="modal-%s-upload" tabindex="-1" role="dialog">' % sub_folders.slug_name().lower()  # START MODAL UPLOAD
				scanned_document_html += '<div class="modal-dialog" role="document">' # START modal-dialog
				scanned_document_html += '<form method="POST" enctype="multipart/form-data" id="scan-form">' # START scan-form
				scanned_document_html += '<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % get_token(request)
				scanned_document_html += '<div class="modal-content">' # START modal-content
				scanned_document_html += '<div class="modal-header">' # START modal-header
				scanned_document_html += '<h4 class="modal-title" id="signatureLabel">UPLOAD %s <button type="button" class="close" data-dismiss="modal">&times;</button></h4>' % sub_folders.name
				scanned_document_html += '<div class="modal-body text-center">' # START modal-body
				fields = Fields.objects.filter(location=sub_folders)
				if fields:
					for field in fields:
						location = str(field.location).replace("/", "-").lower()
						name = field.name.replace(" ", "-").lower()
						input_id = "id-%s-%s" % (name, location)
						label = "<label for='%s' class='input-group-addon input-label'>%s:<label>" % (input_id, field.name)
						scanned_document_html += '<div class="input-group">' # START input-group
						scanned_document_html += '<label for="%s" class="input-group-addon input-label">' % input_id
						scanned_document_html += '%s' % field.name
						scanned_document_html += '</label>'
						scanned_document_html += str(field)
						scanned_document_html += '</div>' # END input-group
					scanned_document_html += '<div class="input-group">' # START input-group
					scanned_document_html += '<label class="input-group-addon input-label">'
					scanned_document_html += 'File Upload: '
					scanned_document_html += '</label>'
					scanned_document_html += '<input type="file" name="scan-file" required>'
					scanned_document_html += '<input type="hidden" name="folder-location" value="%s">' % sub_folders.name
					scanned_document_html += '</div>' # END input-group
				else:
					scanned_document_html += '<h3>NO FIELDS HAS BEEN CONFIGURED YET ON THIS FOLDER</h3>'
				scanned_document_html += '</div>' # END modal-body
				if fields:
					scanned_document_html += '<div class="modal-footer">' # START modal-footer
					scanned_document_html += '<button class="btn btn-primary" name="scan-submit">SUBMIT</button>'
					scanned_document_html += '</div>' # END modal-footer
				scanned_document_html += '</div>' # END modal-header
				scanned_document_html += '</div>' # END modal-content
				scanned_document_html += '</form>' # END scan-form
				scanned_document_html += '</div>' # END modal-dialog
				scanned_document_html += '</div>' # END MODAL UPLOAD
				scanned_document_html += '</div>' # END class.panel-body

				# START EXTRA SUB FOLDERS SECTION
				_scanned_sub_folders = SubFolder.objects.filter(Q(folder=folders) & Q(extra_sub_folder=sub_folders))
				if _scanned_sub_folders:
					scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % (sub_folders.slug_name().lower()) # START panel on _scanned_sub_folders variable
					for _sub_folders in _scanned_sub_folders:
						scanned_document_html += '<div class="panel-body padding-top-bottom-negator">' # START panel-body on _scanned_sub_folders variable
						scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false" style="background:#00BFFF"><strong>%s</strong> <button class="btn btn-primary">UPLOAD</button></p>' % (_sub_folders.slug_name().lower(), str(_sub_folders.name))
						scanned_document_html += '</div>' # END panel-body on _scanned_sub_folders variable
					scanned_document_html += '</div>' # END panel on _scanned_sub_folders variable
				# END EXTRA SUB FOLDERS SECTION


			scanned_document_html += '</div>' # END of Class PANEL-BODY
			scanned_document_html += '</div>' # END of Class PANEL

		# Script conditional on AJAX update scanned document request
		if 'update_value_id' in request.POST and 'update_value' in request.POST:
			update_value = FileFieldValue.objects.get(id=request.POST['update_value_id'])
			update_value.value = request.POST['update_value']
			update_value.save()

		# Script conditional on adding scanned document
		if 'scan-submit' in request.POST and 'scan-file' in request.FILES:
			try:
				request.POST = dict(request.POST)
				_file = request.FILES['scan-file']
				location = request.POST['folder-location'][0]
				location = SubFolder.objects.get(name=location)
				_file = File.objects.create(user=user_profile, uploaded_by=current_user, location=location, name=_file)
				request.POST.pop('csrfmiddlewaretoken')
				request.POST.pop('scan-submit')
				request.POST.pop('folder-location')
				for x in request.POST:
					value = request.POST[x][0]
					field = Fields.objects.get(slug=x)
					FileFieldValue.objects.create(file=_file, field=field, value=value)
			except:
				print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		# Script conditional on filtering via archive and unarchive
		if 'location' in request.GET and 'folder' in request.GET and 'condition' in request.GET:
			condition = request.GET['condition']
			condition = condition in ['True']
			uploads = File.objects.filter(user=user_profile).filter(location=request.GET['location']).filter(archive=condition)
			scanned_document_html = '<div class="form-group">' # START class.form-group
			scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
			for upload in uploads:
				scanned_document_html += '<div class="col-md-3 text-center">'
				scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
				scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'
				scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
				if not condition:
					scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
				scanned_document_html += '<h5>%s</h5>' % upload.file_name()
				file_infos = FileFieldValue.objects.filter(file=upload)
				for file_info in file_infos:
					if condition:
						scanned_document_html += '<h5>%s: %s</h5>' % (file_info.field.name, file_info.value)
					else:
						scanned_document_html += '<h5>%s: <u class="scanned-document-editables" data-toggle="tooltip" title="Click to Update" data-id="%s" data-classes="%s" data-type="%s">%s</u></h5>' % (file_info.field.name, file_info.id, file_info.field.classes, file_info.field.type, file_info.value)
				scanned_document_html += '<h5>Updated By: %s</h5>' % upload.uploaded_by.code
				scanned_document_html += '<h5>Uploaded Date:%s</h5>' % upload.uploaded_date
				scanned_document_html += '</div>'
				scanned_document_html += '</div>'
			scanned_document_html += '</div>' # END class.form-group
			return HttpResponse(scanned_document_html)

		if 'delete_id_list' in request.POST:
			delete_id_list = request.POST['delete_id_list']
			delete_id_list = delete_id_list.split(',')
			query = File.objects.filter(id__in=delete_id_list)
			location = query[0].location
			for x in query:
				x.archive = True
				x.save()
			uploads = File.objects.filter(user=user_profile).filter(location=location).filter(archive=False)
			scanned_document_html = '<div class="form-group">' # START class.form-group
			scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
			for upload in uploads:
				scanned_document_html += '<div class="col-md-3 text-center">'
				scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
				scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'
				scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
				scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
				scanned_document_html += '<h5>%s</h5>' % upload.file_name()
				file_infos = FileFieldValue.objects.filter(file=upload)
				for file_info in file_infos:
					scanned_document_html += '<h5>%s: %s</h5>' % (file_info.field.name, file_info.value)
				scanned_document_html += '<h5>Updated By: %s</h5>' % upload.uploaded_by.code
				scanned_document_html += '<h5>Uploaded Date:%s</h5>' % upload.uploaded_date
				scanned_document_html += '</div>'
				scanned_document_html += '</div>'
			scanned_document_html += '</div>' # END class.form-group
			return HttpResponse(scanned_document_html)

		# END Objects for scanning documents

		# the name of the mariner
		applicant_name_form = ApplicantNameForm(instance=user_profile)
		personal_data_form = PersonalDataForm(request.POST or None, instance=personal_data, initial={'birth_place':personal_data.birth_place, 'preferred_vessel_type':personal_data.preferred_vessel_type, 'dialect':personal_data.dialect})
		personal_data_father_form = PersonalDataFatherForm(request.POST or None, instance=personal_data)
		personal_data_mother_form = PersonalDataMotherForm(request.POST or None, instance=personal_data)
		personal_data_civil_status_form = PersonalDataCivilStatusForm(request.POST or None, instance=personal_data)
		permanent_address_form = PermanentAddressForm(request.POST or None, instance=personal_data.permanent_address, initial={'permanent_zip':personal_data.permanent_address.permanent_zip.zip, 'permanent_barangay':personal_data.permanent_address.permanent_zip.barangay, 'permanent_municipality':personal_data.permanent_address.permanent_zip.municipality})
		current_address_form = CurrentAddressForm(request.POST or None, instance=personal_data.current_address, initial={'current_zip':personal_data.current_address.current_zip.zip, 'current_barangay':personal_data.current_address.current_zip.barangay, 'current_municipality':personal_data.current_address.current_zip.municipality})

		try:
			spouse = Spouse.objects.get(user=id)
			spouse_form = SpouseForm(request.POST or None, instance=spouse)
		except:
			spouse = ''
			spouse_form = SpouseForm(request.POST or None, initial={'user':personal_data.name, } )

		# Used for formset updating / inlineformset_factory
		CollegeFormSet = inlineformset_factory(UserProfile, College, extra=0, can_delete=False, form=CollegeForm )
		college_form = CollegeFormSet(request.POST or None, instance=user_profile, queryset=College.objects.filter().order_by('-collegeyear_to'))

		# sample = [{'emergency_municipality':'Quezon City', 'emergency_barangay':'Holy Spirit', 'emergency_zip':1127}]
		EmergencyContactFormSet = inlineformset_factory(UserProfile, EmergencyContact, extra=0, can_delete=False, form=EmergencyContactForm )
		emergency_contact_form = EmergencyContactFormSet(request.POST or None, instance=user_profile)

		dependents = Dependents.objects.filter(user=id)
		if len(dependents) < 1:
			dependents_num_extra = 1
			dependents_num_label = "No dependets yet"
		else:
			dependents_num_extra = 0
			dependents_num_label = len(dependents)
		DependentsFormSet = inlineformset_factory(UserProfile, Dependents, extra=dependents_num_extra, can_delete=False, form=DependentsForm )
		dependents_form = DependentsFormSet(request.POST or None, instance=user_profile)

		FlagFormSet = inlineformset_factory(FlagDocuments, FlagDocumentsDetailed, extra=0, can_delete=False, form=FlagForm)
		flag_form = FlagFormSet(request.POST or None, instance=flag_documents, queryset=FlagDocumentsDetailed.objects.filter(flags__manship_standard=True))

		TrainingCertificateFormSet = inlineformset_factory(TrainingCertificateDocuments, TrainingCertificateDocumentsDetailed, extra=0, can_delete=False, form=TrainingCertificateForm)
		trainings_certificate_form = TrainingCertificateFormSet(request.POST or None, instance=trainings_certificate_documents, queryset=TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificates__national_certificate=False))
		national_trainings_certificate_form = TrainingCertificateFormSet(request.POST or None, instance=trainings_certificate_documents, queryset=TrainingCertificateDocumentsDetailed.objects.filter(trainings_certificates__national_certificate=True))


		SeaServiceFormSet = inlineformset_factory(UserProfile, SeaService, extra=0, can_delete=False, form=SeaServiceForm )
		sea_service_form = SeaServiceFormSet(request.POST or None, instance=user_profile, queryset=SeaService.objects.filter().order_by('-date_left'))

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
			elif len(land_employment) == 2:
				num_extra = 0
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
			elif len(beneficiary) == 2:
				num_extra = 0
			BeneficiaryFormSet = inlineformset_factory(UserProfile, Beneficiary, fk_name='user', extra=num_extra, can_delete=True, form=BeneficiaryForm )
			beneficiary_form = BeneficiaryFormSet(request.POST or None, instance=user_profile )

		except:
			print "%s - %s" % (sys.exc_info()[0], sys.exc_info()[1])

		try:
			allotee = Allotee.objects.filter(user=id)
			if len(allotee) == 1:
				num_extra = 1
			elif len(allotee) < 1:
				num_extra = 2
			elif len(allotee) == 2:
				num_extra = 0
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
			evaluation_form = EvaluationForm(request.POST or None, initial={'user': personal_data.name, 'evaluated_by': current_user} )
		
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
		mariners_picture_form = MarinersChangePicture(request.POST or None, request.FILES or None, instance=mariners_profile, initial={'picture_last_modified':now})


		template = "mariner-profile/profile.html"

		context_dict = {}

		# form variables
		context_dict['applicant_name_form'] = applicant_name_form
		context_dict['personal_data_form'] = personal_data_form
		context_dict['personal_data_father_form'] = personal_data_father_form
		context_dict['personal_data_mother_form'] = personal_data_mother_form
		context_dict['personal_data_civil_status_form'] = personal_data_civil_status_form
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
		context_dict['national_trainings_certificate_form'] = national_trainings_certificate_form
		context_dict['evaluation_form'] = evaluation_form
		context_dict['sea_service_form'] = sea_service_form
		context_dict['mariner_status_form'] = mariner_status_form
		context_dict['mariners_position_form'] = mariners_position_form
		context_dict['mariners_picture_form'] = mariners_picture_form

		# queryset variables
		context_dict['user_profile'] = user_profile
		context_dict['mariners_profile'] = mariners_profile
		context_dict['picture_age_indicator'] = picture_age_indicator
		context_dict['current_history'] = current_history
		context_dict['histories'] = histories
		context_dict['current_evaluation'] = current_evaluation
		context_dict['evaluations'] = evaluations
		context_dict['spouse'] = spouse
		context_dict['dependents'] = dependents

		context_dict['title'] = "Mariner's Profile - "+str(personal_data).upper()
		context_dict['dependents_num_label'] = dependents_num_label

		context_dict['personal_data'] = personal_data

		# START ScannedVariables
		context_dict['scanned_document_html'] = mark_safe(scanned_document_html)
		context_dict['scanned_js'] = mark_safe(scanned_js)

		# END ScannedVariables

		if request.GET and 'status' in request.GET:
			from application_form.models import ApplicationForm
			mariners_profile.status = 0
			mariners_profile.status_last_modified = now
			mariners_profile.save()
			_status = Status.objects.get(status="Reverted from Mariners Profile")
			application_form = ApplicationForm.objects.get(user=id)
			application_form.status = _status
			application_form.save()
			return HttpResponseRedirect('/application-profile/'+user_profile.slug)

		if request.method == "POST":
			print request.POST
			print request.FILES

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
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/educational-information.html"
				return render(request, template, context_dict)
			
			if 'landemployment_set-0-user' in request.POST:
				if land_employment_form.is_valid():
					for land_employment in land_employment_form:
						land_employment.save()
				else:
					print land_employment_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/land-employment.html"
				return render(request, template, context_dict)

			if 'beneficiary_set-0-user' in request.POST:
				if beneficiary_form.is_valid():
					for beneficiary in beneficiary_form:
						beneficiary.save()
				else:
					print beneficiary_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/beneficiary.html"
				return render(request, template, context_dict)

			if 'allotee_set-0-user' in request.POST:
				if allotee_form.is_valid():
					for allotee in allotee_form:
						allotee.save()
				else:
					print allotee_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/allotment.html"
				return render(request, template, context_dict)

			if 'evaluation' in request.POST:
				if evaluation_form.is_valid():
					evaluation_form.save()
				else:
					print evaluation_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/evaluation.html"
				return render(request, template, context_dict)

			if 'mariner_status' in request.POST:
				if mariner_status_form.is_valid():
					mariner_status_form.save()
				else:
					print mariner_status_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/mariner-status.html"
				return render(request, template, context_dict)

			if 'flagdocumentsdetailed_set-0-flags_documents' in request.POST:
				if flag_form.is_valid():
					for flag in flag_form:
						flag.save()
				else:
					print flag_form.errors
				context_dict['ajax_submit_flag'] = 1
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
				context_dict['ajax_submit_flag'] = 1
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
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/coc_visas.html"
				return render(request, template, context_dict)

			if 'trainingcertificatedocumentsdetailed_set-0-trainings_certificate_documents' in request.POST:
				if request.POST['param']:
					if request.POST['param'] == 'National':
						html = 'national-certificates'
						if national_trainings_certificate_form.is_valid():
							for national_trainings_certificate in national_trainings_certificate_form:
								national_trainings_certificate.save()
						else:
							print national_trainings_certificate_form.errors
					else:
						html = 'certificates'
						if trainings_certificate_form.is_valid():
							for trainings_certificate in trainings_certificate_form:
								trainings_certificate.save()
						else:
							print trainings_certificate_form.errors
				context_dict['ajax_submit_flag'] = 1
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'code' in request.POST or 'first_name' in request.POST or 'first_name' in request.POST or 'middle_name' in request.POST:
				if personal_data_form.is_valid():
					personal_data_form.save()
				else:
					print personal_data_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'permanent_unit' in request.POST or 'permanent_zip' in request.POST or 'permanent_barangay' in request.POST or 'permanent_street' in request.POST:
				if permanent_address_form.is_valid():
					permanent_address_form.save()
				else:
					print permanent_address_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'current_unit' in request.POST or 'current_zip' in request.POST or 'current_barangay' in request.POST or 'current_street' in request.POST:
				if current_address_form.is_valid():
					current_address_form.save()
				else:
					print current_address_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)
			
			
			if 'father_first_name' in request.POST or 'father_first_name' in request.POST or 'father_middle_name' in request.POST:
				if personal_data_father_form.is_valid():
					personal_data_father_form.save()
				else:
					print personal_data_father_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'mother_first_name' in request.POST or 'mother_first_name' in request.POST or 'mother_middle_name' in request.POST:
				if personal_data_mother_form.is_valid():
					personal_data_mother_form.save()
				else:
					print personal_data_mother_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'civil_status' in request.POST or 'spouse_first_name' in request.POST or 'spouse_first_name' in request.POST or 'spouse_middle_name' in request.POST:
				if spouse_form.is_valid() and personal_data_civil_status_form.is_valid():
					spouse_form.save()
					personal_data_civil_status_form.save()
				else:
					print spouse_form.errors
					print personal_data_civil_status_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'dependents_set-0-dependent_relationship' in request.POST or 'dependents_set-0-dependent_zip' in request.POST or 'dependents_set-0-dependent_last_name' in request.POST or 'dependents_set-0-dependent_first_name' in request.POST or 'dependents_set-0-dependent_middle_name' in request.POST or 'dependents_set-0-user' in request.POST:
				print "DEANSSSSSSSSSs"
				if dependents_form.is_valid():
					for dependents in dependents_form:
						dependents.save()
				else:
					print dependents_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = request.POST['param']
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'emergencycontact_set-0-emergency_last_name' in request.POST or 'emergencycontact_set-0-emergency_middle_name' in request.POST or 'emergencycontact_set-0-emergency_first_name' in request.POST or 'emergencycontact_set-0-user' in request.POST:
				if emergency_contact_form.is_valid():
					for emergency_contact in emergency_contact_form:
						emergency_contact.save()
				else:
					print emergency_contact_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = 'emergency'
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'seaservice_set-0-vessel_type' in request.POST or 'seaservice_set-0-vessel_name' in request.POST or 'seaservice_set-0-year_built' in request.POST:
				if sea_service_form.is_valid():
					for sea_service in sea_service_form:
						sea_service.save()
				else:
					print sea_service_form.errors
				context_dict['ajax_submit_flag'] = 1
				html = 'sea-service'
				template = "mariner-profile/ajax-update-sub-profiles/%s.html" % html
				return render(request, template, context_dict)

			if 'picture' in request.FILES:
				if mariners_picture_form.is_valid():
					mariners_picture_form.save()
				else:
					print mariners_picture_form.errors
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

			else:
				return HttpResponse('SECTION STILL IN DEVELOPMENT')

			

			# if applicant_name_form.is_valid():
			# 	applicant_name_form.save()
			# else:
			# 	print applicant_name_form.errors

		return render(request, template, context_dict)

# Real Time delete on a formset
@login_required()
def delete_on_form_set(request):
	id=request.GET['id']
	if id:	
		college = College.objects.get(id=id)
		college.delete()
	return HttpResponse('')