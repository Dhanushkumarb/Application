from sklearn.metrics import mean_squared_error,r2_score
from src.logging import logger
import pandas as pd
import numpy as np
import os
import pickle
from src.utils.common import save_json
from src.entity.config_entity import ModelEvaluationConfig
from src.config.configuration import ConfigurationManager
from pathlib import Path
class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
        
    def evaluate_metric(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mse=mean_squared_error(actual,pred)
        score=r2_score(actual,pred)
        return rmse,mse,score
    
    def save_file(self):
        data_test=pd.read_csv(self.config.test_data_path)
        with open(self.config.model_path, 'rb') as file:
            model = pickle.load(file)

        
            
        test_X=data_test.drop([self.config.target_column],axis=1)
        test_y=data_test[[self.config.target_column]]
        
        predicted_values=model.predict(test_X)
        
        (rmse,mse,score)=self.evaluate_metric(test_y,predicted_values)
        
        scores={"rmse":rmse,"mse":mse,"score":score}
        save_json(path=Path(self.config.metrics_file),data=scores)
