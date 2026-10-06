import numpy as np

first = np.array([[1, 2, 3], [4, 5, 6]])
second = np.array([[7, 8, 9], [10, 11, 12]])
result = np.stack((first, second))
print(result)
print("Shape:", result.shape)
