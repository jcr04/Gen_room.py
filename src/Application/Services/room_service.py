from Domain.Entities.room import Room
from Domain.Repositories.room_repository import RoomRepository

class RoomService:
    def __init__(self):
        self.room_repository = RoomRepository()

    def get_all_rooms(self):
        rooms = self.room_repository.find_all()
        return [Room(room.id, room.name) for room in rooms]
    
    def create_room(self, name):
        new_room = self.room_repository.create_room(name)
        return Room(new_room.id, new_room.name)
    
    def get_room_by_id(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            return Room(room.id, room.name)
        return None
    
    def update_room(self, room_id, new_name):
        room = self.room_repository.find_by_id(room_id)
        if room:
            room.name = new_name
            return Room(room.id, room.name)
        return None
    
    def delete_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            self.room_repository.delete_room(room)
            return Room(room.id, room.name)
        return None

    def get_occupied_rooms(self):
        occupied_rooms = [room for room in self.room_repository.find_all() if room.is_occupied]
        return [Room(room.id, room.name) for room in occupied_rooms]
    
    def reserve_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            if room.is_occupied:
                return None  # A sala já está ocupada
            room.is_occupied = True
            return self.get_room_details(room_id)  # Retorna detalhes da sala após a reserva
        return None
    
    def get_room_details(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            return {
                'id': room.id,
                'name': room.name,
                'is_occupied': room.is_occupied
            }
        return None
    
    def delete_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            self.room_repository.delete_room(room)
            return True  # Sala excluída com sucesso
        return False