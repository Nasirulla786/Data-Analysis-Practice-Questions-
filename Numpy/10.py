import numpy as np

numbers = np.arange(1, 10).reshape(3, 3)
transposed = numbers.T
print(transposed)
print(np.array_equal(transposed.T, numbers))
