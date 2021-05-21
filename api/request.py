import json
import requests



class ApiCall():
    def __init__(self,host):
        self.host = host

    def insert(self, endpoint , payload):
        url = '{0}{1}'.format(self.host , endpoint)
        
        data =requests.post(url , payload , headers={'Connection' : 'close'})
        print('Success')