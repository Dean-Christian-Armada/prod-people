from django import template
import urllib, cStringIO, base64

register = template.Library()

@register.filter
def get_type(value):
	return str(type(value))