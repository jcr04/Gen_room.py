class Room:
    def __init__(self, id, name, room_type=None, capacity=None, description=None, room_category=None, shift=None):
        self.id = id
        self.name = name
        self.room_type = room_type
        self.capacity = capacity
        self.description = description
        self.room_category = room_category  # Campo room_category adicionado
        self.is_occupied = False  # Campo is_occupied definido como False por padrão
        self.reservations = []
        self.shift = shift  # Usando 'shift' para manter a consistência

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'room_category': self.room_category,
            'shift': self.shift  # Usando 'shift' para manter a consistência
        }

    def to_detailed_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'room_type': self.room_type,
            'is_occupied': self.is_occupied,
            'capacity': self.capacity,
            'description': self.description,
            'room_category': self.room_category,  # Campo room_category na saída detalhada JSON
            'reservations': [r.to_json() for r in self.reservations],  # Converta reservas em sua representação JSON
            'shift': self.shift  # Usando 'shift' para manter a consistência
        }
