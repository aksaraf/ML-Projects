import sys
import logging

# Function to create a detailed error message
def error_message_detail(error, error_detail: sys):
    # Unpack the error details
    _, _, exc_tb = error_detail.exc_info()
    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Create a detailed error message
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # Return the detailed error message
    return error_message

# Custom exception class
class CustomException(Exception):
    # Constructor for the custom exception
    def __init__(self, error_message, error_detail: sys):
        # Call the constructor of the parent class (Exception) with the provided error message
        super().__init__(error_message)
        # Create a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    # Method to convert the exception to a string
    def __str__(self):
        # Return the detailed error message when converting to a string
        return self.error_message
