from django.http import HttpResponse

def baseSite(request):
	return HttpResponse("Successfully connected to MAIN WEBSITE")

def site1(request):
	return HttpResponse("Successfully connection to SITE1")