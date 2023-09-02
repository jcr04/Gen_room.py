# src/Presentation/Controllers/room_controller.py
from flask import Blueprint, jsonify, request
from Application.Services.room_service import RoomService

room_app = Blueprint('room_app', __name__)
room_service = RoomService()

@room_app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = room_service.get_all_rooms()
    rooms_json = [room.to_json() for room in rooms]
    return jsonify(rooms_json)

@room_app.route('/rooms/<string:room_id>/reserve', methods=['POST'])
def reserve_room(room_id):
    result = room_service.reserve_room(room_id)
    if result:
        room_details = room_service.get_room_details(room_id)
        return jsonify({'message': 'Room reserved successfully', 'room_details': room_details}), 200
    return jsonify({'error': 'Room not found or already occupied'}), 404

@room_app.route('/rooms/occupied', methods=['GET'])
def get_occupied_rooms():
    occupied_rooms = room_service.get_occupied_rooms()
    return jsonify(occupied_rooms)

@room_app.route('/rooms/<string:room_id>', methods=['GET'])
def get_room_details(room_id):
    room_details = room_service.get_room_details(room_id)
    if room_details:
        return jsonify(room_details), 200
    return jsonify({'error': 'Room not found'}), 404

@room_app.route('/rooms/<string:room_id>', methods=['DELETE'])
def delete_room(room_id):
    result = room_service.delete_room(room_id)
    if result:
        return jsonify({'message': 'Room deleted successfully'}), 200
    return jsonify({'error': 'Room not found'}), 404

@room_app.route('/rooms/available', methods=['GET'])
def get_available_rooms():
    available_rooms = room_service.get_available_rooms()
    return jsonify([room.to_json() for room in available_rooms])

@room_app.route('/rooms/<string:room_id>/update-name', methods=['PUT'])
def update_room_name(room_id):
    data = request.get_json()
    new_name = data.get('new_name')

    updated_room = room_service.update_room_name(room_id, new_name)
    if updated_room:
        return jsonify({'message': 'Room name updated successfully', 'room': updated_room.to_json()}), 200
    return jsonify({'error': 'Room not found'}), 404

@room_app.route('/rooms/by-type/<string:room_type>', methods=['GET'])
def get_rooms_by_type(room_type):
    rooms = room_service.get_rooms_by_type(room_type)
    rooms_json = [room.to_json() for room in rooms]
    return jsonify(rooms_json)

@room_app.route('/rooms/<string:room_id>/reserve-by-period', methods=['POST'])
def reserve_room_by_period(room_id):
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    result = room_service.reserve_room_by_period(room_id, start_time, end_time)

    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 200