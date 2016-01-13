from cms.models import Folder, SubFolder, File, Fields, FileFieldValue

from datetime import timedelta, date
from globals_declarations.variables import _today 

import re, sys

# A scipt used for dynamic folders in picture file upload
# def content_file_name(instance, filename):
#     upload_dir = os.path.join('scanned',instance.folder_path.name)
#     return os.path.join(upload_dir, filename)

# A script to Display the overall notifications of each notifier level of all folders
def overall_converted_notifier(notifier, user):
	_return = 0
	_count = 0
	folder = Folder.objects.filter()

	for _folder in folder:
		sub_folder = SubFolder.objects.filter(folder=_folder)
		for x in sub_folder:
			_list = [ x.low_notifier, x.medium_notifier, x.high_notifier ]
			if notifier == "high":
				_notifier = x.high_notifier
				_index = _list.index(x.high_notifier)
			elif notifier == "medium":
				_notifier = x.medium_notifier
				_index = _list.index(x.medium_notifier)
			else:
				_notifier = x.low_notifier
				_index = _list.index(x.low_notifier)
			try:
				_day_notifier = int(re.search(r'\d+', _notifier).group())
				if 'month' in _notifier:
					_day_notifier = 30 * _day_notifier
				elif 'week' in _notifier:
					_day_notifier = 7 * _day_notifier
				elif 'year' in _notifier:
					_day_notifier = 365 * _day_notifier
			except:
				print ("%s - %s" % (sys.exc_info()[0], sys.exc_info()[1]))
				_day_notifier = int(_notifier)
			y = File.objects.filter(location=x).filter(user=user).filter(archive=False)
			z = Fields.objects.filter(location=x).filter(name__icontains="expir")
			a = FileFieldValue.objects.filter(field=z).filter(file=y)

			for b in a:
				expiry_date = b.value
				_expiry_date = expiry_date.split('-')
				_expiry_date = list(map(int, _expiry_date))
				_expiry_date = date( _expiry_date[0], _expiry_date[1], _expiry_date[2] )
				_day = _expiry_date - timedelta(days=_day_notifier)
				if _day < _today:
					_return += 1
					try:
						z = _list[_index+1]
						try:
							s_day_notifier = int(re.search(r'\d+', z).group())
							if 'month' in z:
								s_day_notifier = 30 *s_day_notifier
							elif 'week' in z:
								s_day_notifier = 7 * s_day_notifier
							elif 'year' in z:
								s_day_notifier = 365 * s_day_notifier
						except:
							s_day_notifier = z
						s_day = _expiry_date - timedelta(days=s_day_notifier)
						if s_day < _today:
							_return -= 1
					except:
						pass
				else:
					_return += 0
	return _return

# Custom method for page manipulation used on the index of mariners-profile and applications-profile app
def crew_retrieve_manipulation(request, method):
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