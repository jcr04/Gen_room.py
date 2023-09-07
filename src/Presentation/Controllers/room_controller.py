# Importe as bibliotecas necessárias para o Swagger
import sys
from flask import Blueprint, jsonify, request
from flask_restful_swagger import swagger
from Domain.Entities.room import Room
from Application.Services.room_service import RoomService


room_app = Blueprint('room_app', __name__)
room_service = RoomService()

# Documentação do endpoint GET /rooms
@room_app.route('/rooms', methods=['GET'])
@swagger.operation(
    notes='Obtém a lista de todas as salas',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='getRooms'
)
def get_rooms():
    rooms = room_service.get_all_rooms()
    rooms_json = [room.to_json() for room in rooms]
    return jsonify(rooms_json)

# Documentação do endpoint POST /rooms
@room_app.route('/rooms', methods=['POST'])
@swagger.operation(
    notes='Cria uma nova sala',
    responseClass=Room.__name__,  
    nickname='createNewRoom'
)
def create_new_room():
    data = request.get_json()
    name = data.get('name')
    room_type = data.get('room_type')
    capacity = data.get('capacity')
    description = data.get('description')
    room_category = data.get('room_category')  # Adicione o campo 'room_category'

    if not name or not room_type or not capacity or not description or not room_category:
        return jsonify({'error': 'Todos os campos (name, room_type, capacity, description e room_category) são obrigatórios.'}), 400

    try:
        new_room = room_service.create_room(name, room_type, capacity, description, room_category)  # Atualize o método create_room
        return jsonify(new_room.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Documentação do endpoint POST /rooms/{room_id}/reserve
@room_app.route('/rooms/<string:room_id>/reserve', methods=['POST'])
@swagger.operation(
    notes='Reserva uma sala',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='reserveRoom'
)
def reserve_room(room_id):
    result = room_service.reserve_room(room_id)
    if result:
        room_details = room_service.get_room_details(room_id)
        return jsonify({'message': 'Room reserved successfully', 'room_details': room_details}), 200
    return jsonify({'error': 'Room not found or already occupied'}), 404

# Documentação do endpoint GET /rooms/occupied
@room_app.route('/rooms/occupied', methods=['GET'])
@swagger.operation(
    notes='Obtém a lista de salas ocupadas',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='getOccupiedRooms'
)
def get_occupied_rooms():
    occupied_rooms = room_service.get_occupied_rooms()
    return jsonify(occupied_rooms)

# Documentação do endpoint GET /rooms/{room_id}
@room_app.route('/rooms/<string:room_id>', methods=['GET'])
@swagger.operation(
    notes='Obtém detalhes de uma sala específica',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='getRoomDetails'
)
def get_room_details(room_id):
    room_details = room_service.get_room_details(room_id)
    if room_details:
        return jsonify({
            'id': room_details['id'],
            'name': room_details['name'],
            'is_occupied': room_details['is_occupied'],
            'capacity': room_details['capacity'],  # Nova informação - Capacidade da sala
            'description': room_details['description']  # Nova informação - Descrição da sala
        }), 200
    return jsonify({'error': 'Room not found'}), 404

# Documentação do endpoint DELETE /rooms/{room_id}
@room_app.route('/rooms/<string:room_id>', methods=['DELETE'])
@swagger.operation(
    notes='Exclui uma sala',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='deleteRoom'
)
def delete_room(room_id):
    result = room_service.delete_room(room_id)
    if result:
        return jsonify({'message': 'Room deleted successfully'}), 200
    return jsonify({'error': 'Room not found'}), 404

# Documentação do endpoint GET /rooms/available
@room_app.route('/rooms/available', methods=['GET'])
@swagger.operation(
    notes='Obtém a lista de salas disponíveis',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='getAvailableRooms'
)
def get_available_rooms():
    available_rooms = room_service.get_available_rooms()
    return jsonify([room.to_json() for room in available_rooms])

# Documentação do endpoint PUT /rooms/{room_id}/update-name
@room_app.route('/rooms/<string:room_id>/update-name', methods=['PUT'])
@swagger.operation(
    notes='Atualiza o nome de uma sala',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='updateRoomName'
)
def update_room(room_id):
    data = request.get_json()
    updated_room = room_service.update_room(room_id, data)
    
    if updated_room:
        return jsonify({'message': 'Room updated successfully', 'room': updated_room.to_json()}), 200
    return jsonify({'error': 'Room not found'}), 404

# Documentação do endpoint GET /rooms/by-type/{room_type}
@room_app.route('/rooms/by-type/<string:room_type>', methods=['GET'])
@swagger.operation(
    notes='Obtém a lista de salas por tipo',
    responseClass=Room.__name__,  # Use a classe apropriada aqui (Room representa o exemplo)
    nickname='getRoomsByType'
)
def get_rooms_by_type(room_type):
    # Verifique se o tipo de sala fornecido é válido
    valid_room_types = ["Sala-Aula", "Sala-Interativa", "Laboratórios", "Auditórios", "Cozinhas"]
    if room_type not in valid_room_types:
        return jsonify({'error': 'Tipo de sala inválido.'}), 400

    # Chame o serviço para buscar as salas por tipo
    rooms = room_service.get_rooms_by_type(room_type)

    if not rooms:
        return jsonify({'message': 'Nenhuma sala encontrada para este tipo.'}), 404

    # Converte as salas em JSON
    rooms_json = [room.to_detailed_json() for room in rooms]

    return jsonify({'rooms': rooms_json}), 200

# Documentação do endpoint POST /rooms/{room_id}/reserve-by-period
@room_app.route('/rooms/<string:room_id>/reserve-by-period', methods=['POST'])
@swagger.operation(
    notes='Reserva uma sala por período',
    responseClass=Room.__name__,
    nickname='reserveRoomByPeriod'
)
def reserve_room_by_period(room_id):
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if not start_time or not end_time:
        return jsonify({'error': 'Both start_time and end_time are required.'}), 400

    result = room_service.reserve_room_by_period(room_id, start_time, end_time)

    if 'error' in result:
        return jsonify(result), 400

    room_details = room_service.get_room_details(room_id)
    return jsonify({'message': 'Room reserved successfully', 'room_details': room_details}), 200