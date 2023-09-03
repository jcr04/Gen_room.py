# main.py
from flask import Flask
from Presentation.Controllers.room_controller import room_app
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Defina as informações gerais da API
app.config['SWAGGER_INFO'] = {
    'title': 'Sua API de Salas',
    'version': '1.0',
    'description': 'Documentação interativa da API de Salas',
}

# Configure o Swagger UI
SWAGGER_URL = '/api/swagger'  # URL da página do Swagger
API_URL = '/static/swagger.json'  # URL da especificação Swagger em JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sua API de Salas"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(room_app, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
