from src.logging import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage_name="Data Ingestion Config"
try:
    logger.info(f">>>> stage {stage_name} started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {stage_name} completed  <<<<")
except Exception as e:
    logger.exception(e)
    raise e 