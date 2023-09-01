from Domain.Entities.room import Room

class RoomRepository:
    def __init__(self):
        self.rooms = []
        
    def find_all(self):
       return self.rooms

    def find_by_id(self, id):
        return next((room for room in self.rooms if room.id == id), None)

    def create_room(self, name):
        new_room = Room(id=str(len(self.rooms) + 1), name=name)
        self.rooms.append(new_room)
        return new_room
    
    def delete_room(self, room):
        self.rooms.remove(room)