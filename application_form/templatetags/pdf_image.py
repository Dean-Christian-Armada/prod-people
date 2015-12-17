from django import template
import urllib.request, base64
from io import BytesIO

register = template.Library()

# Used in the pdf form templates, /templates/principals-application-form/pdf/*
# Used in the pdf form templates, /templates/application_form/pdf-xxxxxxxxx.html/*
@register.filter
def get64(value, url):
    """
    Method returning base64 image data instead of URL for PDF output
    """
    if url.startswith("http"):
    	image = BytesIO(urllib.request.urlopen(url).read())
    	return 'data:image/jpg;base64,' + str(base64.b64encode(image.read()))
    return url


@register.filter
def get_type(value):
	return type(value)