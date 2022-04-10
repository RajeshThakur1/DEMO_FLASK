"""config.py"""

__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"

import os

instance_type = os.environ['INSTANCE_TYPE']

if instance_type == "PRODUCTION":
    DB_NAME = "pybron_Faculties"
elif instance_type == "STAGE":
    DB_NAME = "pybron_Faculties"
elif instance_type == "DEV":
    DB_NAME = "pybron_Faculties"

MONGO_DB_URL = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
COLLECTION_NAME = "pybron"

PORT = 7000