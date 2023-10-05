# No arquivo src\Domain\Entities\resource.py
class Resource:
    def __init__(self, id: str, name: str, description: str, is_reserved: bool = False):
        self.id = id
        self.name = name
        self.description = description
        self.is_reserved = is_reserved  # Definido como False por padrão
        self.reservations = []

    def add_reservation(self, start_time: str, end_time: str) -> bool:
        for reservation in self.reservations:
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return False  # O recurso já está reservado neste período

        new_reservation = {
            'start_time': start_time,
            'end_time': end_time
        }
        self.reservations.append(new_reservation)
        return True

    def remove_reservation(self, start_time: str, end_time: str) -> bool:
        for reservation in self.reservations:
            if start_time == reservation['start_time'] and end_time == reservation['end_time']:
                self.reservations.remove(reservation)
                return True
        return False

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_reserved': self.is_reserved,
            'reservations': self.reservations  # Adicione as reservas ao JSON
        }
