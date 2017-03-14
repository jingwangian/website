from django.db import models

# Create your models here.
class FlightPriceQueryTask(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    execute_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flight_price_query_task'
        
    def __str__(self):
        return str(self.flight_id)+'-'+self.execute_date.strftime('Y-m-d')
    
class FlightTaskStatus(models.Model):
    total_tasks = models.IntegerField(blank=True, null=True)
    success_tasks = models.IntegerField(blank=True, null=True)
    total_records = models.IntegerField(blank=True, null=True)
    workers = models.IntegerField(blank=True, null=True)
    task_start_time = models.DateTimeField(blank=True, null=True)
    task_finished_time = models.DateTimeField(blank=True, null=True)
    execute_date = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'flight_task_status'
        
    def __str__(self):
        ret_str=''
        ret_str = self.execute_date.isoformat()
        ret_str = ret_str+' , total tasks : '+str(self.total_tasks)
        ret_str = ret_str+' , success tasks : '+str(self.success_tasks)
        ret_str = ret_str+' , total records: '+str(self.total_records)
        ret_str = ret_str+' , workers: '+str(self.workers)
        ret_str = ret_str+' , start time : '+self.task_start_time.strftime('%H:%M')
        ret_str = ret_str+' , end time : '+self.task_finished_time.strftime('%H:%M')
        
        return ret_str