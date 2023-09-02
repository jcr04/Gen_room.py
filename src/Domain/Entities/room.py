class Room:
    def __init__(self, id, name, room_type):
        self.id = id
        self.name = name
        self.is_occupied = False
        self.room_type = room_type
        self.reservations = []

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_occupied': self.is_occupied,
            'room_type': self.room_type,
            'reservations': self.reservations
        }