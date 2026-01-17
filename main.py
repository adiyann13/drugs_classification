import sys
import os

exc_type, exc_obj, exc_tb = sys.exc_info()
class CustomException(Exception):
    def __init__(self,message,error_message,file_name):
        super().__init__(message)
        self.error_message = error_message
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return f'the exception {self.error_message} has occurrd in the file {self.file_name}'
