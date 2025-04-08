#Multithreading is a process or a technique which allows a CPU to execute multiple threads of one process at the same time
# the main purpose of the multithreading is to run multiple tasks and funtions at the sametime...
# it does multiple task at the same time without depend on any other thread...
# Multi-threading occurs Simultaneously...#

import threading

class A: 
    def run(self):
        for i in range(5):
            print("Devanshu Dasgupta.")

class B:
    def run(self):
        for i in range(5):
            print("Suparna Dasgupta.")

# Creating instances
t1 = A()
t2 = B()

# Creating threads
thread1 = threading.Thread(target=t1.run)
thread2 = threading.Thread(target=t2.run)

# Starting threads
thread1.start()
thread2.start()

# Waiting for both threads to complete
thread1.join()
thread2.join()

print("Multithreading Completed.")
