# create a 0D array
import numpy as np
arr0 = np.array(45)
print(arr0)

# create a 1D array
arr1 = np.array([1,2,3,4])
print(arr1)

# create a 2D array
arr2 = np.array([1,2,3],[3,4,5])
print(arr2)

# create a 3D array
arr3 = np.array([[[1,2,3],[3,4,5]],[[2,3,1],[2,7,5]]])
print(arr3)

# check the dimension of the array
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)