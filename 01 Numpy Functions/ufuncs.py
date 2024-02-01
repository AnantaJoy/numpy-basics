import numpy as np

x = [8,4,1]
y = [2,4,8]

# sum
z = np.add(x,y)
print(z)
# check the function is ufunc or not
print(type(np.add))

# create your own ufunc
def mySub(x,y):
    return x-y

mySub = np.frompyfunc(mySub,2,1)
print(mySub([9,8,7,6],[4,3,2,1]))
print(type(mySub))

# subtract()
# multiply()
# divide() 
# power()
# mod()
# remainder()
# divmod()
# absolute()