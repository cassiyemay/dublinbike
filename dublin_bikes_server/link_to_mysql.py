from rds_config import *
import sqlalchemy as sqla
from sqlalchemy import create_engine
import pymysql
import traceback
import glob
import os
import sys
import datetime
import pymysql


def connect_to_sql():

    rds_db = rds_config()
    rds_db.db_config_setup()
    
    host = rds_db.db_endpoint
    name = rds_db.db_username
    password = rds_db.db_password
    db = rds_db.db_name
    port = 3306

    try:
        engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}"
                               .format(name, password, host, port, db), echo=True)
    except:
        print("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()
        
    else:
        print("[",str(datetime.datetime.now()), "] Finished link to RDS...")
        return engine
