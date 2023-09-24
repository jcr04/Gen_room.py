from Infrastructure.database import db

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
