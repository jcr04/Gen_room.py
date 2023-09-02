from Domain.Repositories.room_repository import RoomRepository
from Domain.Entities.room import Room

class InMemoryRoomRepository(RoomRepository):
    def __init__(self):
        self.rooms = []

    def find_all(self):
        return self.rooms

    def find_by_id(self, id):
        return next((room for room in self.rooms if room.id == id), None)
    
    def find_by_id(self, room_id):
        return next((room for room in self.rooms if room.id == room_id), None)