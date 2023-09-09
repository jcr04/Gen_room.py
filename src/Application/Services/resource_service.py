# No arquivo src\Application\Services\resource_service.py
from Domain.Entities.resource import Resource
from Domain.Repositories.resource_repository import ResourceRepository

class ResourceService:
    def __init__(self):
        self.resource_repository = ResourceRepository()

    def get_all_resources(self):
        return self.resource_repository.find_all()

    def reserve_resource(self, resource_id):
        resource = self.resource_repository.find_by_id(resource_id)
        if resource:
            if resource.is_reserved:
                return None  # O recurso já está reservado
            resource.is_reserved = True
            return self.get_resource_details(resource_id)  # Retorna detalhes do recurso após a reserva
        return None

    def get_resource_details(self, resource_id):
        resource = self.resource_repository.find_by_id(resource_id)
        if resource:
            return {
                'id': resource.id,
                'name': resource.name,
                'description': resource.description,
                'is_reserved': resource.is_reserved,
            }
        return None
