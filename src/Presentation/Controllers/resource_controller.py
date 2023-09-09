# No arquivo src\Presentation\Controllers\resource_controller.py
from http.client import NOT_FOUND
from flask import Blueprint, app, jsonify, request
from flask_restful_swagger import swagger
from Application.Services.resource_service import ResourceService
from Domain.Entities.resource import Resource
from Domain.Repositories.resource_repository import ResourceRepository

resource_app = Blueprint('resource_app', __name__)
resource_service = ResourceService()

resource_repository = ResourceRepository()

@resource_app.route('/api/resources', methods=['GET'])
@swagger.operation(
    notes='Lista todos os recursos compartilhados',
    responseClass=Resource.__name__,
    nickname='listResources'
)
def list_resources():
    resource_repository = ResourceRepository()
    resources = resource_repository.find_all()

    resource_list = [
        {
            **resource.to_json(),
            'is_reserved': True if resource.is_reserved else False
        }
        for resource in resources
    ]

    return jsonify(resource_list), 200

@resource_app.route('/api/resources', methods=['POST'])
@swagger.operation(
    notes='Cria um novo recurso compartilhado',
    responseClass=Resource.__name__,
    nickname='createResource'
)
def create_resource():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    created_resource = resource_service.create_resource(name, description)
    return jsonify(created_resource.to_json()), 201  # Retorna o recurso criado

@resource_app.route('/api/resources/<string:resource_id>', methods=['DELETE'])
@swagger.operation(
    notes='Exclui um recurso compartilhado',
    responseClass=bool.__name__,
    nickname='deleteResource'
)
def delete_resource(resource_id):
    success = resource_service.delete_resource(resource_id)
    if success:
        return 'Recurso excluído com sucesso', 204
    else:
        return 'Recurso não encontrado', 404

@resource_app.route('/api/resources/<string:resource_id>/reservations', methods=['GET'])
@swagger.operation(
    notes='Obtém as reservas de um recurso compartilhado',
    responseClass=list.__name__,
    nickname='getReservations'
)
def get_resource_reservations(resource_id):
    reservations = resource_service.get_resource_reservations(resource_id)
    return jsonify(reservations), 200

@resource_app.route('/api/resources/<string:resource_id>/reserve', methods=['POST'])
@swagger.operation(
    notes='Reserva um recurso compartilhado',
    responseClass=Resource.__name__,
    nickname='reserveResource'
)
def reserve_resource(resource_id):
    resource_repository = ResourceRepository()  # Crie uma instância do repositório
    resource = resource_repository.find_by_id(resource_id)
    if resource is None:
        return jsonify({'message': 'Recurso não encontrado'}), 404

    resource.is_reserved = True
    return jsonify({
        'message': 'Recurso reservado com sucesso',
        'resource_details': resource.to_json()  # Retorne os detalhes do recurso atualizados em JSON
    }), 200

