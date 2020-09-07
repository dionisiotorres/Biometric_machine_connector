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

class User(Resource):

    @app.route('/get_users', methods = ['GET'])
    def get_users():
        zk = ZK(app.config['DEVICE_IP'], 
                port=app.config['DEVICE_PORT'], 
                timeout=app.config['DEVICE_TIME_OUT'], 
                password=app.config['DEVICE_PASSWORD'], 
                force_udp=app.config['DEVICE_FORCE_UDP'], 
                ommit_ping=app.config['DEVICE_OMMIT_PING'])
        try:
            conn = zk.connect()
            # conn.disable_device()
            user = conn.get_users()
            data = {
                'user':[]
            }
            for uid in user:
                privilege = 'User'
                if uid.privilege == const.USER_ADMIN:
                    privilege = 'Admin'
                data['user'].append({'uid': uid.uid,'name':uid.name,'user_id':uid.user_id,'privilege':privilege,'group_id':uid.group_id})
            return {'status':'success','data' : data}
        except Exception as e:
            return {'status' : format(e)}
