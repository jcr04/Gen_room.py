from datetime import datetime
from Infrastructure.models.room import RoomModel
from Infrastructure.database import db  # Importe também o objeto db, caso precise.

class RoomRepository:
    def __init__(self):
        self.init_sample_rooms()

    def init_sample_rooms(self):
        # Aqui você pode inserir os dados iniciais diretamente no banco de dados, se necessário.
        pass

    def find_all(self):
        return RoomModel.query.all()

    def find_by_id(self, id):
        return RoomModel.query.get(id)

    def create_room(self, name, room_type, capacity=None, description=None, room_category=None, shift=None):
        new_room = RoomModel(
            name=name,
            room_type=room_type,
            capacity=capacity if capacity else 0,
            description=description if description else '',
            room_category=room_category if room_category else '',
            shift=shift if shift else '',
        )
        db.session.add(new_room)
        db.session.commit()
        return new_room
    
    def delete_room(self, room):
        db.session.delete(room)
        db.session.commit()

    def update_room(self, room, data):
        room.update_room(
        name=data.get('name'),
        capacity=data.get('capacity'),
        description=data.get('description')
    )
    # Adicione qualquer outro campo que você queira atualizar
        return room


    def find_by_type(self, room_type):
        return RoomModel.query.filter_by(room_type=room_type).all()

    def reserve_room(self, room, start_time, end_time):
        # Você pode adaptar esse método conforme sua lógica de negócio, mas lembre-se de persistir as alterações com db.session.commit()
        pass

