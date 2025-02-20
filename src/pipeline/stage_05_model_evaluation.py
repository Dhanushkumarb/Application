from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logging import logger

stage_name="Model Evaluation Stage"
class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluate_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_file()
            

        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {stage_name} is initiated <<<<<")
        obj=ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {stage_name} is completed <<<<<<")
    except Exception as e:
        logger.exception (e)
        raise e
