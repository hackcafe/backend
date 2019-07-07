import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/fetch-hacks', methods=['GET'])
def fetch_hacks():
    with open("hacks.json", "r") as read_file:
        hacks = json.load(read_file)
        return jsonify(hacks)

@app.route('/request-package', methods=['POST'])
def request_package():
    print(request.json)
    return jsonify({ 'status': 'OK' })

if __name__ == "__main__":
    app.run(debug=True)