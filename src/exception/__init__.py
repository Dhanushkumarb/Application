import sys
import os
from src.logging import logger

def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error="errror occured in python script [{0}] line number [{1}] message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error


class CustomException(Exception):
    def __init__(self,error,error_details:sys):
        super().__init__(error)
        self.error=error_message_details(error,error_details=error_details)
        
    def __str__(self):
        return self.error
    
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logger.info("Zero division error")
        raise CustomException(e,sys)