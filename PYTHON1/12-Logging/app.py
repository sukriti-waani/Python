import logging

# Configuring logging
logging.basicConfig(
    level=logging.DEBUG, # Set minimum log level (DEBUG and above)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format of each log message (time, logger name, level, message)

    datefmt='%Y-%m-%d %H:%M:%S', # Format for date and time in logs

    handlers=[
        logging.FileHandler("app1.log"), # Write logs to a file named app1.log
        logging.StreamHandler() # Also print logs to the console
    ],

    force=True  # Reset old handlers so our config works
)

logger = logging.getLogger("ArithmeticApp") # Create a logger with the name "ArithmeticApp"


def add(a, b):
    res = a + b
    logger.debug(f"Adding {a} + {b} = {res}") # Log debug message
    return res

def subtract(a, b):
    res = a - b
    logger.debug(f"Subtracting {a} - {b} = {res}") # Log debug message
    return res

def multiply(a, b):
    res = a * b
    logger.debug(f"Multiplying {a} * {b} = {res}")
    return res

def divide(a, b):
    try:
        res = a / b
        logger.debug(f"Dividing {a} / {b} = {res}")
        return res
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None
    

# Calling functions to generate log outputs
add(2, 3)
subtract(10, 4)
multiply(3, 5)
divide(10, 2)
divide(25, 5)