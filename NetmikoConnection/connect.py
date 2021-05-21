from netmiko import ConnectHandler

class NetmikoConnection():
    def __init__(self, device_type, host, username,password):
        device = {
            'device_type': device_type,
            'host':   host,
            'username': username,
            'password': password    
        }
        self.net_connect = ConnectHandler(**device)

    def SendCommand(self,command):
        output = self.net_connect.send_command(command,use_textfsm=True)
        return(output)
