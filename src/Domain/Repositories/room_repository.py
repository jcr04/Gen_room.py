from datetime import datetime
from Infrastructure.models.room import RoomModel
from Infrastructure.database import db  # Importe também o objeto db, caso precise.
from Infrastructure.models.room import RoomModel, EventModel


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

    def create_event(self, room_id, title, organizer, start_time, end_time, participants=None, description=None):
        room = self.find_by_id(room_id)
        if not room:
            return None

        event = EventModel(title=title, organizer=organizer, start_time=start_time, end_time=end_time, participants=participants, description=description)
        room.events.append(event)
        db.session.add(event)
        db.session.commit()

        return event

    def get_all_events(self):
        return EventModel.query.all()

    def get_event_by_id(self, event_id):
        return EventModel.query.get(event_id)

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

        db.session.commit()

        return event

    def delete_event(self, event_id):
        event = EventModel.query.get(event_id)
        if not event:
            return False
        db.session.delete(event)
        db.session.commit()
        return True


    def generate_report(self):
        # Total rooms
        total_rooms = RoomModel.query.count()

        # Rooms with maximum capacity
        max_capacity = db.session.query(db.func.max(RoomModel.capacity)).scalar()
        rooms_with_max_capacity_count = RoomModel.query.filter_by(capacity=max_capacity).count()

        # Rooms available in matutino and noturno shifts
        matutino_available = RoomModel.query.filter_by(shift='matutino', is_occupied=False).count()
        noturno_available = RoomModel.query.filter_by(shift='noturno', is_occupied=False).count()

        # Rooms reserved
        rooms_reserved = RoomModel.query.filter_by(is_occupied=True).count()

        # Rooms in events
        rooms_in_events = RoomModel.query.filter(RoomModel.events.any()).count()

        return {
            'total_rooms': total_rooms,
            'rooms_with_max_capacity': rooms_with_max_capacity_count,
            'matutino_available': matutino_available,
            'noturno_available': noturno_available,
            'rooms_reserved': rooms_reserved,
            'rooms_in_events': rooms_in_events
        }
