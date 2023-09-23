from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from Presentation.Controllers.room_controller import room_app
from Presentation.Controllers.resource_controller import resource_app
from flask_cors import CORS

from database import db, api, cors
from controllers.room import room_controller

app = Flask(__name__)

# Configuração do SQLAlchemy para o PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/Gen_room'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
CORS(app)

# Inicialize as extensões
db.init_app(app)
api.init_app(app)
cors.init_app(app)

# Mapeie a URL '/static' para a pasta '/static' no seu sistema de arquivos
app.static_url_path = '/static'
app.static_folder = 'static'

app.register_blueprint(room_controller, url_prefix='/api')

# Crie as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Defina as informações gerais da API
app.config['SWAGGER_INFO'] = {
    'title': 'Sua API de Salas',
    'version': '2.0',
    'description': 'Documentação interativa da API de Salas',
}

# Configure o Swagger UI
SWAGGER_URL = '/api/swagger'  # URL da página do Swagger
API_URL = '/static/swagger.json'  # Verifique se esta URL está correta
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "GenRoom: Sua API de Salas"
    }
)

# Registre o Swagger UI Blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
