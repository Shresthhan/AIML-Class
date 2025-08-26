# Basic knowledge of Numpy

import numpy as np

# 3D Array
'''
arr_3d = np.array([[[2, 3, 5] , [6, 7, 8]], [[3, 4, 7] , [4, 7, 8]]])
print(arr_3d)
'''

# Creating an Array of Zeros 
'''
arr = np.zeros([4,4])
print(arr)
'''
# Creating an Array of Ones
'''
arr = np.ones([3,3])
print(arr)
'''
# Identity Matrix of size 5 
'''
arr = np.eye(5)
print(arr)
'''

# We have to create an array of first 50 numbers starting from 1
'''
arr = np.arange(1,51,2)  # NOTE: arange -> array range
print(arr)
'''

# Task : print 0 to 100 even numbers 
'''
arr = np.arange(0,101,2)
print(arr)
'''

# Task 2: we need an array having 5 values from 1 to 10 evenly spaced 
'''
arr = np.linspace(1, 10, 6) 
print(arr)
'''

# Random Array 
'''
arr = np.random.rand(4, 4) # -> this creates a 4x4 matrix with all values ranging from 0 to 1 
print(arr)

random_arr = np.random.randint(1, 11, size= (3,3))  # -> It creates a random integer matrix
print(random_arr)
'''
'''
arr = np.array([[10, 20, 30], [40, 50, 60]] )  # NOTE: , dtype = 'int8'  -> This changes the size of int datatype
print(arr)

print(arr.shape) # -> prints the number of rows and columns 
print(arr.size) # -> prints the number of elements in matrix
print(arr.ndim) # -> prints the dimension of the matrix
print(arr.dtype) # -> prints the data type of the matrix
print(arr.itemsize) # -> prints the storage occupied by each element in bytes
print(arr.nbytes) # -> prints the total storage occupied by all elements in bytes 
'''
# 1D Array slicing and Indexing
'''
arr = np.arrSy([10, 20, 30, 40, 50, 60] ) 
print(arr[-1])
print(arr[::2])
'''
# 2D Array Slicing and Indexing

arr1 = np.array([[10, 20, 30], [40, 50, 60] , [70, 80, 90]] )
print(arr1[(0,1),(1,1)])
print(arr1[0:2,1])
print(arr1[2,1])
print(arr1[1,1:])




