import numpy as np

arr = np.array([1,2,3,4,3,5,6,3])

x = np.where(arr == 3)
print(x)

# find where value is odd or even 
odd = np.where(arr%2!=0) 
print(odd)
even = np.where(arr%2==0)
print(even)

# search sorted in numpy array
search_val = np.searchsorted(arr,5555)
print(search_val) 