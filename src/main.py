from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database import db, cors as cors_ext
from controllers.room import room_controller

app = Flask(__name__)

# Configuração do SQLAlchemy para o PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/Gen_room'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
CORS(app)

# Initialize the extensions
db.init_app(app)
api.init_app(app)
cors_ext.init_app(app)  # Use cors_ext to avoid name conflict with flask_cors.CORS

# Map the URL '/static' to the '/static' folder on your filesystem
app.static_url_path = '/static'
app.static_folder = 'static'

app.register_blueprint(room_controller, url_prefix='/api')

# Create the tables in the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
