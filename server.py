from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

players = {}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# 👥 игроки
@socketio.on("update")
def update(data):
    players[data["id"]] = data
    emit("players", players, broadcast=True)

# 🎤 голос (WebRTC сигналинг)
@socketio.on("voice-offer")
def voice_offer(data):
    emit("voice-offer", data, broadcast=True)

@socketio.on("voice-answer")
def voice_answer(data):
    emit("voice-answer", data, broadcast=True)

@socketio.on("voice-candidate")
def voice_candidate(data):
    emit("voice-candidate", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)