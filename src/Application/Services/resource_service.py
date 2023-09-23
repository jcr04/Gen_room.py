# No arquivo src\Application\Services\resource_service.py
from Domain.Entities.resource import Resource
from Domain.Repositories.resource_repository import ResourceRepository

class ResourceService:
    def __init__(self):
        self.resource_repository = ResourceRepository()

    def get_all_resources(self):
        return self.resource_repository.find_all()
    
    def create_resource(self, name, description):
        return self.resource_repository.create_resource(name, description)

    def delete_resource(self, resource_id):
        return self.resource_repository.delete_resource(resource_id)

    def get_resource_reservations(self, resource_id):
        return self.resource_repository.get_resource_reservations(resource_id)
    
    def is_resource_reserved(self, resource, start_time, end_time):
        for reservation in resource.get('reservations', []):
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return True
        return False
    
    def reserve_resource(self, resource_id, start_time, end_time):
        resource = self.resource_repository.find_by_id(resource_id)
        
        if resource is None:
            return {'error': 'Resource not found'}

        if resource['is_reserved'] or self.is_resource_reserved(resource, start_time, end_time):
            return {'error': 'Resource is already reserved during this period'}

        resource['is_reserved'] = True

        new_reservation = {'start_time': start_time, 'end_time': end_time}
        resource.setdefault('reservations', []).append(new_reservation)

        return {'message': 'Resource reserved successfully'}
