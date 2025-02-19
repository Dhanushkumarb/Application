import os
import logging
import sys
from datetime import datetime

level_str="[%(asctime)s]: %(levelname)s: %(module)s:  %(message)s"

file_dir="log"
file_path=os.path.join(file_dir,"requirements.log")
os.makedirs(file_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=level_str,
    
    handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("mlprojectlogger")
