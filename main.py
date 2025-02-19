from src.logging import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
stage_name="Data Ingestion Config"
try:
    logger.info(f">>>> stage {stage_name} started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {stage_name} completed  <<<<")
except Exception as e:
    logger.exception(e)
    raise e  

stage_name="Data Validation Config"
try:
    logger.info(f">>>> stage {stage_name} started")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {stage_name} completed  <<<<")
except Exception as e:
    logger.exception(e)
    raise e  

stage_name="Data Transformation Config"
try:
    logger.info(f">>>> stage {stage_name} started")
    data_ingestion=DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {stage_name} completed  <<<<")
except Exception as e:
    logger.exception(e)
    raise e  