import numpy as np

visits = np.random.poisson(5, 60)
minute = np.argmax(visits) + 1
print("Minute:", minute)
print("Visits:", visits[minute - 1])
