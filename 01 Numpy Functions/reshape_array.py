# 1D array to 2D array
import numpy as np 

arr1 = np.array([1,2,3,4,5,6,7,8])

newarr = arr1.reshape(2,4)
print(newarr)
# print(newarr.ndim())

# you can't reshape into any number
# arr2 = arr1.reshape(5,6)
# print(arr2)

# return result of reshape
print(newarr.reshape(2,4).base)

# multidimensional array to a 1D array
flatarray = newarr.reshape(-1)
print(flatarray)