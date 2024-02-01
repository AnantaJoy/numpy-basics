import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])

for i in arr1:
    for j in i:
        print(j)

print("Looping through 3D array")
# iteratig in a 3D array
arr3 = np.array([[[1,2,3],[4,5,6]],[[4,8,6],[8,9,5]]])

for i in arr3:
    for j in i:
        for k in j:
            print(k)
print("Using nditer function")
# using nditer() function
for x in np.nditer(arr3):
    print(x)

# enumerate in 3D array
print("Enumerate the index no in an array")
for index,i in np.ndenumerate(arr3):
    print(index,i)
                