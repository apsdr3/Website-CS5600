from django.http import HttpResponse

def baseSite(request):
	return HttpResponse("Successfully connected to MAIN WEBSITE")