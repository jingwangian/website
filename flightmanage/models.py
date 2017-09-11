from django.db import models

# Create your models here.

class City(models.Model):
    id = models.IntegerField(primary_key=True,db_index=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=250)
    
    def __str__(self):
        return '{}--{}--{}--{}'.format(self.id,self.name,self.short_name,self.url_name)

class Route(models.Model):
    id = models.IntegerField(primary_key=True,db_index=True)
    from_city = models.ForeignKey(
                City,
                null=True,
                on_delete=models.CASCADE,
                related_name="from_city",
                related_query_name='fromcity')
    
    to_city = models.ForeignKey(
                City,
                null=True,
                on_delete=models.CASCADE,
                related_name="to_city",
                related_query_name='tocity')
    
    def get_table_name(self):
        return  'flight_{}_{}_price'.format(self.from_city.id,self.to_city.id)
     
    def __str__(self):
        return '{}---{}---{}'.format(self.id,self.from_city.name, self.to_city.name)
    
class RouteTask(models.Model):
    TASK_RUNNING_STATE_CHOICES = (
    ('idle', 'not start'),
    ('running', 'running'),
    ('done', 'finished'),
)
    route = models.ForeignKey('Route')
    node_name = models.CharField(max_length=50,null=True,blank=True)
    task_status = models.CharField(max_length=10,choices=TASK_RUNNING_STATE_CHOICES,default='idle')
    task_date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    
    def create_today_task(self):
        route_list = Route.objects.all()
        [print(route) for route in route_list]
    
class RouteTaskHistory(models.Model):
    TASK_RUNNING_STATE_CHOICES = (
    ('idle', 'not start'),
    ('running', 'running'),
    ('done', 'finished'),
)
    route = models.ForeignKey('Route')
    node_name = models.CharField(max_length=50)
    task_status = models.CharField(max_length=10,choices=TASK_RUNNING_STATE_CHOICES,default='idle')
    task_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()