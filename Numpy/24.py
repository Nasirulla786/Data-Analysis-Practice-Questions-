import numpy as np

flips = np.random.binomial(1, 0.7, 200)
print("Heads proportion:", np.mean(flips))
