from django.conf.urls import url

from flightmanage import views

urlpatterns = [
#     url(r'^$', views.index, name='index'),
    
    #flightm/gettask
    url(r'^gettask/$', views.get_a_task, name='get_a_task'),
    
    #flightm/updatetask/num
    url(r'^updatetask/(?P<route_id>\d+)/$', views.update_task, name='update_task')
    
    
]