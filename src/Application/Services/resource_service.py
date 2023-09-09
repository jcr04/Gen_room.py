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
    

    def reserve_resource(self, resource_id, start_time, end_time):
        resource = self.resource_repository.find_by_id(resource_id)
        
        if resource is None:
            return False 

        if resource['is_reserved']:
            return False 

        for reservation in resource.get('reservations', []):
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return False

        resource['is_reserved'] = True

        new_reservation = {'start_time': start_time, 'end_time': end_time}
        resource.setdefault('reservations', []).append(new_reservation)

        return True
