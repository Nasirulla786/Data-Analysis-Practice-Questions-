import numpy as np

numbers = np.arange(1, 13)
numbers[numbers % 3 == 0] = -1
print(numbers)
