import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DATA_FILE = 'data.json'

# This is the default data that will load the very first time you run the app
DEFAULT_DATA = {
    "baptismsYear": 91,
    "names": ["Alexandra", "Crescencie", "Franklin", "Maya", "Elena", "Tina", "Piero", "Jimmy", "Audrey", "Nadège", "Confidence", "Ludovic", "Ludovic", "Helena", "Teresa", "Maria", "Josuana", "Domingos", "Sinclair", "Stephen", "Jonas", "Chadli Nganga", "Blessing", "Olife", "André", "Jonaas", "Mary"],
    "stages": [
        {"label": "Nouveaux Amis", "tw": 1364, "lw": 1424, "avg": 1043, "color": "#1D9E75"},
        {"label": "Amis à l'Église", "tw": 359, "lw": 381, "avg": 322, "color": "#D4943A"},
        {"label": "Avec une Date", "tw": 71, "lw": 66, "avg": 54, "color": "#C05535"},
        {"label": "Baptisé", "tw": 16, "lw": 8, "avg": 8, "color": "#3A7FCC"}
    ],
    "lessons": {"tw": 833, "lw": 872, "avg": 482},
    "members": {"tw": 126, "lw": 139, "avg": 119}
}

# Helper function to load data from the JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump(DEFAULT_DATA, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Route 1: Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: Handle the API data (GET for fetching, POST for saving)
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        # Someone clicked "Appliquer", save the new data
        new_data = request.json
        with open(DATA_FILE, 'w') as f:
            json.dump(new_data, f)
        return jsonify({"status": "success"})
    
    # Otherwise, it's a GET request, so send the current data
    return jsonify(load_data())

if __name__ == '__main__':
    # Start the Flask server
    app.run(port=5000)
