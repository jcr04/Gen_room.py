from typing import List, Optional
from Infrastructure.models.resource import ResourceModel

class ResourceRepository:
    def __init__(self):
        pass  # A inicialização pode ser omitida já que estamos usando o ORM
    
    def find_all(self) -> List[ResourceModel]:
        return ResourceModel.query.all()
    
    def find_by_id(self, resource_id: str) -> Optional[ResourceModel]:
        return ResourceModel.query.filter_by(id=resource_id).first()
    
    def create_resource(self, name: str, description: str) -> ResourceModel:
        new_resource = ResourceModel(name=name, description=description)
        new_resource.save_to_db()  # Supondo que você tenha um método save_to_db em sua model
        return new_resource

    def delete_resource(self, resource_id: str) -> bool:
        resource = self.find_by_id(resource_id)
        if resource:
            resource.delete_from_db()  # Supondo que você tenha um método delete_from_db em sua model
            return True
        return False
    
    def reserve_resource(self, resource_id: str, start_time: str, end_time: str) -> bool:
        resource = self.find_by_id(resource_id)
        if resource:
            # Suponho que sua reserva seja representada de alguma forma. Se for um campo ou objeto, você precisará ajustar aqui.
            new_reservation = {
                'start_time': start_time,
                'end_time': end_time
            }
            resource.reservations.append(new_reservation)
            resource.save_to_db()  # Salve as alterações no banco de dados
            return True
        return False

    def get_resource_reservations(self, resource_id: str) -> List[dict]:
        resource = self.find_by_id(resource_id)
        if resource:
            return resource.reservations  # Supondo que reservations seja uma lista
        return []
