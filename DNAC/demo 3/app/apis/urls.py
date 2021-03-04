from app import api
from app.resources.networkdevice_api import NetworkDeviceAPI

api.add_resource(NetworkDeviceAPI, '/network-devices')