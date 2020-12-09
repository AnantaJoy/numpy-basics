import numpy as np

# 1D array spliting
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)
newarr2 = np.array_split(arr,4)
print(newarr2)
# access new split array
print(newarr2[2])

# 2D array spliting
# example from w3school.com
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

# vsplit
# dsplit