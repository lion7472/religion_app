from sqlalchemy.dialects.postgresql import JSON
from application.extensions import db, ma


class Device(db.Model):

	__tablename__ = 'device'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	device_id = db.Column(db.Integer,unique=True, nullable=True)
	versionName = db.Column(db.String(256),unique=True, nullable=True)
	applicationName = db.Column(db.String(256),unique=True, nullable=True)
	deviceName = db.Column(db.String(256),unique=True, nullable=True)
	systemName = db.Column(db.String(256),unique=True, nullable=True)


   

class DeviceSchema(ma.ModelSchema):
	class Meta:
		model = Device