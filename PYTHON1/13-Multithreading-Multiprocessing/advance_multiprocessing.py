# Multiprocessing with Thread Pool Executor

'''
# Multiprocessing using ProcessPoolExecutor
# - Runs tasks in SEPARATE PROCESSES (true parallel execution)
# - Best for CPU-bound tasks (heavy calculations)
# - Bypasses the GIL, uses multiple CPU cores
# - Processes are heavier but give more speed for computation-heavy work
'''

# Import ThreadPoolExecutor for multithreading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Import time module for adding delay
import time

def square_num(num):
  time.sleep(1)  # Simulates a 1-second time-consuming task
  return f"Square: {num * num}"  # Returns the square of the number

nums = [1, 2, 3, 4, 5]

if __name__ == "__main__":
  with ProcessPoolExecutor(max_workers=3) as executor:
      
      # executor.map() sends the list items to the function in parallel
      # It returns the results in the SAME ORDER as the input list
      results = executor.map(square_num, nums)

  # Loop through the results returned by executor.map()
  for result in results:
      print(result)