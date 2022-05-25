from django.http import HttpResponse
from django.shortcuts import render

def automation_network_management(request):
	template = "automationNetworkManagement.html"

	return render(request, template)