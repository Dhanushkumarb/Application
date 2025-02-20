from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTrainer
from src.logging import logger

stage_name="Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        model_data_config=config.get_model_train_config()
        model_data=ModelTrainer(config=model_data_config)
        model_data.train()
        
if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>> stage{stage_name} is initiated")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {stage_name} is completed")
    except Exception as e:
        logger.exception(e)
        raise e   