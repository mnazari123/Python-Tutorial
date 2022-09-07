# Python Multiprocessing: 
# Multiprocessing : running task in parallel on different cpu cores, bypasses GIL used for thread
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count+= 1

def main():
    a = Process(target=counter, args=(5000000000,))
    b = Process(target=counter, args=(5000000000,))
    
    b.start()
    a.start()

    a.join()
    b.joing()
    
    print("finished in ", time.perf_counter(), "seconds")