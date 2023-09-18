from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfg
import sys




if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        #data_ingestion_config = DataIngestionConfg()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)