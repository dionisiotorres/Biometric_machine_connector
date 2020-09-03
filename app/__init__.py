from flask import Flask
import logging

app = Flask(__name__)

from . import attendance
from . import controller
from . import user

if __name__ == "__main__":
   logging.basicConfig(filename='error.log',level=logging.DEBUG)
   app.run(host='0.0.0.0', port=5000)