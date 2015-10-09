from django import template
import urllib, cStringIO, base64

register = template.Library()

# Used in pdf templates inside application form folder
@register.filter
def get64(value, url):
    """
    Method returning base64 image data instead of URL for PDF output
    """
    if url.startswith("http"):
        image = cStringIO.StringIO(urllib.urlopen(url).read())
        return 'data:image/jpg;base64,' + base64.b64encode(image.read())
    return url