import numpy as np

# truncation and fix
arr = np.trunc([3.1416,2.736,4685])
print(arr)
arr = np.fix([3.23,3.2322,3.24234])
print(arr)

# rounding
print(np.round(2.5301,2))
print(np.round(2.534,2))
print(np.round(2.535,2))
print(np.round(2.536,2))
print(np.round(2.539,2))

# floor()
# ceil()
# log()
# log2()
# log10()
# sum()
# cumsum()
# prod()
# cumprod()
# diff()
# Finding LCM (Lowest Common Multiple)
num1 = 20
num2 = 16
x = np.lcm(num1,num2)
print(x)

# GCD Greatest Common Denominator
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

# trigonometric function 
# cos(), sin(), tan()

x = np.sin(np.pi/2)
print(x)
# radian to degree deg2rad()
# degree to radian rad2deg()
# finding angles
# arcsin(), arccos(), arctan()

# hypotenuse 
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

# Hyperbolic Functions
# sinh(), cosh(), tanh()
x = np.sinh(np.pi/2)
print(x) 

# sets in python
# unique()

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
# union1d()
# intersection1d()
# setdiff1d()