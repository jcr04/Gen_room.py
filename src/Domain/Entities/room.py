class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.is_occupied = False

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_occupied': self.is_occupied
        }
