from interface import *
import time
import json

while True: 
    with open('./json/devices.json', 'w') as f:
        json.dump( GetDevices().run(), f, indent=2)
    time.sleep(100)