import numpy as np

numbers = np.random.randint(1, 100, 10)
index = np.argmax(numbers)
print(numbers)
print("Maximum:", numbers[index])
print("Index:", index)
