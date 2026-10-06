import numpy as np

numbers = np.arange(1, 37).reshape(6, 6)
print(numbers[0, 0], numbers[0, -1], numbers[-1, 0], numbers[-1, -1])
