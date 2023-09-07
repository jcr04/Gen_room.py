from Domain.Repositories.resource_repository import ResourceRepository

class InMemoryResourceRepository(ResourceRepository):
    def __init__(self):
        self.resources = []
        self.reservations = []

    def find_all(self):
        return self.resources

    def find_by_id(self, id):
        for resource in self.resources:
            if resource['id'] == id:
                return resource
        return None

    def create_resource(self, name, description):
        new_resource = {
            'id': str(len(self.resources) + 1),
            'name': name,
            'description': description,
            'reservations': []  # Adicionamos uma lista vazia para as reservas deste recurso.
        }
        self.resources.append(new_resource)
        return new_resource

    def delete_resource(self, resource):
        if resource in self.resources:
            self.resources.remove(resource)
            return True
        return False

    def reserve_resource(self, resource_id, start_time, end_time):
        resource = self.find_by_id(resource_id)
        if resource:
            # Verifica se o recurso já está reservado durante o período especificado
            for reservation in resource['reservations']:
                if (
                    start_time < reservation['end_time']
                    and end_time > reservation['start_time']
                ):
                    return False  # O recurso já está reservado neste período

            # Adiciona a reserva ao recurso
            new_reservation = {
                'start_time': start_time,
                'end_time': end_time
            }
            resource['reservations'].append(new_reservation)
            return True  # Recurso reservado com sucesso
        return False

    def get_resource_reservations(self, resource_id):
        resource = self.find_by_id(resource_id)
        if resource:
            return resource['reservations']
        return []
