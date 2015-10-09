from django import template

from mariners_profile.models import *

import urllib, cStringIO, base64

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

# @register.filter
# def get_data_person_contacted(value):
# 	try:
# 		person_reference = PersonReference.objects.get(id=value)
# 	except:
# 		person_reference = ""
# 	return str(person_reference)