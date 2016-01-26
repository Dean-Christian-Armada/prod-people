from django.http import HttpResponse
from django.shortcuts import render

def error404(request):
	template = "errors/404.html"
	context_dict = { }
	return render(request, template, context_dict)
	# return HttpResponse("dasdasd")