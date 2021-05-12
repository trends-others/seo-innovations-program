from flask_restful import Resource
from flask_restful import reqparse
from flask import jsonify
from app.models.NetworkDeviceModel import NetworkDevice
from app.models.NetworkDeviceSchema import NetworkDeviceSchema
from app import db
import json


class NetworkDeviceController(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("interface")
    parser.add_argument("ip_address")
    parser.add_argument("status")
    parser.add_argument("proto")

    def get(self):
        data = db.session.query(NetworkDevice).order_by(NetworkDevice.id.desc()).all()
        result = NetworkDeviceSchema(many=True).dump(data)
        db.session.close()
        db.engine.dispose()
        return result

    def post(self):
        args = self.parser.parse_args()
        model = NetworkDevice(**args)
        db.session.add(model)
        db.session.commit()
        return args