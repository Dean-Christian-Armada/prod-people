from django.shortcuts import render
from django.middleware.csrf import get_token
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings

from io import StringIO, BytesIO

from login.models import UserProfile
from cms.models import Folder, SubFolder, File, Fields, FileFieldValue
from globals_declarations.variables import fileformat_today

from datetime import date

import sys, os, zipfile, tarfile

# Create your views here.
def scanned_documents(request, user_profile):

	# START Objects for scanning documents
	
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
	scanned_js += '$(this).closest(".panel-collapse").siblings("p.cursor-pointer").find(".archive-delete-process-button").removeClass("hide");'
	scanned_js += '}else{'
	scanned_js += '$(this).closest(".panel-collapse").siblings("p.cursor-pointer").find(".archive-delete-process-button").addClass("hide");'
	scanned_js += '}'
	scanned_js += '});' # END of checkboxchange event
	scanned_js += '$(".scanned-document-modal-show-id-based").on("click", function(){' # START of scanned-document-modal-show-id-based
	scanned_js += 'id = $(this).attr("id");'
	scanned_js += 'if($(this).attr("data-file-id")){'
	scanned_js += 'data_file_id=$(this).attr("data-file-id");'
	# scanned_js += 'alert("armada");'
	# scanned_js += 'alert("#form-"+id);'
	scanned_js += '$("#form-"+id).append("<input class=\'hide\' name=\'archive-file-id\' value="+data_file_id+">");'
	scanned_js += '}'
	scanned_js += '$("#modal-"+id).modal("show");'
	scanned_js += '});' # END of scanned-document-modal-show-id-based
	scanned_js += '$(".archive-delete-process-button").click(function(){' # START of put to archive process button event
	scanned_js += 'delete_id_list = $(this).parent().next().find(".delete-id-list").val();'
	scanned_js += 'var json_archive_ids = {csrfmiddlewaretoken: "%s"};' % get_token(request)
	scanned_js += 'if($(this).attr("data-process")){'
	scanned_js += 'json_archive_ids["process"] = $(this).attr("data-process");'
	scanned_js += '};'
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
	scanned_js += '$(this).siblings(".archive-delete-process-button").addClass("hide");'
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
	scanned_js += '$(this).siblings(".archive-delete-process-button").text("DELETE SELECTED FILES");'
	scanned_js += '$(this).siblings(".archive-delete-process-button").attr("data-process", "delete");'
	scanned_js += '}else{'
	scanned_js += '$(this).prev().removeClass("hide");'
	scanned_js += '$(this).siblings(".archive-delete-process-button").text("ARCHIVE SELECTED FILES");'
	scanned_js += '$(this).siblings(".archive-delete-process-button").removeAttr("data-process");'
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
	scanned_js += '}, 300);'
	scanned_js += '});' # END scanned-document-editing focustout event
	scanned_js += '$(".scanned-document-hide-event").on("hidden.bs.modal", function(){' # START scanned-document-hide-event
	# scanned_js += 'alert("dean");'
	scanned_js += '});' # END scanned-document-hide-event
	
	scanned_folders = Folder.objects.filter(~Q(name=''))

	for folders in scanned_folders:
		scanned_sub_folders = SubFolder.objects.filter(Q(folder=folders) & Q(extra_sub_folder__name=' ')).order_by('order')
		scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false"><strong>%s</strong></p>' % (folders.slug_name().lower(), folders)
		scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % folders.slug_name() # START of Class PANEL
		scanned_document_html += '<div class="panel-body padding-top-bottom-negator">'
		for sub_folders in scanned_sub_folders: # START of Class PANEL-BODY
			scanned_upload_button = ""
			uploads = ""
			archive_button = ""
			if sub_folders.upload == True:
				scanned_upload_button = '<button class="btn btn-primary event-propagation scanned-document-modal-show-id-based" id="%s-upload">UPLOAD</button>' % sub_folders.slug_name()
				uploads = File.objects.filter(user=user_profile).filter(location=sub_folders).filter(archive=False)
			archives = File.objects.filter(user=user_profile).filter(location=sub_folders).filter(archive=True)
			if archives:
				archive_button = '<button class="btn btn-warning event-propagation archive-show-button" data-location="%s" data-params="True">ARCHIVES</button> <button class="btn btn-success event-propagation archive-show-button hide" data-location="%s" data-params="False">UNARCHIVED</button>' % (sub_folders.id, sub_folders.id )
			scanned_document_html += '<div class="panel-body padding-top-bottom-negator">' # START class.panel-body
			scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false" style="background:#006400"><strong>%s</strong> %s %s <button class="btn btn-danger event-propagation archive-delete-process-button hide">ARCHIVE SELECTED FILES</button> </p>' % ( sub_folders.slug_name().lower(), sub_folders.name, scanned_upload_button, archive_button)
			# scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false" style="background:#006400"><strong>%s</strong> %s %s <button class="btn btn-danger event-propagation delete-process-button hide" data-process="delete">DELETED SELECTED FILES</button> </p>' % ( sub_folders.slug_name().lower(), sub_folders.name, scanned_upload_button, archive_button)
			if uploads:
				scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % sub_folders.slug_name() # START class.panel-collapse
				scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
				scanned_document_html += '<h4 style="color:#00aeef;">NOTE: <i>To update simply click the underlined value</i></h4>'
				for upload in uploads:
					scanned_document_html += '<div class="col-md-3 text-center">'
					scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
					scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'	
					scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
					scanned_document_html += '<button class="btn btn-primary event-propagation scanned-document-modal-show-id-based upload-archive form-control input-group" id="%s-upload" data-file-id="%s">UPLOAD ARCHIVE</button>' % (sub_folders.slug_name(), upload.id)
					scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
					scanned_document_html += '<h5 class="break-word">%s</h5>' % upload.file_name()
					file_infos = FileFieldValue.objects.filter(file=upload)
					for file_info in file_infos:
						scanned_document_html += '<h5>%s: <u class="scanned-document-editables" data-toggle="tooltip" title="Click to Update" data-id="%s" data-classes="%s" data-type="%s">%s</u></h5>' % (file_info.field.name, file_info.id, file_info.field.classes, file_info.field.type, file_info.value)
					scanned_document_html += '<h5>Updated By: %s</h5>' % upload.uploaded_by.code
					scanned_document_html += '<h5>Uploaded Date:%s</h5>' % upload.uploaded_date
					scanned_document_html += '</div>'
					scanned_document_html += '</div>'
				scanned_document_html += '</div>' # END class.panel-collapse
			scanned_document_html += '<div class="modal fade modal-size-500 scanned-document-hide-event" id="modal-%s-upload" tabindex="-1" role="dialog">' % sub_folders.slug_name()  # START MODAL UPLOAD
			scanned_document_html += '<div class="modal-dialog" role="document">' # START modal-dialog
			scanned_document_html += '<form method="POST" enctype="multipart/form-data" class="scan-form" id="form-%s-upload">' % sub_folders.slug_name() # START scan-form
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
			_scanned_sub_folders = SubFolder.objects.filter(Q(folder=folders) & Q(extra_sub_folder=sub_folders)).order_by('order')
			if _scanned_sub_folders:
				scanned_document_html += '<div id="scanned-%s" class="panel-collapse collapse" aria-expanded="false">' % (sub_folders.slug_name()) # START panel on _scanned_sub_folders variable
				for _sub_folders in _scanned_sub_folders:
					scanned_document_html += '<div class="panel-body padding-top-bottom-negator">' # START panel-body on _scanned_sub_folders variable
					scanned_document_html += '<p class="cursor-pointer" data-toggle="collapse" data-parent="#accordion" href="#scanned-%s" aria-expanded="false" style="background:#00BFFF"><strong>%s</strong> <button class="btn btn-primary scanned-document-modal-show-id-based" id="%s-upload">UPLOAD</button></p>' % (_sub_folders.slug_name(), str(_sub_folders.name), _sub_folders.slug_name())
					scanned_document_html += '</div>' # END panel-body on _scanned_sub_folders variable
					scanned_document_html += '<div class="modal fade modal-size-500 scanned-document-hide-event" id="modal-%s-upload" tabindex="-1" role="dialog">' % _sub_folders.slug_name()  # START MODAL UPLOAD
					scanned_document_html += '<div class="modal-dialog" role="document">' # START modal-dialog
					scanned_document_html += '<form method="POST" enctype="multipart/form-data" class="scan-form" id="form-%s-upload">' % sub_folders.slug_name() # START scan-form
					scanned_document_html += '<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % get_token(request)
					scanned_document_html += '<div class="modal-content">' # START modal-content
					scanned_document_html += '<div class="modal-header">' # START modal-header
					scanned_document_html += '<h4 class="modal-title" id="signatureLabel">UPLOAD %s <button type="button" class="close" data-dismiss="modal">&times;</button></h4>' % _sub_folders.name
					scanned_document_html += '<div class="modal-body text-center">' # START modal-body
					fields = Fields.objects.filter(location=_sub_folders)
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
						scanned_document_html += '<input type="hidden" name="folder-location" value="%s">' % _sub_folders.name
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
			# dict is used to enable the for loop x
			request.POST = dict(request.POST)
			_file = request.FILES['scan-file']
			location = request.POST['folder-location'][0]
			location = SubFolder.objects.get(name=location)
			_file = File.objects.create(user=user_profile, uploaded_by=current_user, location=location, name=_file)
			if 'archive-file-id' in request.POST:
				archive_file_id = request.POST['archive-file-id'][0]
				archive_file = File.objects.get(id=archive_file_id)
				archive_file.archive = True
				archive_file.save()
				request.POST.pop('archive-file-id')
			request.POST.pop('csrfmiddlewaretoken')
			request.POST.pop('scan-submit')
			request.POST.pop('folder-location')
			for x in request.POST:
				value = request.POST[x][0]
				field = Fields.objects.get(slug=x)
				FileFieldValue.objects.create(file=_file, field=field, value=value)
		except:
			print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	# Script conditional on filtering via archive and unarchive
	if 'location' in request.GET and 'folder' in request.GET and 'condition' in request.GET:
		condition = request.GET['condition']
		condition = condition in ['True']
		uploads = File.objects.filter(user=user_profile).filter(location=request.GET['location']).filter(archive=condition)
		scanned_document_html = '<div class="form-group">' # START class.form-group
		scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
		if not condition:
			scanned_document_html += '<h4 style="color:#00aeef;">NOTE: <i>To update simply click the underlined value</i></h4>'
		for upload in uploads:
			scanned_document_html += '<div class="col-md-3 text-center">'
			scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
			scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'
			scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
			if not condition:
				scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
			else:
				scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">DELETE</label>' % (upload.id, upload.id, upload.id)
			scanned_document_html += '<h5 class="break-word">%s</h5>' % upload.file_name()
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
		condition = False
		for x in query:
			if 'process' in request.POST:
				x.delete()
				condition = True
			else:
				x.archive = True
				x.save()
		uploads = File.objects.filter(user=user_profile).filter(location=location).filter(archive=condition)
		scanned_document_html = '<div class="form-group">' # START class.form-group
		scanned_document_html += '<input type="text" class="delete-id-list hide">' # Stores the delete ids
		for upload in uploads:
			scanned_document_html += '<div class="col-md-3 text-center">'
			scanned_document_html += '<img src="%s" height="150" width="150">' % upload.logo()
			scanned_document_html += '<div class="text-left col-centered" style="width: 200px">'
			scanned_document_html += '<a class="btn btn-primary form-control input-group" href="%s" target="_blank">VIEW / DOWNLOAD</a>' % upload.download_link()
			scanned_document_html += '<input id="id_%s" type="checkbox" class="scanned_delete_checkbox" value="%s"> <label for="id_%s">PUT TO ARCHIVE</label>' % (upload.id, upload.id, upload.id)
			scanned_document_html += '<h5 class="break-word">%s</h5>' % upload.file_name()
			file_infos = FileFieldValue.objects.filter(file=upload)
			for file_info in file_infos:
				scanned_document_html += '<h5>%s: %s</h5>' % (file_info.field.name, file_info.value)
			scanned_document_html += '<h5>Updated By: %s</h5>' % upload.uploaded_by.code
			scanned_document_html += '<h5>Uploaded Date:%s</h5>' % upload.uploaded_date
			scanned_document_html += '</div>'
			scanned_document_html += '</div>'
		scanned_document_html += '</div>' # END class.form-group
		return HttpResponse(scanned_document_html)

	return (scanned_document_html, scanned_js)
	# END Objects for scanning documents

