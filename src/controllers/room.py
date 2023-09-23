from flask import Blueprint, request, Flask
from flask_restful import Api
from models.room import RoomModel
from database import db

app = Flask(__name__)
room_controller = Blueprint('room_controller', __name__)
api = Api(room_controller)

@room_controller.route('/rooms/<int:id>', methods=['GET'])
def get_room_by_id(id):
    room = RoomModel.find_by_id(id)
    if room is None:
        return {'message': 'Room not found'}, 404

    return room.json()
    
@room_controller.route('/rooms', methods=['GET'])
def get_all_rooms():
    rooms = RoomModel.find_all()
    return [room.json() for room in rooms], 200

@room_controller.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()

    room = RoomModel(**data)  # Crie uma instância com base nos dados
    db.session.add(room)  # Adicione a instância à sessão
    db.session.commit()  # Salve-a no banco de dados

    return room.json(), 201

@room_controller.route('/rooms/<int:id>', methods=['PUT'])
def edit_room_by_id(id):
    data = request.get_json()

    room = RoomModel.find_by_id(id)
    if room is None:
        return {'message': 'Room not found'}, 404

    # Atualize os atributos do objeto com base nos dados recebidos
    room.name = data['name']
    room.room_type = data['room_type']
    room.capacity = data['capacity']
    room.description = data['description']
    room.room_category = data['room_category']
    room.shift = data['shift']

    db.session.commit()  # Salve as atualizações no banco de dados

    return room.json(), 200

@room_controller.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room_by_id(id):
    room = RoomModel.find_by_id(id)
    if room is None:
        return {'message': 'Room not found'}, 404

    db.session.delete(room)  # Exclua a instância da sessão
    db.session.commit()  # Commit para aplicar a exclusão no banco de dados

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
