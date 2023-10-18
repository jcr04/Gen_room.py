import datetime
from Infrastructure.models.room import RoomModel
from Domain.Repositories.room_repository import RoomRepository
from Infrastructure.models.room import RoomModel, EventModel

class RoomService:
    def __init__(self):
        self.room_repository = RoomRepository()

    def get_all_rooms(self):
        return self.room_repository.find_all()

    def validate_input(self, name, room_type, capacity, description, room_category, shift):
        if not all([name, room_type, capacity, description, room_category, shift]):
            return {'error': 'Todos os campos são obrigatórios.'}
        
        return None

    def create_room(self, name, room_type, capacity, description, room_category, shift):
        validation_result = self.validate_input(name, room_type, capacity, description, room_category, shift)
        if validation_result:
            return validation_result
        
        return self.room_repository.create_room(name, room_type, capacity, description, room_category, shift)

    def get_room_by_id(self, room_id):
        return self.room_repository.find_by_id(room_id)

    def get_occupied_rooms(self):
        return [{'room': room.json(), 'is_occupied': room.is_occupied} for room in self.room_repository.find_all() if room.is_occupied]
    
    def reserve_room(self, room_id):
        room = self.get_room_by_id(room_id)
        if room and not room.is_occupied:
            room.is_occupied = True
            return room.json()
        return None
    
    def get_room_details(self, room_id):
        room = self.get_room_by_id(room_id)
        return room.json() if room else None
    
    def delete_room(self, room_id):
        room = self.get_room_by_id(room_id)
        if room:
            self.room_repository.delete_room(room)
            return True
        return False
    
    def get_available_rooms(self):
        return [room.json() for room in self.room_repository.find_all() if not room.is_occupied]
    
    def update_room(self, room_id, data):
        room = self.get_room_by_id(room_id)
        if room:
            updated_room = self.room_repository.update_room(room, data)
        # Dependendo do seu design, você pode optar por fazer commit aqui ou no repository.
        # db.session.commit()
            return updated_room.json()
        return None

    
    def get_rooms_by_type(self, room_type):
        return [room.json() for room in self.room_repository.find_by_type(room_type)]

    def reserve_room_by_period(self, room_id, start_time, end_time):
        room = self.room_repository.find_by_id(room_id)
        
        if room is None:
            return {'error': 'Room not found'}
            
        try:
            start_datetime = datetime.strptime(start_time, '%d/%m/%Y %H:%M:%S')
            end_datetime = datetime.strptime(end_time, '%d/%m/%Y %H:%M:%S')
        except ValueError:  
            return {'error': 'Invalid date format'}
            
        if start_datetime >= end_datetime:
            return {'error': 'Invalid time period'}
        
        if any(start_datetime < reservation['end_time'] and end_datetime > reservation['start_time'] for reservation in room.reservations):
            return {'error': 'Room already occupied during this period'}
        
        room.reservations.append({'start_time': start_datetime, 'end_time': end_datetime})
        
        # Adapte o próximo comando ao que está implementado no seu repositório ou ORM.
        self.room_repository.save(room)
        
        # Adapte o próximo comando para o método correto se to_json() não estiver definido na sua classe Room.
        return {'message': 'Room reserved successfully', 'room_details': room.to_json()}

    def create_event(self, room_id, title, organizer, start_time, end_time, participants=None, description=None):
        room = self.room_repository.find_by_id(room_id)
        if not room:
            return {'error': 'Room not found'}
    
        event = EventModel(title=title, organizer=organizer, start_time=start_time, end_time=end_time, participants=participants, description=description)
        room.events.append(event)
        room.save_to_db()

        return event.json()

    def get_all_events(self):
        return [event.json() for event in EventModel.query.all()]

    def get_event_by_id(self, event_id):
        event = EventModel.query.get(event_id)
        if not event:
            return None
        return event.json()

    def update_event(self, event_id, data):
        event = EventModel.query.get(event_id)
        if not event:
            return None

        if 'title' in data:
            event.title = data['title']
        if 'organizer' in data:
            event.organizer = data['organizer']
        if 'start_time' in data:
            event.start_time = data['start_time']
        if 'end_time' in data:
            event.end_time = data['end_time']
        if 'participants' in data:
            event.participants = ",".join(data['participants'])
        if 'description' in data:
            event.description = data['description']

        event.save_to_db()

        return event.json()

    def delete_event(self, event_id):
        event = EventModel.query.get(event_id)
        if not event:
            return False
        event.delete_from_db()
        return True

    def generate_report(self, start_time, end_time, room_type=None):
        try:
            start_datetime = datetime.datetime.strptime(start_time, '%d/%m/%Y %H:%M:%S')
            end_datetime = datetime.datetime.strptime(end_time, '%d/%m/%Y %H:%M:%S')
        except ValueError:
            return {'error': 'Invalid date format'}

        if start_datetime >= end_datetime:
            return {'error': 'Invalid time period'}

        rooms = self.room_repository.find_all()

        # Filtrar por tipo de sala se especificado
        if room_type:
            rooms = [room for room in rooms if room.room_type == room_type]

        # Construindo o relatório
        report = []
        for room in rooms:
            room_data = {
                "room_name": room.name,
                "room_type": room.room_type,
                "events": []
            }
            
            for event in room.events:
                if event.start_time >= start_datetime and event.end_time <= end_datetime:
                    room_data["events"].append(event.json())

            if room_data["events"]:  # Se houver eventos na sala durante o período, adicionamos no relatório
                report.append(room_data)

        return report