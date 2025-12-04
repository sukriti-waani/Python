'''
Real-World Example : Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations can be CPU-intensive, especially for large numbers. Using multiprocessing can help speed up these calculations by distributing the workload across multiple CPU cores.
'''

import multiprocessing
import math
import time
import sys

sys.set_int_max_str_digits(1000000)  # Increase limit for large factorials

# function to compute factorials of a given number
def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers = [50000, 60000, 70000, 80000]  # List of large numbers to compute factorials for

    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken : {end_time - start_time} seconds.")