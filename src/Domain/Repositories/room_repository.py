# Importe a classe Room do módulo correto
import datetime
from Domain.Entities.room import Room

class RoomRepository:
    def __init__(self):
        self.rooms = []

        # Adicione algumas salas diretamente no construtor
        self.create_room("Sala 101", "Sala-Aula", 10, "Sala de reunião para 10 pessoas")
        self.create_room("Sala 102", "Sala-Aula", 8, "Sala de conferência para 8 pessoas")
        self.create_room("Sala 103", "Sala-Aula", 6, "Sala de reunião para 6 pessoas")  # Adicione o tipo de sala aqui
        
    def find_all(self):
       return self.rooms

    def find_by_id(self, id):
        return next((room for room in self.rooms if room.id == id), None)

    def create_room(self, name, room_type, capacity=None, description=None, room_category=None):
        new_room = Room(id=str(len(self.rooms) + 1), name=name, room_type=room_type, capacity=capacity, description=description, room_category=room_category)
        self.rooms.append(new_room)
        return new_room
    
    def delete_room(self, room):
        self.rooms.remove(room)
        
    def update_room(self, room_id, data):
        room = self.room_repository.find_by_id(room_id)
    
        if room:
            if 'name' in data:
                room.name = data['name']
            if 'capacity' in data:
                room.capacity = data['capacity']
            if 'description' in data:
                room.description = data['description']
                
            return room
        return None

    def find_by_type(self, room_type):
        return [room for room in self.rooms if room.room_type == room_type]
    
    def reserve_room(self, room, start_time, end_time):
        # Verifica se a sala já está ocupada durante o período especificado
        for reservation in room.reservations:
            if start_time < reservation['end_time'] and end_time > reservation['start_time']:
                return False  # A sala já está ocupada nesse período

        # Adiciona a reserva à sala
        room.reservations.append({
            'start_time': start_time,
            'end_time': end_time
        })
        return True  # Sala reservada com sucesso
    
    def reserve_room_by_period(self, room_id, start_time, end_time):
        room = self.find_by_id(room_id)
        if room:
            start_datetime = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            end_datetime = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

            if start_datetime >= end_datetime:
                return {'error': 'Invalid time period'}

            result = self.reserve_room(room, start_datetime, end_datetime)

            if result:
                return {'message': 'Room reserved successfully'}
            else:
                return {'error': 'Room already occupied during this period'}

        return {'error': 'Room not found'}
