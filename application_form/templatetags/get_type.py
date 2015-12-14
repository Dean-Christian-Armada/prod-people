from django import template
import urllib, base64

from io import StringIO

register = template.Library()

# Used in training-certificates.html
@register.filter
def get_type(value):
	return str(type(value))