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
    resources = resource_repository.find_all()
    resource_list = [resource.to_json() for resource in resources]
    return jsonify(resource_list), 200

@resource_app.route('/resources/<string:resource_id>/reserve', methods=['POST'])
@swagger.operation(
    notes='Reserva um recurso compartilhado',
    responseClass=Resource.__name__,
    nickname='reserveResource'
)
def reserve_resource(resource_id):
    resource = ResourceRepository.find_by_id(resource_id)
    if resource is None:
        raise NOT_FOUND("Resource not found")  # Isso irá gerar um erro 404

