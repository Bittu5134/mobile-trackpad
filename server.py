import flask
import flask_socketio
import multiprocessing

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app, max_buffer_size=1024**2)

@app.get("/")
def index():
    # if OAuthCode != flask.request.args.get("code", default=None): return "Invalid OAuth Code"
    return flask.render_template("index.html")

@socketio.on("touch_event")
def touch_event(data):
    mousePos.put(data)


def start(Code, Queue:multiprocessing.Queue):
    global OAuthCode, mousePos
    OAuthCode = Code
    mousePos = Queue
    app.run(port=4155, host="0.0.0.0")