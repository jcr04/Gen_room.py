from typing import List, Optional, Union
from Domain.Repositories.resource_repository import ResourceRepository
from Domain.Entities.resource import Resource  # Importa a classe Resource para um tipo de dado mais preciso

class InMemoryResourceRepository(ResourceRepository):
    def __init__(self):
        self.resources: List[Resource] = []  # Adiciona anotação de tipo

    def find_all(self) -> List[Resource]:
        return self.resources

    def find_by_id(self, resource_id: str) -> Optional[Resource]:
        for resource in self.resources:
            if resource.id == resource_id:
                return resource
        return None

    def create_resource(self, name: str, description: str) -> Resource:
        new_resource = Resource(
            id=str(len(self.resources) + 1),
            name=name,
            description=description,
            is_reserved=False,  # Campo is_reserved adicionado
        )
        self.resources.append(new_resource)
        return new_resource

    def delete_resource(self, resource_id: str) -> bool:
        resource = self.find_by_id(resource_id)
        if resource:
            self.resources.remove(resource)
            return True
        return False

    def get_resource_reservations(self, resource_id: str) -> List[dict]:
        resource = self.find_by_id(resource_id)
        if resource:
            return resource.reservations  # Usa a propriedade 'reservations' da classe Resource
        return []

    def reserve_resource(self, resource_id: str, start_time: str, end_time: str) -> bool:
        resource = self.find_by_id(resource_id)
        if resource:
            for reservation in resource.reservations:
                if (
                    start_time < reservation['end_time']
                    and end_time > reservation['start_time']
                ):
                    return False  # O recurso já está reservado neste período

            new_reservation = {
                'start_time': start_time,
                'end_time': end_time
            }
            resource.reservations.append(new_reservation)
            return True
        return False

    # Método get_resource_reservations removido, pois já foi definido anteriormente
