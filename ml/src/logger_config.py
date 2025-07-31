import logging
import sys

def setup_logger():
    logger = logging.getLogger()
    
     # Clear any existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()
        
    # Set the logging level (e.g., INFO, DEBUG)
    logger.setLevel(logging.INFO)
    
    # Create a formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Create a handler to print to the console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
     # Add the handler to the logger
    logger.addHandler(console_handler)