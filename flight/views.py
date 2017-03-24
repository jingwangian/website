# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import FlightTaskStatus

# Create your views here.
def index(request):
    template = loader.get_template('flight/index.html')
    context = {
        'status_list': None
        }
    
    return HttpResponse(template.render(context,request))
#     return HttpResponse('You are visiting the fight website')

def status(request):
    status_list = FlightTaskStatus.objects.all()
    
    template = loader.get_template('flight/status.html')
    
    context = {
        'status_list': status_list
        }
    
    return HttpResponse(template.render(context,request))