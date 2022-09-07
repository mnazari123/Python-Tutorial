# thread  = a flow of exacution. Like a separator  order of instructions. 
#           however, each thread takes a turn running to achieve concurrency 
#           GIL = (global interpreter lock),
#           allow only one thread to hold the control of the python interpreter at any one time

# CPU bound = program/task spends most of it's tiem waiting for internal events (CPU intensive)
#               use multiprocessing
# IO bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#               use multithreading


from ast import arg
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("You dink coffee")
def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#drink_coffee()
#study()
print(threading.active_count()) # print the current thread running.
print(threading.enumerate())
print(time.perf_counter())
