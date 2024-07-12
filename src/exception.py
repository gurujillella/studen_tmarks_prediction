import sys
import  logging

#error details is present in the sys
def error_message_detail(err,error_detail:sys):
    #exc_info of the error details gives the information regarding to the error ,in which file ,in which line number all those 
    #information is availble note:it returns the three values but all the required information is available in third value so i use _,_exc_tb
    _,_,exc_tb=error_detail.exc_info()
    #here exc_tb contains the tb_frame contains the f_code in the contains the co_filename its our filename
    file_name=exc_tb.tb_frame.f_code.co_filename
    Error_Message="Error Occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,
        str(err)
    )
    return Error_Message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        #here we inherit from the error message from the exception
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        def __str__(self):
            return self.error_message
