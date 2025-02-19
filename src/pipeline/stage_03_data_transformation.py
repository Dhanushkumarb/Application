from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logging import logger

STAGE_NAME=" Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformed()
        data_transformed=DataTransformation(config=data_transformation_config)
        data_transformed.train_test_split()
        
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} initiated")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed ")
            
    except Exception as e:
        logger.exception(e)
        raise e
        