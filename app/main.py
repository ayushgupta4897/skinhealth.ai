from flask_cors import CORS, cross_origin
from flask import Flask, json, request, send_from_directory, abort, jsonify, redirect, render_template

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=8080)