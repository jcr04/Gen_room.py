from datetime import datetime
from Domain.Entities.room import Room  # Verifique se o caminho está correto de acordo com a estrutura do diretório

class RoomRepository:
    def __init__(self):
        self.rooms = []
        self.init_sample_rooms()

    def init_sample_rooms(self):
        self.create_room("Sala 101", "Sala-Aula", 10, "Sala de reunião para 10 pessoas", shift="Matutino")
        self.create_room("Sala 102", "Sala-Aula", 8, "Sala de conferência para 8 pessoas", shift="Vespertino")
        self.create_room("Sala 103", "Sala-Aula", 6, "Sala de reunião para 6 pessoas", shift="Noturno")

    def find_all(self):
        return self.rooms

    def find_by_id(self, id):
        return next((room for room in self.rooms if room.id == id), None)

    def create_room(self, name, room_type, capacity=None, description=None, room_category=None, shift=None):
        new_room = Room(
            id=str(len(self.rooms) + 1),
            name=name,
            room_type=room_type,
            capacity=capacity,
            description=description,
            room_category=room_category,
            shift=shift
        )
        self.rooms.append(new_room)
        return new_room
    
    def delete_room(self, room):
        self.rooms.remove(room)

    def update_room(self, room, data):
        if 'name' in data:
            room.name = data['name']
        if 'capacity' in data:
            room.capacity = data['capacity']
        if 'description' in data:
            room.description = data['description']
        return room

    def find_by_type(self, room_type):
        return [room for room in self.rooms if room.room_type == room_type]
    
    def parse_datetime(self, time_str):
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    
    def reserve_room(self, room, start_time, end_time):
        start_datetime = self.parse_datetime(start_time)
        end_datetime = self.parse_datetime(end_time)

        # Verificando se o período de tempo é válido
        if start_datetime >= end_datetime:
            return {'error': 'Invalid time period'}

        # Verificando se a sala já está reservada para o período fornecido
        for reservation in room.reservations:
            if not (start_datetime >= reservation['end_time'] or end_datetime <= reservation['start_time']):
                return {'error': 'Room already occupied during this period'}

        # Reservando a sala
        room.reservations.append({
            'start_time': start_datetime,
            'end_time': end_datetime
        })

        return {'message': 'Room reserved successfully'}
