import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.get("/")
def index():
    return flask.render_template("index.html")

@socketio.on("touch_event")
def touch_event(data):
    print(data)

@app.post("/api/auth")
def auth():
    return "auth"

if __name__ == "__main__":
    app.run(port=4155, host="0.0.0.0")