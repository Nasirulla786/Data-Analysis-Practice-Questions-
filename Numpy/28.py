import numpy as np

deck = np.arange(1, 53)
np.random.shuffle(deck)
print("Five-card hand:", deck[:5])
