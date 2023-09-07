# No arquivo src\Domain\Entities\resource.py
class Resource:
    def __init__(self, id, name, description, is_reserved=False):
        self.id = id
        self.name = name
        self.description = description
        self.is_reserved = is_reserved
        self.reservations = []

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_reserved': self.is_reserved,
            'reservations': self.reservations  # Incluímos as reservas aqui.
        }