import flask
import flask_socketio
import queue

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.get("/")
def index():
    if OAuthCode != flask.request.args.get("code", default=None): return "Invalid OAuth Code"
    return flask.render_template("index.html")

@socketio.on("touch_event")
def touch_event(data):
    print(data)


def start(Code, Queue):
    global OAuthCode, mousePos
    OAuthCode = Code
    mousePos = Queue
    app.run(port=4155, host="0.0.0.0")