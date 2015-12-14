from django import template

from mariners_profile.models import *

from io import StringIO

import urllib, base64

register = template.Library()

# Used in profiles html
@register.filter
def get_data(value, model):
	# Method used for querying out string values of foreignkeys for inlineformsets
	try:
		model = eval(model)
		model = model.objects.get(id=value)
	except:
		model = ""
	return str(model)

@register.filter
def get_data_field(value, args):
	# Method used for querying out string values of foreignkeys and selected field for inlineformsets
	args = args.split(',')
	try:
		model = eval(args[0])
		model = model.objects.get(id=value)
		model = getattr(model, args[1])
	except:
		model = ""
	return str(model)


# @register.filter
# def get_data_person_contacted(value):
# 	try:
# 		person_reference = PersonReference.objects.get(id=value)
# 	except:
# 		person_reference = ""
# 	return str(person_reference)