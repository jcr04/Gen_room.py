# No arquivo src\Presentation\Controllers\resource_controller.py
from flask import Blueprint, jsonify, request
from flask_restful_swagger import swagger
from Application.Services.resource_service import ResourceService
from Domain.Entities.resource import Resource

resource_app = Blueprint('resource_app', __name__)
resource_service = ResourceService()



@resource_app.route('/resources/<string:resource_id>/reserve', methods=['POST'])
@swagger.operation(
    notes='Reserva um recurso compartilhado',
    responseClass=Resource.__name__,
    nickname='reserveResource'
)
def reserve_resource(resource_id):
    result = resource_service.reserve_resource(resource_id)
    if result:
        resource_details = resource_service.get_resource_details(resource_id)
        return jsonify({'message': 'Resource reserved successfully', 'resource_details': resource_details}), 200
    return jsonify({'error': 'Resource not found or already reserved'}), 404
