class Room:
    def __init__(self, id, name, room_type=None, is_occupied=False, capacity=None, description=None):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.is_occupied = is_occupied
        self.capacity = capacity
        self.description = description
        self.reservations = []

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
        }

    def to_detailed_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'capacity': self.capacity,
            'description': self.description,
            'reservations': self.reservations
        }
