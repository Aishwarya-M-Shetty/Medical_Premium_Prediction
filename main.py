from insurance_predictor.logger import logging
from insurance_predictor.exception import InsuranceException
import os,sys
from insurance_predictor.utils import get_collection_as_dataframe

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
        get_collection_as_dataframe(database_name="INSURANCE",collection_name="INSURANCE_PROJECT")
    except Exception as e:
        print(e)

