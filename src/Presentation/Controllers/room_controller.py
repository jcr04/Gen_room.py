from io import StringIO
from flask import Blueprint, make_response, request, jsonify, Flask
from flask_restful import Api
from Domain.Entities.room import Room
from Application.Services.room_service import RoomService
from Domain.Repositories.room_repository import RoomRepository
from Infrastructure.models.room import EventModel, ReservationModel, RoomModel
from Infrastructure.database import db
import csv
app = Flask(__name__)
room_controller = Blueprint('room_controller', __name__)
api = Api(room_controller)
room_service = RoomService()

def handle_error(message, status_code):
    return jsonify({'error': message}), status_code

# ---------------- Rooms Endpoints ------------------

@room_controller.route('/rooms', methods=['GET'])
def get_all_rooms():
    rooms = RoomModel.find_all()
    rooms_json = [room.json() for room in rooms]
    return jsonify(rooms_json), 200

@room_controller.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()
    room = RoomModel(**data)
    room.save_to_db()
    return room.json(), 201

@room_controller.route('/rooms/<int:room_id>', methods=['GET'])
def get_room_details(room_id):
    room = RoomModel.find_by_id(room_id)
    if room:
        return room.json(), 200
    return handle_error('Room not found', 404)

@room_controller.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room_by_id(room_id):
    room = RoomModel.find_by_id(room_id)
    if room is None:
        return handle_error('Room not found', 404)

    room.delete_from_db()
    return '', 204

@room_controller.route('/rooms/<int:room_id>/update', methods=['PUT'])
def edit_room_by_id(room_id):
    data = request.get_json()
    room = RoomModel.find_by_id(room_id)
    if room is None:
        return handle_error('Room not found', 404)

    # Update room attributes
    for key, value in data.items():
        setattr(room, key, value)
    
    room.save_to_db()
    return room.json(), 200

# ---------------- Reservation Endpoints ------------------

@room_controller.route('/rooms/<string:room_id>/reserve', methods=['POST'])
def reserve_room(room_id):
    room = RoomModel.find_by_id(room_id)
    if not room or room.is_occupied:
        return handle_error('Room not found or already occupied', 404)

    room.is_occupied = True
    room.save_to_db()

    return jsonify({'message': 'Room reserved successfully', 'room_details': room.json()}), 200


@room_controller.route('/rooms/<string:room_id>/reserve-by-period', methods=['POST'])
def reserve_room_by_period(room_id):
    data = request.get_json()
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    
    room = RoomModel.find_by_id(room_id)
    if not room:
        return handle_error('Room not found', 404)
        
    if not room.is_available(start_time, end_time):
        return handle_error('Room already occupied during this period', 400)
    
    room.reserve_room(start_time, end_time)
    return jsonify({'message': 'Room reserved successfully', 'room_details': room.json()}), 200



# ---------------- Additional Room Retrieval Endpoints ------------------

@room_controller.route('/rooms/occupied', methods=['GET'])
def get_occupied_rooms():
    """Retrieve all occupied rooms."""
    occupied_rooms = room_service.get_occupied_rooms()
    return jsonify(occupied_rooms)

@room_controller.route('/rooms/available', methods=['GET'])
def get_available_rooms():
    available_rooms = RoomModel.query.filter_by(is_occupied=False).all()
    return jsonify([room.json() for room in available_rooms])


@room_controller.route('/rooms/by-type/<string:room_type>', methods=['GET'])
def get_rooms_by_type(room_type):
    valid_room_types = ["Sala-Aula", "Sala-Interativa", "Laboratórios", "Auditórios", "Cozinhas"]
    if room_type not in valid_room_types:
        return handle_error('Tipo de sala inválido.', 400)

    rooms = RoomModel.query.filter_by(room_type=room_type).all()

    if not rooms:
        return handle_error('Nenhuma sala encontrada para este tipo.', 404)

    return jsonify([room.json() for room in rooms]), 200

@room_controller.route('/rooms/<int:room_id>/update', methods=['PUT'])
def update_room(room_id):
    data = request.get_json()
    updated_room_json = room_service.update_room(room_id, data)
    if updated_room_json is None:
        return handle_error('Room not found or invalid data', 404)
    return updated_room_json, 200


# ---------------- events Endpoints ------------------

