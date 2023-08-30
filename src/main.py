# main.py
from flask import Flask
from Presentation.Controllers.room_controller import room_app

app = Flask(__name__)

# Registrar o blueprint do room_controller
app.register_blueprint(room_app, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

