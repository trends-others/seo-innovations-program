from app import api as url
from app.controllers.NetworkdeviceController import NetworkDeviceController

# api.add_resource(NetworkDeviceController, '/network-device')
url.add_resource(NetworkDeviceController, '/network-device')