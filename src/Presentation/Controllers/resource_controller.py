from flask import Blueprint, jsonify, request
from Infrastructure.models.resource import ResourceModel, db

resource_app = Blueprint('resource_app', __name__)

def handle_error(message, status_code):
    return jsonify({'error': message}), status_code

def create_response(data, message, status_code=200):
    return jsonify({'data': data, 'message': message}), status_code

@resource_app.route('/api/resources', methods=['GET'])
def list_resources():
    resources = ResourceModel.query.all()
    return create_response([resource.json() for resource in resources], 'Resources retrieved successfully')

@resource_app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return handle_error('Nome é obrigatório', 400)

    created_resource = ResourceModel(name=name, description=description)
    db.session.add(created_resource)
    db.session.commit()
    return create_response(created_resource.json(), 'Resource created successfully', 201)

@resource_app.route('/api/resources/<string:resource_id>', methods=['DELETE'])
def delete_resource(resource_id: str):
    resource = ResourceModel.query.filter_by(id=resource_id).first()
    if resource:
        db.session.delete(resource)
        db.session.commit()
        return create_response({}, 'Recurso excluído com sucesso', 204)
    return handle_error('Recurso não encontrado', 404)

@resource_app.route('/api/resources/<string:resource_id>/reservations', methods=['GET'])
def get_resource_reservations(resource_id: str):
    resource = ResourceModel.query.filter_by(id=resource_id).first()
    if resource:
        reservations = [reservation.json() for reservation in resource.reservations]
        return create_response(reservations, 'Reservations retrieved successfully')
    return handle_error('Recurso não encontrado', 404)

@resource_app.route('/api/resources/<string:resource_id>/reserve', methods=['POST'])
def reserve_resource(resource_id: str):
    resource = ResourceModel.query.filter_by(id=resource_id).first()
    if resource:
        resource.is_reserved = True
        db.session.commit()
        return create_response(resource.json(), 'Recurso reservado com sucesso')
    return handle_error('Recurso não encontrado', 404)
