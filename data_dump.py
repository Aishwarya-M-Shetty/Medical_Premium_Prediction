from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://cluster0.yorhz0i.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='/Users/aishwaryashetty/Downloads/X509-cert-8459402186787425190.pem')
DATA_FILE_PATH="/Users/aishwaryashetty/Desktop/Study/Deep_Learning_Module/Medical_Premium_Prediction/insurance.csv"
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows & columns:{df.shape}")

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)