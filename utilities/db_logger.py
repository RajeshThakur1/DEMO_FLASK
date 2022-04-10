__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"


import pymongo
import logging

import config as cfg

logger = logging.getLogger(__name__)

myclient = pymongo.MongoClient(cfg.MONGO_DB_URL)
mydb = myclient[cfg.DB_NAME]

