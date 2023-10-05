# src\Application\Services\resource_service.py
from Infrastructure.models.resource import ResourceModel  # Importamos o modelo SQLAlchemy

class ResourceService:
    def __init__(self):
        pass  # Não precisamos inicializar o repositório aqui, porque estamos usando o SQLAlchemy diretamente

    def get_all_resources(self):
        return ResourceModel.query.all()  # Utilizamos o método query para obter todos os recursos

    def create_resource(self, name, description):
        new_resource = ResourceModel(name=name, description=description)
        new_resource.save_to_db()  # Salva o novo recurso no banco de dados
        return new_resource

    def delete_resource(self, resource_id):
        resource = ResourceModel.query.get(resource_id)  # Obtemos o recurso pelo ID
        if resource:
            resource.delete_from_db()  # Deleta o recurso do banco de dados
            return True
        return False

    def get_resource_reservations(self, resource_id):
        resource = ResourceModel.query.get(resource_id)
        return resource.reservations if resource else []

    def is_resource_reserved(self, resource, start_time, end_time):
        for reservation in resource.reservations:
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return True
        return False
    
    def reserve_resource(self, resource_id, start_time, end_time):
        resource = ResourceModel.query.get(resource_id)  # Obtemos o recurso pelo ID
        if not resource:
            return {'error': 'Resource not found'}

        if resource.is_reserved or self.is_resource_reserved(resource, start_time, end_time):
            return {'error': 'Resource is already reserved during this period'}

        resource.is_reserved = True  # Definimos o recurso como reservado

        new_reservation = {'start_time': start_time, 'end_time': end_time}
        resource.reservations.append(new_reservation)  # Adicionamos a nova reserva ao recurso
        resource.save_to_db()  # Salva as alterações no banco de dados

        return {'message': 'Resource reserved successfully'}
