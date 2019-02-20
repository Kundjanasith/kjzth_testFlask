import os
from flask import Flask, request, jsonify, send_from_directory
from json import dumps, loads
app = Flask(__name__, static_folder=".", template_folder=".")

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response

@app.route("/")
def home():
    return 'Kundjanasith Thonglek . . .'

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)