# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Route

import datetime

# Create your views here.
def index(request):
    template = loader.get_template('flight/index.html')
    context = {
        'status_list': None
        }
    
    return HttpResponse(template.render(context,request))
#     return HttpResponse('You are visiting the fight website')

def status(request):
#     status_list = FlightTaskStatus.objects.all()

    date_str = datetime.date.today().strftime('%Y-%m-%d')
#     date_str = '2017-03-08'
    file_name = '''/db/github/flight/expedia/log/result_'''+date_str+'.log' 
    
    status_list = []
    
    template = loader.get_template('flight/status.html')
    
    with open(file_name) as f:
        for line in f.readlines()[-30:-1]:
            line = line.strip()
            status_list.append(line)
    
    context = {
        'status_list': status_list
        }
    
    return HttpResponse(template.render(context,request))

def route(request):
    
    route_list = Route.objects.all()
    
    template = loader.get_template('flight/route.html')

    
    context = {
        'route_list': route_list
        }
    
    return HttpResponse(template.render(context,request))