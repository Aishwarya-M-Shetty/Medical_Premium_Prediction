import pymongo
#from pymongo.mongo_client import MongoClient
import pandas as pd
import os,sys
import json
import numpy as np
from dataclasses import dataclass

@dataclass
class EnvironmentVariable:
    mongo_db_url=os.getenv("MONGO_DB_URL")
    

env_var=EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_var.mongo_db_url,tlsCertificateKeyFile='/Users/aishwaryashetty/Downloads/X509-cert-8459402186787425190.pem')
TARGET_COLUMN ="expenses"
print(f"connection established")