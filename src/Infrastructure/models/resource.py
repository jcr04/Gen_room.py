from datetime import datetime
from Infrastructure.database import db

class ResourceModel(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    is_reserved = db.Column(db.Boolean, default=False)
    
    reservations = db.relationship('ReservationModel', backref='resource', lazy=True)  # Adiciona o parâmetro lazy


    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_reserved': self.is_reserved,
            'reservations': [reservation.json() for reservation in self.reservations]
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def create_resource(cls, name, description):
        new_resource = cls(name=name, description=description)
        new_resource.save_to_db()
        return new_resource

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
