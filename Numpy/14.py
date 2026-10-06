import numpy as np

first = np.array([1, 2]).reshape(1, -1)
second = np.array([[3, 4]])
third = np.array([5, 6, 7]).reshape(1, -1)
print(np.concatenate((first, second, third), axis=1))
