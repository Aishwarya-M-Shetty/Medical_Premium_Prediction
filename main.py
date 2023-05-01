from insurance_predictor.logger import logging
from insurance_predictor.exception import InsuranceException
import os,sys
from insurance_predictor.utils import get_collection_as_dataframe
from insurance_predictor.entity.config_entity import DataIngestionConfig
from insurance_predictor.entity import config_entity

def test_logger_and_exception():
    try:
        logging.info("starting the test_logger_and_exception function")
        result=3/0
        print(result)
        logging.info("ending the test_logger_and_exception function")
        
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)
    

if __name__=="__main__":
    try:
        #test_logger_and_exception()
        #get_collection_as_dataframe(database_name="INSURANCE",collection_name="INSURANCE_PROJECT")
        print("inside main")
        training_pipeline_config=config_entity.TrainingPipelineConfig()
        data_ingestion_config=config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)

