from django.shortcuts import render
from .models import Notices
def index(request):
        model= Notices
        return render(request, 'home/homepage.html')
	
def hvisits(request):
	return render(request, 'home/hvisits.html')

def outofhours(request):
	return render(request, 'home/outofhours.html')
	
def chaperones(request):
	return render(request, 'home/chaperones.html')

def leaflets(request):
	return render(request, 'home/leaflets.html')

def newpatients(request):
	return render(request, 'home/newpatients.html')

def vaccines(request):
	return render(request, 'home/vaccines.html')

def carers(request):
	return render(request, 'home/carers.html')
	
def candc(request):
	return render(request, 'home/candc.html')

def equalopps(request):
	return render(request, 'home/equalopps.html')

def datapro(request):
	return render(request, 'home/datapro.html')
	
def nhscon(request):
	return render(request, 'home/nhscon.html')
