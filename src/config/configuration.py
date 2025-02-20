from src.constants import *
from src.utils.common import read_yaml_file,create_directories
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import DataTransformationConfig
from src.entity.config_entity import ModelTrainerConfig
from src.entity.config_entity import ModelEvaluationConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_fileapth=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):
        self.config=read_yaml_file(config_filepath)
        self.params=read_yaml_file(params_fileapth)
        self.schema=read_yaml_file(schema_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])
        data_ingestion_config= DataIngestionConfig( 
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    
    def get_data_validation(self) ->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema= schema,
        )
        return data_validation_config
    
    
    def get_data_transformed(self)->DataTransformationConfig:
        config=self.config.data_transformation
        
        create_directories([config.root_dir])
        data_transformed_config= DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformed_config
    
    def get_model_train_config(self)-> ModelTrainerConfig:
        config=self.config.model_training
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_train_data=ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            l1_ratio=params.l1_ratio,
            alpha=params.alpha,
            target_column=schema.name,
        )
        return model_train_data
    
    def get_model_evaluate_config(self)->ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_evaluate_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metrics_file=config.metrics_file,
            all_params=params,
            target_column=schema.name,
        )
        return model_evaluate_config
        