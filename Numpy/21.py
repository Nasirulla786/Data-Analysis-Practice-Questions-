import numpy as np

original = np.random.randint(1, 100, (5, 5))
np.savetxt("array.csv", original, delimiter=",", fmt="%d")
loaded = np.loadtxt("array.csv", delimiter=",", dtype=int)
print(np.array_equal(original, loaded))
