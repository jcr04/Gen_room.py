from datetime import datetime
from Infrastructure.database import db
from sqlalchemy import DateTime

class ReservationModel(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    resource_id = db.Column(db.String, db.ForeignKey('resources.id'), nullable=False)
    
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    room = db.relationship('RoomModel', back_populates='reservations')

class EventModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    organizer = db.Column(db.String(80), nullable=False)
    start_time = db.Column(DateTime, nullable=False)
    end_time = db.Column(DateTime, nullable=False)
    participants = db.Column(db.String(500))  # Armazena os participantes como string; considere normalizar isso no futuro
    description = db.Column(db.String(500), nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)

    room = db.relationship('RoomModel', back_populates='events')


    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'room_id': self.room_id,
            'organizer': self.organizer,
            'start_time': self.start_time.strftime('%d/%m/%Y %H:%M:%S'),
            'end_time': self.end_time.strftime('%d/%m/%Y %H:%M:%S'),
            'participants': self.participants.split(",") if self.participants else [],
            'description': self.description
        }
        
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def find_by_room_id(cls, room_id):
        return cls.query.filter_by(room_id=room_id).all()

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

        
# Modelo de Sala
class RoomModel(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    room_type = db.Column(db.String(80), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    room_category = db.Column(db.String(80), nullable=False)
    shift = db.Column(db.String(80), nullable=False)
    is_occupied = db.Column(db.Boolean, default=False)
    
    # Relacionamento com ReservationModel
    reservations = db.relationship('ReservationModel', back_populates='room', cascade='all, delete-orphan')
    events = db.relationship('EventModel', back_populates='room', cascade='all, delete-orphan')
    
    def __init__(self, name, room_type, capacity, description, room_category, shift):
        self.name = name
        self.room_type = room_type
        self.capacity = capacity
        self.description = description
        self.room_category = room_category
        self.shift = shift

    def __repr__(self):
        return f'RoomModel(id={self.id}, name={self.name}, room_type={self.room_type}, capacity={self.capacity}, description={self.description}, room_category={self.room_category}, shift={self.shift})'

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'capacity': self.capacity,
            'description': self.description,
            'room_category': self.room_category,
            'shift': self.shift
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def update_room(self, name=None, capacity=None, description=None):
        if name:
            self.name = name
        if capacity:
            self.capacity = capacity
        if description:
            self.description = description
        
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def reserve_room(self, start_time, end_time):
        reservation = ReservationModel(start_time=start_time, end_time=end_time)
        self.reservations.append(reservation)
        db.session.commit()

    def is_available(self, start_time, end_time):
        start_datetime = datetime.strptime(start_time, '%d/%m/%Y %H:%M:%S')
        end_datetime = datetime.strptime(end_time, '%d/%m/%Y %H:%M:%S')
        for reservation in self.reservations:
            if not (start_datetime >= reservation.end_time or end_datetime <= reservation.start_time):
                return False  # Room is not available during this period
        return True