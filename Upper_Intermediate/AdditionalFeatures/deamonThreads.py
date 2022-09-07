# deamon Thread = a thread that runs in the background, not important for program to run
#                   your program not waits fro daemon threads to complete before exiting
#                   non daemon thead cannot normally be killed, stay alive until task is complete
#                   ex. background tast, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count+=1
        print("loggin in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do yo wish to exit?")