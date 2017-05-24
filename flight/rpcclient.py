#!/usr/bin/env python3

import argparse
import xmlrpc.client

class EC2MonitorClient():
    def __init__(self,url):
        self.server_url = url
        self.server_proxy = None
        self.name='flight'
        self.password='flight_password'
        
    def connect(self):
        """
        Connect successfully return True. Otherwise return False
        """
        ret = True
        try:
            self.server_proxy = xmlrpc.client.ServerProxy(self.server_url)
        except ConnectionRefusedError as e:
            ret = False
        finally:
            return ret
        
    def check_flight_task_status(self):
        """
        Check flight task is running or not.
        return True if task is running.
        """
        try:
            process_num = self.server_proxy.check_process(self.name,self.password)
        except ConnectionRefusedError as e:
            return False
        
        if process_num > 0:
            return True
        else:
            return False
        
    def get_flight_results_staus(self):
        """
        Return the finished number of results
        """
        try:
            fin_results_num = self.server_proxy.check_results(self.name,self.password)
        except ConnectionRefusedError as e:
            return 0
        
        return fin_results_num
 
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
