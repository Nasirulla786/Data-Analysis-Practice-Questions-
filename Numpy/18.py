import numpy as np

numbers = np.array([10, 11, 12, 13, 12, 11, 100])
mean = np.mean(numbers)
standard_deviation = np.std(numbers)
result = numbers[np.abs(numbers - mean) <= 2 * standard_deviation]
print(result)
