from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def hello():

  return render_template('index.html')



@socketio.on('connect')
def handle_connect():
  print("Cliente connected")

@socketio.on('message')
def handle_message(msg):
  print("Mensagem:", msg)
  socketio.emit('message', msg)

if __name__ == '__main__':
  socketio.run(app, debug=True)