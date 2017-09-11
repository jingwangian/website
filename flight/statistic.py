#!/usr/bin/env python3

import argparse
import datetime

def get_estimated_time(total_task,finished_task, start_time=None):
    """
    
    """
    
    to_day=datetime.date.today()
    
    t1 = datetime.datetime(to_day.year,to_day.month,to_day.day)
    t2 = datetime.datetime.now()
    
    d1 = t2 - t1
    
    passed_seconds = d1.seconds
    left_seconds = 86400 - d1.seconds
    
    tasks_per_second =(total_task - finished_task)/ passed_seconds
    
    need_seconds = tasks_per_second * left_seconds
    
    total_seconds_needed = d1.seconds+need_seconds
    
    est_finish_task_time = t2 + datetime.timedelta(seconds=need_seconds)

    # 86400 is a total seconds of a day
    if(total_seconds_needed > 86400):
        return est_finish_task_time.strftime("%H:%M:%S")+" tomorrow"
    else:
        return est_finish_task_time.strftime("%H:%M:%S")+" today"
 
def main():
    est_time = get_estimated_time(28000,20000)
    print(est_time)

if __name__ == '__main__':
    main()
