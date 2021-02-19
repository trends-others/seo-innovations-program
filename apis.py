#Start the program 

## Payload
device_info_payload = [
    {
        "id": 1,
        "brand": "Cisco",
        "model": "Catalyst 9600 Series 6-slot",
        "description": "State-of-the-art high availability with N+1 power and fan redundancy ",
        "ip_address":"192.168.1.1",
        "status" : 0
    },
    {
        "id": 2,
        "brand": "Alcatel Lucent",
        "model": "OmniSwitch 6450",
        "description": "Stackable Gigabit Ethernet LAN Switch",
        "ip_address":"192.168.1.2",
        "status" : 1
    },
    {
        "id": 3,
        "brand": "Ruckus",
        "model": "Ruckus R750",
        "description": "8 Stream AP with wi-Fi 6(802.11ax)",
        "ip_address":"192.168.1.3",
        "status" : 1
    },
    {
        "id": 4,
        "brand": "Ruckus",
        "model": "Ruckus R750",
        "description": "8 Stream AP with wi-Fi 6(802.11ax)",
        "ip_address":"192.168.1.4",
        "status" : 1
    },
    {
        "id": 5,
        "brand": "Alcatel Lucent",
        "model": "OmniSwitch 6450",
        "description": "Stackable Gigabit Ethernet LAN Switch",
        "ip_address":"192.168.1.5",
        "status" : 1,

    }
]


## APIs


## Add Device info on existing payload using POST Method
{
        "id": 5,
        "brand": "Alcatel Lucent",
        "model": "OmniSwitch 6450",
        "description": "Stackable Gigabit Ethernet LAN Switch",
        "ip_address":"192.168.1.5",
        "status" : 1,

}

## List of Devices with status 0 using GET method
{
        "id": 1,
        "brand": "Cisco",
        "model": "Catalyst 9600 Series 6-slot",
        "description": "State-of-the-art high availability with N+1 power and fan redundancy ",
        "ip_address":"192.168.1.1",
        "status" : 0,
}

## Update the device status from 0 to 1 using Id and PUT Method

{
        "id": 1,
        "brand": "Cisco",
        "model": "Catalyst 9600 Series 6-slot",
        "description": "State-of-the-art high availability with N+1 power and fan redundancy ",
        "ip_address":"192.168.1.1",
        "status" : 1,
}

## Delete 1 device info using Id and Delete Method