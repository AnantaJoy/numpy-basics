from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(loc=1, scale=2, size=(2,3))
print(x)

# visualize the normal distribution
sns.distplot(x,hist=False)
plt.show()