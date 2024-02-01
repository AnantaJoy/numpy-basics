# filter actually create a new array based on certain conditions
import numpy as np


arr = np.array([0,1,2,3,4,5,6,7,8,9,10])

# write a program to filter odd number from an array
filter_arr = []

for num in arr:
    if num%2!=0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

odd_arr = arr[filter_arr]
print(odd_arr)

# filter directly from an array
filter_arr = arr%2 == 0
evenarr = arr[filter_arr]

print(evenarr)