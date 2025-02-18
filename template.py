import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

#project_name="mlproject"
list_of_file=[
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"file dir has been created {filedir} in fiile name {filename}")
        
        if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath,'w') as f: 
                pass
                logging.info("file has been created emptly")
                
    else:
        logging.info('f{filename} is alreday exist') 
            
            

