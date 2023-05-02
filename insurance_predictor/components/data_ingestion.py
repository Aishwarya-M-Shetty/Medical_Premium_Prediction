import pandas as pd
import os,sys
import numpy as np
from insurance_predictor.entity import config_entity
from insurance_predictor.exception import InsuranceException
from insurance_predictor.entity import artifact_entity
from  insurance_predictor import utils
from insurance_predictor.logger import logging
from sklearn.model_selection import train_test_split

class data_ingestion: 
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise InsuranceException(e,sys)
    
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info(f"Export collection data as pandas dataframe")
            df:pd.DataFrame = utils.get_collection_as_dataframe(
            database_name=self.data_ingestion_config.database_name,
            collection_name=self.data_ingestion_config.collection_name
            )
            logging.info(f"saved data in feature store")
            df.replace(to_replace="na",value=np.NaN,inplace=True)

#Save data in feature store
            logging.info("make feature store dir if not available")
            feature_store_dir=os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            logging.info(f"save dataframe to feature store folder")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            logging.info(f"splitting our dataset into train and test set")
            train_df,test_df =train_test_split(df,test_size=self.data_ingestion_config.test_size,random_state=1)
            
            logging.info("creating dataset dir folder")
            dataset_dir=os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            logging.info("saving dataset to feature store")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)

            #Prepare artifact folder
            data_ingestion_artifact=artifact_entity.DataIngestionArtifact(
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
            train_file_path=self.data_ingestion_config.train_file_path,
            test_file_path=self.data_ingestion_config.test_file_path
            )

        
        except Exception as e:
            raise InsuranceException(e,sys)
        
