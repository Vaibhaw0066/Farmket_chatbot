from flask import Flask
from flask import render_template,request,redirect,url_for


from flask_socketio import SocketIO

app=Flask(__name__)
socketio=SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/chat')
def chat():
    message=request.args.get('msg')
    print(message)
    return render_template(url_for('index.html'))
@socketio.on('connection_stablished')
def connected(data):
    app.logger.info("{}".format(data['status']))

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("message --->> {} ".format(data['message']))
    socketio.emit('receive_message',data)


if __name__=="__main__":
    socketio.run(app,debug=True)
