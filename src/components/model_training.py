from src.config.configuration import ConfigurationManager
from src.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
from src.logging import logger
import os
import pickle
import pandas as pd

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
    
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        train_X=train_data.drop([self.config.target_column],axis=1)
        test_X=test_data.drop([self.config.target_column],axis=1)
        train_y=train_data[[self.config.target_column]]
        test_y=test_data[[self.config.target_column]]
        
        ls=ElasticNet(l1_ratio=self.config.l1_ratio,alpha=self.config.alpha,random_state=42)
        ls.fit(train_X,train_y)
        
        filepath=os.path.join(self.config.root_dir,self.config.model_name)
        
        with open(filepath,'wb') as f:
            pickle.dump(ls,f)