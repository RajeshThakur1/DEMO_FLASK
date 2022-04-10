""""app.py"""

__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"

from flask import Flask, jsonify, request
from flask_cors import  CORS,cross_origin
import logging
import os
import config as cfg


logging.basicConfig(
    filename=os.path.join("logs", "appLogs.log"),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"

)
logger = logging.getLogger(__name__)

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin(origin="*")
def hello_world():
    return "hello world"

@app.route('/add',methods=["POST"])
@cross_origin(origin="*")
def add():
    logger.info("add API triggred")
    a = request.json['a']
    logger.info("number 1 taken")
    b = request.json['b']
    logger.info("number 2 taken")
    return jsonify(a+b)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=False,port=cfg.PORT)
