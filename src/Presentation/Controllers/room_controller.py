from flask import Blueprint, request, jsonify, Flask
from flask_restful import Api
from models.room import RoomModel
from database import db
from Domain.Entities.room import Room
from Application.Services.room_service import RoomService

app = Flask(__name__)
room_controller = Blueprint('room_controller', __name__)
api = Api(room_controller)
room_service = RoomService()

def handle_error(message, status_code):
    return jsonify({'error': message}), status_code

# ---------------- Rooms Endpoints ------------------

@room_controller.route('/rooms', methods=['GET'])
def get_all_rooms():
    rooms = room_service.get_all_rooms()
    rooms_json = [room.to_json() for room in rooms]
    return jsonify(rooms_json), 200

@room_controller.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()
    room = RoomModel(**data)
    db.session.add(room)
    db.session.commit()
    return room.json(), 201

@room_controller.route.route('/rooms/<string:room_id>', methods=['GET'])
def get_room_details(room_id):
    """Retrieve details of a specific room."""
    room_details = room_service.get_room_details(room_id)
    if room_details:
        return jsonify({
            'id': room_details['id'],
            'name': room_details['name'],
            'is_occupied': room_details['is_occupied'],
            'capacity': room_details['capacity'],
            'description': room_details['description']
        }), 200
    return handle_error('Room not found', 404)

@room_controller.route('/rooms/<string:room_id>', methods=['DELETE'])
def delete_room_by_id(id):
    room = RoomModel.find_by_id(id)
    if room is None:
        return handle_error('Room not found', 404)

    db.session.delete(room)
    db.session.commit()
    return '', 204

@room_controller.route('/rooms/<string:room_id>/update-name', methods=['PUT'])
def edit_room_by_id(id):
    data = request.get_json()
    room = RoomModel.find_by_id(id)
    if room is None:
        return handle_error('Room not found', 404)

    # Update room attributes
    room.name = data['name']
    room.room_type = data['room_type']
    room.capacity = data['capacity']
    room.description = data['description']
    room.room_category = data['room_category']
    room.shift = data['shift']

    db.session.commit()
    return room.json(), 200

# ---------------- Reservation Endpoints ------------------

@room_controller.route('/rooms/<string:room_id>/reserve', methods=['POST'])
def reserve_room(room_id):
    """Reserve a room."""
    result = room_service.reserve_room(room_id)
    if result:
        room_details = room_service.get_room_details(room_id)
        return jsonify({'message': 'Room reserved successfully', 'room_details': room_details}), 200
    return handle_error('Room not found or already occupied', 404)

@room_controller.route('/rooms/<string:room_id>/reserve-by-period', methods=['POST'])
def reserve_room_by_period(room_id):
    """Reserve a room for a specific period."""
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    if not start_time or not end_time:
        return handle_error('Both start_time and end_time are required.', 400)

    result = room_service.reserve_room_by_period(room_id, start_time, end_time)

    if 'error' in result:
        return jsonify(result), 400

    room_details = room_service.get_room_details(room_id)
    return jsonify({'message': 'Room reserved successfully', 'room_details': room_details}), 200

# ---------------- Additional Room Retrieval Endpoints ------------------

@room_controller.route('/rooms/occupied', methods=['GET'])
def get_occupied_rooms():
    """Retrieve all occupied rooms."""
    occupied_rooms = room_service.get_occupied_rooms()
    return jsonify(occupied_rooms)

@room_controller.route.route('/rooms/available', methods=['GET'])
def get_available_rooms():
    """Retrieve all available rooms."""
    available_rooms = room_service.get_available_rooms()
    return jsonify([room.to_json() for room in available_rooms])

@room_controller.route.route('/rooms/by-type/<string:room_type>', methods=['GET'])
def get_rooms_by_type(room_type):
    """Retrieve rooms based on their type."""
    valid_room_types = ["Sala-Aula", "Sala-Interativa", "Laboratórios", "Auditórios", "Cozinhas"]
    if room_type not in valid_room_types:
        return handle_error('Tipo de sala inválido.', 400)

    rooms = room_service.get_rooms_by_type(room_type)

    if not rooms:
        return handle_error('Nenhuma sala encontrada para este tipo.', 404)

    rooms_json = [room.to_detailed_json() for room in rooms]

    return jsonify({'rooms': rooms_json}), 200
