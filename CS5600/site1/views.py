from django.shortcuts import render
from django.http import HttpResponse

def site1Test(request):
	return HttpResponse("Successfully connected to SITE1")