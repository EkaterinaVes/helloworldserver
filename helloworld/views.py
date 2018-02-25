from django.shortcuts import render, render_to_response, redirect

from django.http import HttpResponse
from django.views.generic.base import View


def name_form(request):
	return render_to_response('helloworld/nameform.html')

def getname(request):
	if 'q' in request.GET:
		return render_to_response('helloworld/greetings.html', {'name' : request.GET['q']})
	else:
		message = 'Hello, user!'
		return HttpResponse(message)
