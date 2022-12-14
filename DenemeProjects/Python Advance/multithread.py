#
# Python program to illustrate the concept of threading importing the threading module
import threading


def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	# creating thread
	thrd1 = threading.Thread(target=print_square, args=(10,))
	thrd2 = threading.Thread(target=print_cube, args=(10,))


	# starting thread 1
	thrd1.start()
	# starting thread 2
	thrd2.start()


  # wait until thread 1 is completely executed
	thrd1.join()
	# wait until thread 2 is completely executed
	thrd2.join()

	# both threads completely executed
	print("Done!")


print("- - - - -  - - -")
#

# Python program to illustrate the concept
# of threading
import threading
import os

def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	# starting threads
	t1.start()
	t2.start()

	# wait until all threads finish
	t1.join()
	t2.join()



print("- - - - -  - - -")
#
## Synchronization

import threading

# global variable x
x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task():
	"""
	task for thread
	calls increment function 100000 times.
	"""
	for _ in range(100000):
		increment()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating threads
	t1 = threading.Thread(target=thread_task)
	t2 = threading.Thread(target=thread_task)

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))

print("  - - - - - - - -")
#
## using blocks

import threading

# global variable x
x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task(lock):
	"""
	task for thread
	calls increment function 100000 times.
	"""
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating a lock
	lock = threading.Lock()

	# creating threads
	t1 = threading.Thread(target=thread_task, args=(lock,))
	t2 = threading.Thread(target=thread_task, args=(lock,))

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))


print(" - -  - - - - - ")

#
##