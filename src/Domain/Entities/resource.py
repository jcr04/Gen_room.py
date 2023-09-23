# No arquivo src\Domain\Entities\resource.py
class Resource:
    def __init__(self, id: str, name: str, description: str, is_reserved: bool = False):
        self.id = id
        self.name = name
        self.description = description
        self.is_reserved = is_reserved  # Definido como False por padrão
        self.reservations = []

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_reserved': self.is_reserved,
            'reservations': self.reservations  # Adicione as reservas ao JSON
        }