from flask import Flask, Blueprint
from flask_socketio import SocketIO, send
from flask_cors import CORS
from api.api import api
from mongoengine import *

from api.api import upload_db

connect('storylab')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)
CORS(app)

app.register_blueprint(api, url_prefix='/api')

@socketio.on('json')
def handleMessage(data):
    print('received json: ' + str(data))
    line = upload_db(data)
    send(data, broadcast=True, json=True)


if __name__ == '__main__':
    socketio.run(app)