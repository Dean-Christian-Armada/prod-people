from django import template

from mariners_profile.models import Company, PersonReference

import urllib, cStringIO, base64

register = template.Library()

# Used in profiles html
@register.filter
def get_data_company(value):
	try:
		company = Company.objects.get(id=value)
	except:
		company = ""
	return str(company)

@register.filter
def get_data_person_contacted(value):
	try:
		person_reference = PersonReference.objects.get(id=value)
	except:
		person_reference = ""
	return str(person_reference)