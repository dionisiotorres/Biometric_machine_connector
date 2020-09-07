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

class Base(Resource):

    @app.route('/connect', methods = ['GET'])
    def connect():
        zk = ZK(app.config['DEVICE_IP'], 
            port=app.config['DEVICE_PORT'], 
            timeout=app.config['DEVICE_TIME_OUT'], 
            password=app.config['DEVICE_PASSWORD'], 
            force_udp=app.config['DEVICE_FORCE_UDP'], 
            ommit_ping=app.config['DEVICE_OMMIT_PING'])
        try:
            conn = zk.connect()
            conn.disconnect()
            # conn.disable_device()
            return {'status':'success','message':'Biometric Device \'%s\' is Up/Reachable' % (app.config['DEVICE_IP'])}
        except Exception as e:
            return {'status':'failed','message':'Biometric Device \'%s\' is Down/Unreachable' % (app.config['DEVICE_IP'])}
            # return {'status' : format(e)}

    @app.route('/restart', methods = ['GET'])
    def restart():
        zk = ZK(app.config['DEVICE_IP'], 
            port=app.config['DEVICE_PORT'], 
            timeout=app.config['DEVICE_TIME_OUT'], 
            password=app.config['DEVICE_PASSWORD'], 
            force_udp=app.config['DEVICE_FORCE_UDP'], 
            ommit_ping=app.config['DEVICE_OMMIT_PING'])
        try:
            conn = zk.connect()
            # conn.test_voice(index=1) 
            conn.restart()
            # conn.disconnect()
            # conn.disable_device()
            return {'status':'success'}
        except Exception as e:
            return {'status' : format(e)}

            
    