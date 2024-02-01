import numpy as np

arr = np.array([2,4,4,8,1,7,0,5])

# sorting from lowest to highest
print(np.sort(arr))

arr1 = np.array(['dhaka','rajshahi','khulna','rangpur','barishal','sylhet','chittagong','cumilla','mymenshingh'])
# sorting alphabetical order
arr_a = np.sort(arr1)
print(arr_a)

bool_arr = np.array([True,False,False,True])
# sorting boolean value
print(np.sort(bool_arr))

# sort a 3D array
arr3 = np.array([[[3, 2],[3,7]], [[5, 0],[4, 1]]])

print(np.sort(arr3))