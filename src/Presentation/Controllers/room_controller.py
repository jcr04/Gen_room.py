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
        return jsonify(result), 200
    return jsonify({'error': 'Room not found or already occupied'}), 404
