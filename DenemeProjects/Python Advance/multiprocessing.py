'''
# importing the multiprocessing module
import multiprocessing

def print_cube(num):
	"""
	function to print cube of given num
	"""
	print("Cube: {}".format(num * num * num))

def print_square(num):
	"""
	function to print square of given num
	"""
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	# creating processes
	p1 = multiprocessing.Process(target=print_square, args=(10, ))
	p2 = multiprocessing.Process(target=print_cube, args=(10, ))

	# starting process 1
	p1.start()
	# starting process 2
	p2.start()

	# wait until process 1 is finished
	p1.join()
	# wait until process 2 is finished
	p2.join()

	# both processes finished
	print("Done!")


print(" - - - - - - - ")
#
# importing the multiprocessing module
import multiprocessing
import os

def worker1():
	# printing process id
	print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
	# printing process id
	print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
	# printing main program process id
	print("ID of main process: {}".format(os.getpid()))

	# creating processes
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)

	# starting processes
	p1.start()
	p2.start()

	# process IDs
	print("ID of process p1: {}".format(p1.pid))
	print("ID of process p2: {}".format(p2.pid))

	# wait until processes are finished
	p1.join()
	p2.join()

	# both processes finished
	print("Both processes finished execution!")

	# check if processes are alive
	print("Process p1 is alive: {}".format(p1.is_alive()))
	print("Process p2 is alive: {}".format(p2.is_alive()))

'''

print(" - - - - - - - ")
#
import multiprocessing

# empty list with global scope
result = []

def square_list(mylist):
	"""
	function to square a given list
	"""
	global result
	# append squares of mylist to global list result
	for num in mylist:
		result.append(num * num)
	# print global list result
	print("Result(in process p1): {}".format(result))

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating new process
	p1 = multiprocessing.Process(target=square_list, args=(mylist,))
	# starting process
	p1.start()
	# wait until process is finished
	p1.join()

	# print global result list
	print("Result(in main program): {}".format(result))


print(" - - - - - - - ")
# sharing data

import multiprocessing

def square_list(mylist, result, square_sum):
	"""
	function to square a given list
	"""
	# append squares of mylist to result array
	for idx, num in enumerate(mylist):
		result[idx] = num * num

	# square_sum value
	square_sum.value = sum(result)

	# print result Array
	print("Result(in process p1): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in process p1): {}".format(square_sum.value))

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating Array of int data type with space for 4 integers
	result = multiprocessing.Array('i', 4)

	# creating Value of int data type
	square_sum = multiprocessing.Value('i')

	# creating new process
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

	# starting process
	p1.start()

	# wait until the process is finished
	p1.join()

	# print result array
	print("Result(in main program): {}".format(result[:]))

	# print square_sum Value
	print("Sum of squares(in main program): {}".format(square_sum.value))


print(" - - - - - - - ")
# server process

import multiprocessing

def print_records(records):
	"""
	function to print record(tuples) in records(list)
	"""
	for record in records:
		print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
	"""
	function to add a new record to records(list)
	"""
	records.append(record)
	print("New record added!\n")

if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# creating a list in server process memory
		records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)])
		# new record to be inserted in records
		new_record = ('Jeff', 8)

		# creating new processes
		p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
		p2 = multiprocessing.Process(target=print_records, args=(records,))

		# running process p1 to insert new record
		p1.start()
		p1.join()

		# running process p2 to print records
		p2.start()
		p2.join()

print(" - - - - - - - -")

# communication between process
## - queue

import multiprocessing

def square_list(mylist, q):
	"""
	function to square a given list
	"""
	# append squares of mylist to queue
	for num in mylist:
		q.put(num * num)

def print_queue(q):
	"""
	function to print queue elements
	"""
	print("Queue elements:")
	while not q.empty():
		print(q.get())
	print("Queue is now empty!")

if __name__ == "__main__":
	# input list
	mylist = [1,2,3,4]

	# creating multiprocessing Queue
	q = multiprocessing.Queue()

	# creating new processes
	p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
	p2 = multiprocessing.Process(target=print_queue, args=(q,))

	# running process p1 to square list
	p1.start()
	p1.join()

	# running process p2 to get queue elements
	p2.start()
	p2.join()

print(" - - - - -  - -")

##  pipes -
import multiprocessing

def sender(conn, msgs):
	"""
	function to send messages to other end of pipe
	"""
	for msg in msgs:
		conn.send(msg)
		print("Sent the message: {}".format(msg))
	conn.close()

def receiver(conn):
	"""
	function to print the messages received from other
	end of pipe
	"""
	while 1:
		msg = conn.recv()
		if msg == "END":
			break
		print("Received the message: {}".format(msg))

if __name__ == "__main__":
	# messages to be sent
	msgs = ["hello", "hey", "hru?", "END"]

	# creating a pipe
	parent_conn, child_conn = multiprocessing.Pipe()

	# creating new processes
	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

	# running processes
	p1.start()
	p2.start()

	# wait until processes finish
	p1.join()
	p2.join()

