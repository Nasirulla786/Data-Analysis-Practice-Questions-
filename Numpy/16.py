import numpy as np

numbers = np.arange(32).reshape(2, 4, 4)
first, second = np.split(numbers, 2, axis=0)
print(first)
print(second)
