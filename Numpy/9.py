import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
normalized = (numbers - numbers.min()) / (numbers.max() - numbers.min())
print(normalized)
