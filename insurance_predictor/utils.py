import numpy as np
import pandas as pd

import os,sys
from insurance_predictor.exception import InsuranceException
from insurance_predictor.config import mongo_client
from insurance_predictor.logger import logging

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        logging.info(f"reading data from db: {database_name} and collection name {collection_name}")
        df=pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Find columns:{df.columns}")
        if "_id" in df.columns:
            logging.info(f"Drop _id column")
            df=df.drop("_id",axis=1)
        logging.info(f"rows and columns in df:{df.shape}")
        return df
    
    except Exception as e:
        raise InsuranceException(e,sys)
