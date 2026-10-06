import numpy as np

numbers = np.random.normal(0, 2, 2000)
outside = np.sum((numbers < -4) | (numbers > 4))
print("Outside [-4, 4]:", outside)
