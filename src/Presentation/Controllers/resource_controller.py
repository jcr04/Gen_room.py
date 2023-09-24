from flask import Blueprint, jsonify, request
from Application.Services.resource_service import ResourceService
from Domain.Entities.resource import Resource

resource_app = Blueprint('resource_app', __name__)
resource_service = ResourceService()

@resource_app.route('/api/resources', methods=['GET'])
def list_resources():
    resources = resource_service.get_all_resources()
    resource_list = [{**resource.to_json(), 'is_reserved': resource.is_reserved} for resource in resources]
    return jsonify(resource_list), 200

@resource_app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'error': 'Nome e descrição são obrigatórios'}), 400

    created_resource = resource_service.create_resource(name, description)
    return jsonify(created_resource.to_json()), 201

@resource_app.route('/api/resources/<string:resource_id>', methods=['DELETE'])
def delete_resource(resource_id: str):
    success = resource_service.delete_resource(resource_id)

    if success:
        return jsonify({'message': 'Recurso excluído com sucesso'}), 204
    return jsonify({'error': 'Recurso não encontrado'}), 404

@resource_app.route('/api/resources/<string:resource_id>/reservations', methods=['GET'])
def get_resource_reservations(resource_id: str):
    reservations = resource_service.get_resource_reservations(resource_id)
    return jsonify(reservations), 200

@resource_app.route('/api/resources/<string:resource_id>/reserve', methods=['POST'])
def reserve_resource(resource_id: str):
    resource = resource_service.find_by_id(resource_id)
    
    if resource is None:
        return jsonify({'error': 'Recurso não encontrado'}), 404

    resource.is_reserved = True
    return jsonify({
        'message': 'Recurso reservado com sucesso',
        'resource_details': resource.to_json()
    }), 200
