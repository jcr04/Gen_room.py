# src/Presentation/Controllers/room_controller.py
from flask import Blueprint, jsonify
from Application.Services.room_service import RoomService

room_app = Blueprint('room_app', __name__)
room_service = RoomService()

@room_app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = room_service.get_all_rooms()
    return jsonify(rooms)

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