@room_controller.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    room_id = data.get('room_id')

    # Verificar se a sala existe
    room = RoomModel.find_by_id(room_id)
    if not room:
        return handle_error('Room not found', 404)

    # O método **data desempacotará o dicionário, e os nomes das chaves precisam corresponder aos parâmetros esperados pelo construtor do EventModel
    event = EventModel(**data)
    event.save_to_db()

    return event.json(), 201

@room_controller.route('/events', methods=['GET'])
def get_all_events():
    events = EventModel.find_all()
    return jsonify([event.json() for event in events]), 200

@room_controller.route('/rooms/<int:room_id>/events', methods=['GET'])
def get_events_by_room(room_id):
    room = RoomModel.find_by_id(room_id)
    if not room:
        return handle_error('Room not found', 404)
    
    events = EventModel.find_by_room_id(room_id)
    return jsonify([event.json() for event in events]), 200

@room_controller.route('/rooms/<int:room_id>/events', methods=['PUT'])
def update_event(room_id):
    data = request.get_json()
    event_id = data.get('id')

    if not event_id:
        return handle_error('Event ID (id) is required in the request body', 400)

    event = EventModel.find_by_id(event_id)
    if not event or event.room_id != room_id:
        return handle_error('Event not found for the given room', 404)
    
    # Aqui, você pode adicionar validação para os dados
    for key, value in data.items():
        if key != "id":  # Não queremos atualizar o ID do evento
            setattr(event, key, value)

    event.save_to_db()
    return event.json(), 200

@room_controller.route('/rooms/<int:room_id>/events', methods=['DELETE'])
def delete_event(room_id):
    data = request.get_json()
    event_id = data.get('id')

    if not event_id:
        return handle_error('Event ID (id) is required in the request body', 400)

    event = EventModel.find_by_id(event_id)
    if not event or event.room_id != room_id:
        return handle_error('Event not found for the given room', 404)
    
    event.delete_from_db()
    return '', 204


from flask import make_response
from io import StringIO
import csv

@room_controller.route('/rooms/report', methods=['GET'])
def report():
    # Dados agregados
    total_rooms = RoomModel.query.count()
    max_capacity = db.session.query(db.func.max(RoomModel.capacity)).scalar()
    rooms_with_max_capacity = RoomModel.query.filter_by(capacity=max_capacity).count()
    matutino_available = RoomModel.query.filter_by(shift='matutino').outerjoin(ReservationModel).filter(ReservationModel.id == None).count()
    noturno_available = RoomModel.query.filter_by(shift='noturno').outerjoin(ReservationModel).filter(ReservationModel.id == None).count()
    rooms_reserved = RoomModel.query.join(ReservationModel).count()
    rooms_in_events = RoomModel.query.join(EventModel).count()

    # Prepara um objeto StringIO para armazenar dados CSV
    si = StringIO()
    cw = csv.writer(si)

    # Escreve os dados agregados no começo ou fim do arquivo CSV
    aggregated_data = [
        ['Total Rooms', total_rooms],
        ['Rooms with Max Capacity', rooms_with_max_capacity],
        ['Matutino Available', matutino_available],
        ['Noturno Available', noturno_available],
        ['Rooms Reserved', rooms_reserved],
        ['Rooms in Events', rooms_in_events]
    ]

    # Escreve o cabeçalho dos dados agregados
    cw.writerow(['Métrica', 'Valor'])
    cw.writerows(aggregated_data)

# Espaçamento entre seções
    cw.writerow([])

# Escreve o cabeçalho dos dados detalhados de cada sala com cabeçalhos mais legíveis
    cw.writerow(['ID da Sala', 'Nome', 'Tipo de Sala', 'Capacidade', 'Descrição', 'Categoria da Sala', 'Turno', 'Número de Eventos'])

# Obtém todas as salas do banco de dados, possivelmente ordenadas por algum critério
    rooms = RoomModel.query.order_by(RoomModel.name).all()  # Exemplo de ordenação pelo nome
    for room in rooms:
        room_data = room.generate_report()

    room_info = room_data['room_info']
    cw.writerow([
        room_info['id'], room_info['name'], room_info['room_type'], room_info['capacity'],
        room_info['description'], room_info['room_category'], room_info['shift'],
        len(room_data['events'])  # Aqui contamos o número de eventos associados
    ])

    # Prepara a resposta com o arquivo CSV
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=rooms_report.csv"
    output.headers["Content-type"] = "text/csv"
    return output

