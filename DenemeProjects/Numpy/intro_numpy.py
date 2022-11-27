#


# Python program to demonstrate
# basic array characteristics
import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],[ 4, 7, 5], [4,5,6]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

print(" - - - - - -")
#
# # Array creation

# Python program to demonstrate
# array creation techniques
import numpy as np

# Creating array from list with type float
a = np.array([[3, 4, 5], [5, 6, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array((1 , 8, 9))
print ("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((4, 5))
print ("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
			"Array type is complex:\n", d)

# Create an array with random values
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
										"0 and 5:\n", g)

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[9, 8, 3, 14],
				[5, 2, 4, 22],
				[1, 2, 0, 31]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


print(" - - - - -- -  -")

#
## Array indexing
# Python program to demonstrate
# indexing in numpy
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
				[4, -0.5, 6, 0],
				[2.6, 0, 7, 8],
				[3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print ("Array with first 2 rows and alternate"
					"columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
									"(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)


print(" - - - - -- -  -")

#
## Basic operations
## operations on single array -
# Python program to demonstrate basic operations on single array
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print ("Adding 1 to every element:", a+1)

# add 2 to every element
print ("Adding 2 to every element:", a+2)
# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)

# subtract 2 from each element
print ("Subtracting 2 from each element:", a-2)

# multiply each element by 10
print ("Multiplying each element by 10:", a*10)

# multiply each element by 5
print ("Multiplying each element by 5:", a*5)
# square each element
print ("Squaring each element:", a**2)

# modify existing array
a *= 2
print ("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)



print(" - - - - -- -  -")

#
## Unary operators
###
# Python program to demonstrate unary operators in numpy
import numpy as np

arr = np.array([[1, 5, 16],
				[4, 7, 25],
				[3, 1, 9]])

# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
					arr.max(axis = 1))

# minimum element of array
print ("Column-wise minimum elements:",
						arr.min(axis = 0))

# sum of array elements
print ("Sum of all array elements:",
							arr.sum())

# cumulative sum along each row
print ("Cumulative sum along each row:\n",
						arr.cumsum(axis = 1))


print(" - - - - -- -  -")

# Binary operators

# Python program to demonstrate
# binary operators in Numpy
import numpy as np

a = np.array([[1, 2],
			[3, 4]])
b = np.array([[4, 3],
			[2, 1]])

# add arrays
print ("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)

# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))



print(" - - - - -- -  -")

# universal functions (ufunc)

# Python program to demonstrate
# universal functions in numpy
import numpy as np

# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.sqrt(a))

print(" - - - - -- -  -")

# sorting array _

# Python program to demonstrate sorting in numpy
import numpy as np

a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

# sorted array
print("Array elements in sorted order:\n",
      np.sort(a, axis=None))

# sort array row-wise
print("Row-wise sorted array:\n",
      np.sort(a, axis=1))

# specify sort algorithm
print("Column wise sort by applying merge-sort:\n",
      np.sort(a, axis=0, kind='mergesort'))

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n",
      np.sort(arr, order=['grad_year', 'cgpa']))

print(" - - - - -- -  -")

#