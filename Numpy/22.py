import numpy as np

np.savez("arrays.npz", first=np.array([1, 2]), second=np.ones((2, 2)), third=np.arange(6))
data = np.load("arrays.npz")
print(data.files)
data.close()
