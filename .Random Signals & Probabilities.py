
import numpy as np
import matplotlib.pyplot as plt

#1.Random Signals & Probabilities
##1.1 Create Random Sequences
# length N = 10000 with equally distributed values
length_N = 10000

### Generate two independant random sequences
Sequence_a = 2 * np.random.random(length_N) - 1
Sequence_b = 2 * np.random.random(length_N) - 1


print(Sequence_a)
print(Sequence_b)


##1.2 Plot and Discuss the Distributions]
### Plot PMF with 100 bins of both Sequence_a
plt.hist(Sequence_a, bins=100, density=True, alpha=0.8, color='grey', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('PMF')
plt.title('Probability Mass Function of Sequence_a')
plt.show()

### Plot PMF with 100 bins of both Sequence_b
plt.hist(Sequence_b, bins=100, density=True, alpha=0.8, color='grey', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('PMF')
plt.title('Probability Mass Function of Sequence_b')
plt.show()

##1.3 Multiply The Sequences
Sequence_y=Sequence_a + Sequence_b

##1.4 Plot and the Distribution
plt.hist(Sequence_y, bins=100, density=True, alpha=0.8, color='grey', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('PMF')
plt.title('Probability Mass Function of Sequence_y')
plt.show()
