from django.shortcuts import render

from .models import Route,RouteTask
# Create your views here.

def get_a_task(request):
    RouteTask.objects.filter(task_date='2017-09-10')
    
    
def create_today_tasks(request):
    route_list = Route.objects.all()
    
    RouteTask.objects.create(route=route,task_date='2017-09-10')