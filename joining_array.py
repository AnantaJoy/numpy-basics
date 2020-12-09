import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))
print(arr)

# 2D array
arr3 = np.array([[1,2,4],[4,2,6]])
arr4 = np.array([[1,4,2],[7,8,6]])

new_arr = np.concatenate((arr3,arr4),axis=1)
print(new_arr)

new_arr2 = np.stack((arr3,arr4), axis=1)
print(new_arr2)

# row stacking hstack()
# column stacking vstack()
# depth stack dstack()

