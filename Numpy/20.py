import numpy as np

first = np.array([1, 2, 3, 4, 5])
second = np.array([2, 4, 6, 8, 10])
print(np.corrcoef(first, second))
