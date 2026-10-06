import sys
import numpy as np

values = [1, 2, 3, 4, 5]
array = np.array(values)
print("List size:", sys.getsizeof(values))
print("NumPy array size:", sys.getsizeof(array))
