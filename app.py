""""app.py"""

__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"

from flask import Flask, jsonify, request
from flask_cors import  CORS,cross_origin
import logging
import os
import config as cfg
from utilities import db_logger, all_utils
logging.basicConfig(
    filename=os.path.join("logs", "appLogs.log"),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"

)
logger = logging.getLogger(__name__)

app = Flask(__name__)
cors = CORS(app)

# GET === whenever you have to fetch the data from DB
# POST = Insert something in the DB
# DELETE:- if we have to remove the data
# put === if you want to update the eisting document


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

@app.route('/insert_faculty',methods=["POST"])
@cross_origin(origin="*")
def insert_faculty():
    logger.info("Inserting the new faculty in pybron faculty")
    com_name = request.json['companyName']
    logger.info(f"company name {com_name}")
    faculty_name = request.json['faculty_name']
    logger.info(f"faculty name {faculty_name}")
    specilization = request.json['specilization']
    logger.info(f"specilization {specilization}")
    price = request.json['price']
    logger.info(f"price {price}")
    obj = {"companyName": com_name, "faculty_name": faculty_name, "specilization": specilization, "price": price}
    collection_name = cfg.COLLECTION_NAME
    db_logger.insert_obj(obj=obj, collection_name=collection_name)
    return jsonify(all_utils.response_format({"status_code":200,"message":"data inserted Successfully"}))


@app.route('/upsert_faculty',methods=["POST"])
@cross_origin(origin="*")
def upsert_faculty():
    logger.info("Inserting the new faculty in pybron faculty")
    com_name = request.json['companyName']
    logger.info(f"company name {com_name}")
    faculty_name = request.json['faculty_name']
    logger.info(f"faculty name {faculty_name}")
    specilization = request.json['specilization']
    logger.info(f"specilization {specilization}")
    price = request.json['price']
    logger.info(f"price {price}")
    obj = {"companyName": com_name, "faculty_name": faculty_name, "specilization": specilization, "price": price}
    collection_name = cfg.COLLECTION_NAME
    db_logger.upsert_obj(obj=obj, collection_name=collection_name,faculty_name="romio")
    return jsonify(all_utils.response_format({"status_code":200,"message":"data upserted Successfully"}))





if __name__=="__main__":
    app.run(host="0.0.0.0",debug=False,port=cfg.PORT)
