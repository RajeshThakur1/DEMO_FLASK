__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"


import pymongo
import logging

import config as cfg

logger = logging.getLogger(__name__)

myclient = pymongo.MongoClient(cfg.MONGO_DB_URL)
mydb = myclient[cfg.DB_NAME]

def insert_obj(obj,collection_name):
    mycol = mydb[collection_name]
    mycol.insert_one(obj)
    logger.info(f"{obj} inserted into {str(mycol)}")

def upsert_obj(obj,collection_name,faculty_name):
    mycol = mydb[collection_name]
    filter = {'faculty_name':faculty_name}
    newvalues = {"$set": obj}
    mycol.update_one(filter, newvalues, upsert=True)
    logger.info(f"{obj} upserted successfully")




