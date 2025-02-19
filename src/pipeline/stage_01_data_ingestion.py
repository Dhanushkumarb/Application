from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logging import logger

stage_name= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
                    # Step 1: Initialize ConfigurationManager
        confi = ConfigurationManager()
    
    # Step 2: Get data ingestion config
        data_ingestion_config = confi.get_data_ingestion_config()
    
    # Step 3: Initialize DataIngestion with the config
        data_ingestion = DataIngestion(config=data_ingestion_config)
    
    # Step 4: Download the file
        data_ingestion.download_file()
    
    # Step 5: Extract the zip file
        data_ingestion.get_unzip_file()
        

    
if __name__ =="__main__":
    try:
        logger.info(f" >>>>>>>>>>>>> stage {stage_name} started ")
        obj=DataIngestionTrainingPipeline
        obj.main()
        logger.info(f" >>>>>>>>>>>>>>stage {stage_name} completed")
    except Exception as r:
        logger.exception (e)
        raise e
    
        