# method to compress file downloads in a zip file
def zipped(request):
	# Source: http://stackoverflow.com/questions/12881294/django-create-a-zip-of-multiple-files-and-make-it-downloadable
	list_files = []
	# START Comment below for testing purposes
	get_request = request.GET['x']
	request_ids = get_request.split(',')
	
	file_ids = File.objects.filter(id__in=request_ids)
	location_name = file_ids[0].location.name.lower()
	for x in file_ids:
		list_files.append("%s%s" % (settings.MEDIA_URL[1:], str(x.name)))
	# END Comment above for testing purposes
	# filenames = ["media/scanned/SRC/Selection_006.png", "media/scanned/SRC/mascot.png"] # Used for test purposes Uncomment this
	zip_subdir = "%s%s%s" % (fileformat_today, location_name, request.user) # the name of the zip file, comment this in testing
	# zip_subdir = "test" # Used for test purposes Uncomment this
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()

	zf = zipfile.ZipFile(s, "w")

	# for fpath in filenames: # Used for test purposes Uncomment this
	for fpath in list_files: # Comment this when testing
		# START removes the folder hierarchy like "media", "scanned", "SRC"
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		# END removes the folder hierarchy like "media", "scanned", "SRC"
		zf.write(fpath, arcname=zip_path)
	zf.close()
	resp = HttpResponse(s.getvalue(), content_type="application/zip-compressed")
	resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
	return resp

