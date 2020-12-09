import numpy as np
from numpy import random

# generate a random number
# integer
x = random.randint(100) 
print(x)
# float
x = random.rand(2)
print(x)

# random 1D array
x = random.randint(10,size=(6))
print(x)
# random 2D array
x = random.randint(50,size=(2,4))
print(x)

# you can do same operation in random float using random.rand
# generate random number from a given array
# using choice()
x = random.choice([4,8,6,0,5,6,'Joy'])
print(x)

# choice from a 2D array
x = random.choice([3,5,3,8,6,5],size=(4,5))
print(x)

# randon data distribution
x = random.choice([1,3,5,7],p=[0.1,0.4,0.5,0],size=[4,6])
print(x)

arr = np.array([2,8,6,9,4,6,0,2,7,1])
# shuffling an array
# unchanged original array value
# random.permutation(arr)
# print(arr)
print(random.permutation(arr))

# changed original array value
random.shuffle(arr)
print(arr)

