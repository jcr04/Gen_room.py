from importlib import resources
from Domain.Entities.resource import Resource


class ResourceRepository:
    def __init__(self):
        self.resource = []
        
        self.create_resource('Projetor', 'Projetor de alta definição' )
        self.create_resource('Notebook', 'Notebook para apresentações' )
        self.create_resource('Quadro branco', 'Quadro branco interativo' )
        
    def find_all(self):
        return self.resource

    def find_by_id(self, id):
       for resource in resource:
        if resource['id'] == id:
            return resource
        return None

    def create_resource(self, name, description):
        new_resource = {
            'id': str(len(self.resource) + 1),  # Corrija 'self.resources' para 'self.resource'.
            'name': name,
            'description': description
        }
        self.resource.append(new_resource)  # Corrija 'self.resources' para 'self.resource'.
        return new_resource

    def delete_resource(self, resource):
        resource_id = resource.get('id')

        for existing_resource in resource:
            if existing_resource.get('id') == resource_id:
                resource.remove(existing_resource)
                return True 
        return False

    def reserve_resource(self, resource_id, start_time, end_time):
        resource_to_reserve = None
        for existing_resource in resources:
            if existing_resource.get('id') == resource_id:
                resource_to_reserve = existing_resource
                break

        if resource_to_reserve is None:
            return False  # O recurso com o ID especificado não foi encontrado.

        # Verifica se o recurso já está reservado durante o período especificado.
        for reservation in resource_to_reserve.get('reservations', []):
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return False  # O recurso já está reservado nesse período.

        # Adiciona a nova reserva ao recurso.
        new_reservation = {'start_time': start_time, 'end_time': end_time}
        resource_to_reserve.setdefault('reservations', []).append(new_reservation)

        return True

    def get_resource_reservations(self, resource_id):
        resource_reservations = []
        for existing_resource in resources:
            if existing_resource.get('id') == resource_id:
                resource_reservations = existing_resource.get('reservations', [])
                break

        return resource_reservations