class Room:
    def __init__(self, id, name, room_type=None, capacity=None, description=None, room_category=None, shift=None):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.capacity = capacity
        self.description = description
        self.room_category = room_category
        self.is_occupied = False  # Campo is_occupied definido como False por padrão
        self.reservations = []
        self.shift = shift
        self.events = []  # Lista para armazenar eventos associados a esta sala

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'room_category': self.room_category,
            'shift': self.shift,
            'events': [event.to_json() for event in self.events]  # Converta eventos em sua representação JSON
        }

    def to_detailed_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'capacity': self.capacity,
            'description': self.description,
            'room_category': self.room_category,
            'reservations': [r.to_json() for r in self.reservations],
            'shift': self.shift,
            'events': [event.to_json() for event in self.events]  # Converta eventos em sua representação JSON detalhada
        }


class Event:
    def __init__(self, id, title, organizer, start_time, end_time, participants=None, description=None):
        self.id = id
        self.title = title
        self.organizer = organizer
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants
        self.description = description

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'organizer': self.organizer,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'participants': self.participants,
            'description': self.description
        }
