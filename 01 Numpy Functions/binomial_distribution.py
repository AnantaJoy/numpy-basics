"""
Difference Between Normal and Binomial Distribution
The main difference is that normal distribution is continuos whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# toss a coin
x = random.binomial(n=10, p=.5, size=1000)
print(x)

# visualize a binomial distribution
sns.distplot(x,hist=True, kde=False)
plt.show()

# random vs normal distribution 

sns.distplot(random.normal(loc=50, scale=5, size=10000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=10000), hist=False, label='binomial')

plt.show()