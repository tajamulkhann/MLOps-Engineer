import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current timestamp  
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a 'logs' directory inside the current working directory and store logs there
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)  # Create the directory if it doesn't exist

# Full path to store the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # File to save logs
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO,  # Minimum level of logs to be captured
)