# method to compress file downloads in a tar gz file
def targz(request):
	# Source: http://stackoverflow.com/questions/908258/generating-file-to-download-with-django
	list_files = []
	# START Comment below for testing purposes
	get_request = request.GET['x']
	request_ids = get_request.split(',')
	file_ids = File.objects.filter(id__in=request_ids)
	location_name = file_ids[0].location.name.lower()
	for x in file_ids:
		list_files.append("%s%s" % (settings.MEDIA_URL[1:], str(x.name)))
	# END Comment above for testing purposes
	# filenames = ["media/scanned/SRC/Selection_006.png", "media/scanned/SRC/mascot.png"] # Used for test purposes Uncomment this
	tar_subdir = "%s%s%s" % (fileformat_today, location_name, request.user) # the name of the tar file, comment this in testing
	# tar_subdir = "test" # Used for test purposes Uncomment this
	tar_filename = "%s.tar.gz" % tar_subdir

	resp = HttpResponse(content_type="application/x-gzip")
	resp['Content-Disposition'] = 'attachment; filename=%s' % tar_filename
	tf = tarfile.open(fileobj=resp, mode="w:gz")

	# for fpath in filenames: # Used for test purposes Uncomment this
	for fpath in list_files: # Comment this when testing
		# START removes the folder hierarchy like "media", "scanned", "SRC"
		fdir, fname = os.path.split(fpath)
		tar_path = os.path.join(tar_subdir, fname)
		# END removes the folder hierarchy like "media", "scanned", "SRC"
		tf.add(fpath, arcname=tar_path)
	tf.close()
	
	return resp

