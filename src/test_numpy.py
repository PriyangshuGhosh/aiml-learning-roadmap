import numpy as np

my_list = [1,2,3,4]

#for multiplying a normal list i cannot use List * 2 it duplicates it 
# but numpy makes it possible and also is faster

array = np.array([1,2,3,4])
array *= 2
print(array) 
print(type(array))

#creating and printing multi dimensional array 

a=np.array([[1,2,3,4],[5,6,7,8],[12,34,56,67]])
d = np.array([[[1, 2, 3],[4, 5, 6]],
             [[1, 2, 3], [4, 5, 6]]])

print(array.ndim)
print(a.ndim)
print(d.ndim)


#array indexing 
print(d[1,1][1:])

#slicing is also similar


""" 
Data Types in NumPy

NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
 
    
"""
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#Create an array with data type 4 bytes integer:

arr2 = np.array([1,2,3,4],dtype='i2')
print(arr2.dtype)

#Change data type from float to integer by using 'i' as parameter value:

L=np.array([1.1,2,3,4,5])
L1=np.array(L,dtype= int)
L2=L1.astype('S')
print(L1)
print(L2)


#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape) 

#Reshape From 1-D to 3-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr) 

print("***************")
"""Unknown Dimension

You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you."""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])

newarr = arr.reshape(2,2, -1)
print(newarr) 

"""Flattening the arrays

Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this."""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr) 