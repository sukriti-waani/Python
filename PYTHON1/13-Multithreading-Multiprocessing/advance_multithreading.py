# Multithreading with Thread Pool Executor
'''
# Multithreading using ThreadPoolExecutor
# - Runs tasks in MULTIPLE THREADS (concurrent execution)
# - Best for I/O-bound tasks (waiting tasks like sleep, API calls, file read)
# - Threads share memory and are lightweight
# - Limited by GIL → not ideal for heavy CPU maths
'''


# Import ThreadPoolExecutor for multithreading
from concurrent.futures import ThreadPoolExecutor

# Import time module for adding delay
import time

# Function that will run in different threads
def print_number(number):
    time.sleep(1)            # Simulates a 1-second time-consuming task
    return f"Number: {number}"   # Returns a string after finishing

# A list of numbers to process
numbers = [1, 2, 3, 4, 5]

# Creating a thread pool with 3 worker threads
# "with" ensures threads are cleaned up automatically after work is done
with ThreadPoolExecutor(max_workers=3) as executor:
    
    # executor.map() sends the list items to the function in parallel
    # It returns the results in the SAME ORDER as the input list
    results = executor.map(print_number, numbers)

# Loop through the results returned by executor.map()
for result in results:
    print(result)
