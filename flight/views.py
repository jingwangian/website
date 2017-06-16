from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import EC2Info

from .rpcclient import EC2MonitorClient
from .statistic import get_estimated_time 

# Create your views here.
def index(request):
    template = loader.get_template('flight/index.html')
    context = {
        'status_list': None
        }
    
    return HttpResponse(template.render(context,request))

def all_ec2_status(request):
    ec2_list = EC2Info.objects.all()

    ec2_status_list = []
    
    for ec2 in ec2_list:
        ec2_url='http://{}:{}'.format(ec2.public_dns,'8989')
        print(ec2_url)
        
        ec2_mc = EC2MonitorClient(ec2_url)
        if ec2_mc.connect() == False:
            ec2.status='unknown'
            continue
            
        if ec2_mc.check_flight_task_status() == True:
            ec2.status = 'running'
            print('{} is running'.format(ec2.name))
            task_dict = ec2_mc.get_task_status()
            if task_dict is not None:
                ec2.total_task_num = task_dict['total_task_num']
                ec2.finished_task_num = task_dict['finished_task_num']
                ec2.finish_time = get_estimated_time(ec2.total_task_num,ec2.finished_task_num)
            else:
                ec2.total_task_num = 0
                ec2.finished_task_num = 0
                
        else:
            ec2.status = 'not running'
            print('{} is not running'.format(ec2.name))

#         break
        
    
#     template = loader.get_template('flight/status.html')
   
    context = {
        'ec2_list': ec2_list
        }
    
#     return HttpResponse(template.render(context,request))
    return render(request, 'flight/status.html', context)
