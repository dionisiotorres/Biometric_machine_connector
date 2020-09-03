from app import app
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import sys
import os
import json
sys.path.insert(1,os.path.abspath("./pyzk"))
from zk import ZK, const

app.config['DEVICE_IP'] = os.getenv('BIOMETRIC_DEVICE_IP')
app.config['DEVICE_PORT'] = int(os.getenv('BIOMETRIC_DEVICE_PORT'))
app.config['DEVICE_TIME_OUT'] = int(os.getenv('BIOMETRIC_DEVICE_TIME_OUT'))
app.config['DEVICE_PASSWORD'] = os.getenv('BIOMETRIC_DEVICE_PASSWORD')
app.config['DEVICE_FORCE_UDP'] = bool(os.getenv('BIOMETRIC_DEVICE_FORCE_UDP'))
app.config['DEVICE_OMMIT_PING'] = bool(os.getenv('BIOMETRIC_DEVICE_OMMIT_PING'))

class Attendance(Resource):

    @app.route('/get_attendance', methods = ['GET'])
    def get_attendance():
        zk = ZK(app.config['DEVICE_IP'], 
            port=app.config['DEVICE_PORT'], 
            timeout=app.config['DEVICE_TIME_OUT'], 
            password=app.config['DEVICE_PASSWORD'], 
            force_udp=app.config['DEVICE_FORCE_UDP'], 
            ommit_ping=app.config['DEVICE_OMMIT_PING'])
        try:
            conn = zk.connect()
            # conn.disable_device()
            attendance = conn.get_attendance()
            data = []
            for atten in attendance:
                data.append({'user_id': atten.user_id,'timestamp':str(atten.timestamp),'status':atten.status,'punch':atten.punch})
            return {'status':'success','attendance' : data}
        except Exception as e:
            return {'status' : format(e)}