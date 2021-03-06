from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def hw1(request):
	template = loader.get_template('hw1/hw1.html')
	return HttpResponse(template.render())

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)