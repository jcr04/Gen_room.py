class Room:
    def __init__(self, id, name, room_type=None, is_occupied=False):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.is_occupied = is_occupied
        self.reservations = []

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'reservations': self.reservations
        }
