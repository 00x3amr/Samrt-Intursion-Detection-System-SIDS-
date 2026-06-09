from flask import Flask, request

app = Flask(__name__)

latest_data = {}

@app.route("/upload", methods=["POST"])
def upload():
    global latest_data
    latest_data = request.json
    return {"status": "ok"}

@app.route("/latest", methods=["GET"])
def latest():
    return latest_data

app.run(host="0.0.0.0", port=5000)