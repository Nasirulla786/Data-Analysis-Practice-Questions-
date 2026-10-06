import numpy as np

parts = np.array_split(np.arange(17), 4)
print([len(part) for part in parts])
