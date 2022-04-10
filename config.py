"""config.py"""

__author__ = "Rajesh"
__copyright__ = "xyz"
__created_date__ = "10-04-2022"

import os

instance_type = os.environ['INSTANCE_TYPE']

if instance_type == "PRODUCTION":
    DB_NAME = "prod_db"
elif instance_type == "STAGE":
    DB_NAME = "stage_db"
elif instance_type == "DEV":
    DB_NAME = "dev_db"

PORT = 7000