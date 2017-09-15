from django.shortcuts import render
from django.http import HttpResponse

from .models import Route,RouteTask
import datetime

# Create your views here.

def get_a_task(request):
    """
    Get a route task. If routetask is empty for today then create it.
    """
    d1= datetime.datetime.today().date()
    route_list = RouteTask.objects.filter(task_date=d1)
    if route_list:
        return HttpResponse("{}".format(route_list[0]))
    else:
        create_today_tasks()
        return HttpResponse("Rout is not there, creating it...")
        
    
def update_task(request,route_id):
    """
    This let node update the task status.
    Here the task means the route id based task
    """
    route_task = RouteTask.objects.get(route__id=route_id)
    
    if route_task:
        route_task.node_name='node1'
        route_task.task_status=RouteTask.TASK_RUNNING_STATE_CHOICES[2][0]
        route_task.end_time = datetime.datetime.today().time()
        route_task.save()
        return HttpResponse("Updated the route task {}".format(route_task.route.id))
    else:
        return HttpResponse("Can't find the route task {}".format(route_task.route.id))
        
def create_today_tasks():
    route_list = Route.objects.all()
    
    td = datetime.datetime.today()
    d1= td.date()
    t1 = td.time()
    
    for route in route_list:
        RouteTask.objects.create(route=route,
                                 task_date=d1,
                                 start_time = t1,
                                 end_time = t1)