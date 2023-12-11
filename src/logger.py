# Import necessary libraries
import logging  # For handling logs
import os  # For working with the operating system
from datetime import datetime  # For dealing with dates and times

# Create a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

# Create a path for storing logs in a 'logs' folder within the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# Create the 'logs' folder if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Create the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the file where logs will be stored
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define the format of log messages
    level=logging.INFO,  # Set the logging level to INFO, meaning it will log INFO and higher-level messages
)
