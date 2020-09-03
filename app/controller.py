from app import app
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return make_response(
      jsonify(
        info='Attendance Biometric Web Service',
        author='Witech Enterprise',
        version='0.1'
      ), 200
    )
    