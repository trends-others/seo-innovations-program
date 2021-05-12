from marshmallow import Schema, fields, validate

class NetworkDeviceSchema(Schema):
    id = fields.Integer()
    interface = fields.String()
    ip_address = fields.String()
    status = fields.String()
    proto = fields.String()
