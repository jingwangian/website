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
        est_finish_task_time.strftime("%H:%M:%S")+" tomorrow"
    else:
        est_finish_task_time.strftime("%H:%M:%S")+" today"
 
def main():
    print("Starting client")

    parser = argparse.ArgumentParser()
    parser.add_argument('--addr',default='localhost', help='ip address to listen on')
    parser.add_argument('-p','--port',default='8989', help='ip address port to listen on')
    
    args = parser.parse_args()
    
    addr = args.addr
    port = args.port
    
    server_url='http://{}:{}'.format(addr,port)
    
    print('Connect to {}'.format(server_url))
    
    s = xmlrpc.client.ServerProxy(server_url)

    name='flight'
    password='flight_password'
    process_num = s.check_process(name,password)
    results_num = s.check_results(name,password)

    print("process_num is {}".format(str(process_num)))
    print("results_num is {}".format(str(results_num)))

    print("Client stopped")
 
if __name__ == '__main__':
    main()
