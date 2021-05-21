from NetmikoConnection.connect import NetmikoConnection
from api.request import ApiCall

netmiko_connection = NetmikoConnection('cisco_ios' , '10.20.19.253' , 'admin' , 'tr3nds')


netmiko_output = netmiko_connection.SendCommand('show ip int brief')


connection = ApiCall('http://localhost:5000')


for interface in netmiko_output:
    payload = {
        'interface' : interface["intf"],
        'ip_address' : interface["ipaddr"],
        'status' : interface["status"],
        'proto' :interface["proto"]
    }

    connection.insert('/network-device' ,payload )

    # print('{0} is {1}'.format(interface["intf"] , interface["status"]) )
    # print(interface)
    # print(interface["intf"])