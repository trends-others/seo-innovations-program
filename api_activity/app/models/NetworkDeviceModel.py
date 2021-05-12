from app import db

class NetworkDevice(db.Model):
    __tablename__ = 'network_device'

    id = db.Column(db.Integer, primary_key=True)
    interface = db.Column(db.String(50))
    ip_address = db.Column(db.String(50))
    status = db.Column(db.String(50))
    proto = db.Column(db.String(50))