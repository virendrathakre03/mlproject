import sys
import traceback

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """_summary_

    Args:
        error (_type_): _description_
        error_detail (sys): _description_

        Creates a detailed error message with file_name ,line number and error message. 
        
        Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module (pass sys).

        Returns:
        str: Formatted error message.
    """
    _, _, exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line [{line_number}] with message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        """
        Custom exception that logs detailed error information.

        Args:
            error_message (str): The custom error message.
            error_detail (sys): The sys module for traceback.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
