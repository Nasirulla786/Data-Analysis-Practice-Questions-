import numpy as np

marks = np.array([[80, 75, 90, 85], [70, 65, 80, 75], [90, 88, 95, 92], [60, 70, 65, 68], [85, 80, 88, 90]])
print("Student averages:", np.mean(marks, axis=1))
print("Subject averages:", np.mean(marks, axis=0))
