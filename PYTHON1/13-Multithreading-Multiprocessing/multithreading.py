'''
### Multithreading
Multithreading means running multiple threads inside a single process at the same time (concurrently).
Each thread performs a different part of the task.

Example:
A browser uses multiple threads to:
load images, run JavaScript, play video, handle user input


##### Use multithreading when:
The program spends time waiting
(example: waiting for network, file read/write, database).

We want to perform multiple tasks simultaneously
(example: download multiple files at once).

Do NOT use multithreading for CPU-heavy work
(example: large calculations, ML model training).
Use multiprocessing instead.


##### I/O-Based Tasks (Input/Output Tasks)
Tasks where the program waits for external resources, such as:
Reading/writing files
Sending/receiving network requests
Accessing databases
Waiting for user input
These tasks are slow because they depend on external devices, not CPU.
This is where multithreading works best.


##### Concurrent Execution
Concurrent execution means tasks appear to run at the same time, even if the CPU switches between them very fast.


In multithreading:
Threads take turns using the CPU
They overlap in time
Gives the effect of multiple tasks running together

Example:
Downloading 3 files at the same time → system switches between threads rapidly → looks simultaneous.
'''


import threading
import time

def print_numbers():
  for i in range(5):
    time.sleep(2)
    print(f"Number: {i}")

def print_letter():
  for letter in "abcde":
    time.sleep(2)
    print(f"Letter : {letter}")


# Create 2 threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letter)

t = time.time()

# start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")