# method to compress file downloads in a tar bz2 file
def tarbz2(request):
	# Source: http://stackoverflow.com/questions/27512635/python-tarfile-not-creating-valid-tar-gz-file
	list_files = []
	# START Comment below for testing purposes
	get_request = request.GET['x']
	request_ids = get_request.split(',')
	file_ids = File.objects.filter(id__in=request_ids)
	location_name = file_ids[0].location.name.lower()
	for x in file_ids:
		list_files.append("%s%s" % (settings.MEDIA_URL[1:], str(x.name)))
	# END Comment above for testing purposes
	# filenames = ["media/scanned/SRC/Selection_006.png", "media/scanned/SRC/mascot.png"] # Used for test purposes Uncomment this
	tar_subdir = "%s%s%s" % (fileformat_today, location_name, request.user) # the name of the tar file, comment this in testing
	# tar_subdir = "test" # Used for test purposes Uncomment this
	tar_filename = "%s.tar.bz2" % tar_subdir

	resp = HttpResponse(content_type="application/x-gzip")
	resp['Content-Disposition'] = 'attachment; filename=%s' % tar_filename
	tf = tarfile.open(fileobj=resp, mode="w:bz2")

	# for fpath in filenames: # Used for test purposes Uncomment this
	for fpath in list_files: # Comment this when testing
		# START removes the folder hierarchy like "media", "scanned", "SRC"
		fdir, fname = os.path.split(fpath)
		tar_path = os.path.join(tar_subdir, fname)
		# END removes the folder hierarchy like "media", "scanned", "SRC"
		tf.add(fpath, arcname=tar_path)
	tf.close()
	
	return resp