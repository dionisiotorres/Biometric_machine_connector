# Getting started!

**Before Started :**

1. run `pip install -r requirements.txt`
2. run `python3 -m venv virtualenv`
3. run `source virtualenv/bin/active`
4. run `pip install -r requirements.txt`

**Environment**
1. add `.env`
`BIOMETRIC_DEVICE_IP='{device_IP}'`
`BIOMETRIC_DEVICE_PORT={device_port}`
`BIOMETRIC_DEVICE_TIME_OUT={set_Time_Out}`
`BIOMETRIC_DEVICE_PASSWORD={password}`
`BIOMETRIC_DEVICE_FORCE_UDP=`
`BIOMETRIC_DEVICE_OMMIT_PING=`

2. Flask Environment `.flaskenv`

`FLASK_ENV={development/production}`

`FLASK_APP=main.py`