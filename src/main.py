from flask import Flask
from flask_restful import Api
from psycopg2 import apilevel
from Presentation.Controllers.room_controller import room_controller
from Infrastructure.database import db, cors as cors_ext

app = Flask(__name__)
api = Api(room_controller)

# Configuração do SQLAlchemy para o PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@127.0.0.1:5432/Gen_room'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the extensions
db.init_app(app)
api.init_app(app)
cors_ext.init_app(app)  # Use cors_ext to avoid name conflict with flask_cors.CORS

app.register_blueprint(room_controller, url_prefix='/api')

# Create the tables in the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
