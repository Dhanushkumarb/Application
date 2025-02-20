import os
import sys
import joblib
import yaml
from src.logging import logger
from src.exception import CustomException
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
from pathlib import Path
import json

@ensure_annotations
def read_yaml_file(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} has loaded succesfully")
            return ConfigBox(content)
    except Exception as e:
        logger.info("yaml file is empty")
        raise CustomException(e,sys)
    
    
@ensure_annotations   
def create_directories(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"path has been created in {path}")
            
            
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved to {path}")
    
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)
    logger.info(f"file loaded succesfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"file has been saved")
    
    
    
@ensure_annotations
def load_bin(path:Path):
    data=joblib.load(path)
    logger.info(f"binary file has been loaded{path}")
    return data