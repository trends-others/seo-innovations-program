from common.auth import *
import http.client
import json

class GetDevices():

    def filter_device(self,device_list):
        filter_list = []
        for device in device_list:
            filter_list.append({
                "reachabilityStatus" : device["reachabilityStatus"],
                "macAddress" : device["macAddress"],
                "hostname" : device["hostname"]  ,
                "id":device["id"],
                "managementIpAddress" : device["managementIpAddress"],
                "upTime" : device["upTime"]
            })
        return(filter_list)

    def run(self):
        conn = http.client.HTTPSConnection("sandboxdnac.cisco.com")
        payload = ''
        headers = {
            'Content-Type': 'application/json',
            'x-auth-token': get_token()["Token"]
        }
        conn.request("GET", "/dna/intent/api/v1/network-device", payload, headers)
        res = conn.getresponse()
        data = res.read()
        device_raw = json.loads(data.decode("utf-8"))["response"]
     
        filtered = self.filter_device(device_raw)
        
        return filtered

