import pickle
import os
from pathlib import Path
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        with open('artifacts/model_trainer/model.pkl','rb') as f:
            self.model=pickle.load(f)
        
    def prediction(self,data):
        
        prediction= self.model.predict(data)
        
        return prediction
    
    
