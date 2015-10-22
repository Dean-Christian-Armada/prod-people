from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
	template = "sample.html"
	context_dict = {}
	return render(request, template, context_dict)
