import datetime
from Domain.Entities.room import Room
from Domain.Repositories.room_repository import RoomRepository


class RoomService:
    def __init__(self):
        self.room_repository = RoomRepository()

    def get_all_rooms(self):
        return [room for room in self.room_repository.find_all() if hasattr(room, 'room_type')]

    def validate_input(self, name, room_type, capacity, description, room_category, shift):
        if not all([name, room_type, capacity, description, room_category, shift]):
            return {'error': 'Todos os campos são obrigatórios.'}

        if not isinstance(capacity, int) or capacity <= 0:
            return {'error': 'A capacidade deve ser um número inteiro positivo.'}

        valid_room_types = ['Sala-Aula', 'Sala-Interativa', "Laboratórios", "Auditórios", "Cozinhas"]
        if room_type not in valid_room_types:
            return {'error': 'O tipo da sala é inválido.'}

        valid_shifts = ['Matutino', 'Vespertino', 'Noturno']
        if shift not in valid_shifts:
            return {'error': 'O turno é inválido.'}

        return None

    def create_room(self, name, room_type, capacity, description, room_category, shift):
        validation_result = self.validate_input(name, room_type, capacity, description, room_category, shift)
        if validation_result:
            return validation_result

        new_room = self.room_repository.create_room(name, room_type, capacity, description, room_category, shift)
        return Room(new_room.id, new_room.name, new_room.room_type, new_room.capacity, new_room.description,
                    new_room.room_category, new_room.shift)

    def get_room_by_id(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        return room if room else None

    def get_occupied_rooms(self):
        occupied_rooms = [room for room in self.room_repository.find_all() if room.is_occupied]
        return [{'room': Room(room.id, room.name).to_json(), 'is_occupied': True} for room in occupied_rooms]
    
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
                'is_occupied': room.is_occupied,
                'capacity': room.capacity,  # Inclua a capacidade da sala aqui
                'description': room.description  # Inclua a descrição da sala aqui
            }
        return None
    
    def delete_room(self, room_id):
        room = self.room_repository.find_by_id(room_id)
        if room:
            self.room_repository.delete_room(room)
            return True  # Sala excluída com sucesso
        return False
    
    def get_available_rooms(self):
        available_rooms = [room for room in self.room_repository.find_all() if not room.is_occupied]
        return [Room(room.id, room.name) for room in available_rooms]
    
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
    
    def get_rooms_by_type(self, room_type):
    # Consulte o repositório para buscar salas por tipo
        rooms = self.room_repository.find_by_type(room_type)

        return rooms
    
    def reserve_room_by_period(self, room_id, start_time, end_time):
        room = self.get_room_by_id(room_id)
        if room is None:
            return {'error': 'Room not found'}

        try:
            start_datetime = datetime.datetime.strptime(start_time, '%d/%m/%Y %H:%M:%S')
            end_datetime = datetime.datetime.strptime(end_time, '%d/%m/%Y %H:%M:%S')
        except ValueError:
            return {'error': 'Invalid date format'}

        if start_datetime >= end_datetime:
            return {'error': 'Invalid time period'}

        if any(start_datetime < reservation['end_time'] and end_datetime > reservation['start_time']
               for reservation in room.reservations):
            return {'error': 'Room already occupied during this period'}

        room.reservations.append({'start_time': start_datetime, 'end_time': end_datetime})
        return {'message': 'Room reserved successfully'}

    
    def find_by_id(self, room_id):
        for room in self.rooms:
            print(f"Room ID: {room.id}")
            if room.id == room_id:
                return room
        return None
