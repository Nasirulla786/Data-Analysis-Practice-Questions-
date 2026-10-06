import sys
import numpy as np


np.random.seed(1)

# 1. Multiples of 7 between 7 and 100
array1 = np.arange(7, 101, 7)
print("1.", array1)
print("Length:", len(array1))

# 2. A 4 x 4 array filled with 9
array2 = np.full((4, 4), 9)
print("\n2.\n", array2)

# 3. Convert integer array to float
array3 = np.arange(1, 11)
float_array3 = array3.astype(float)
print("\n3. Before:", array3.dtype)
print("After:", float_array3.dtype)

# 4. Compare memory size of a list and a NumPy array
values = [1, 2, 3, 4, 5]
list_array = values
numpy_array = np.array(values)
print("\n4. List size:", sys.getsizeof(list_array), "bytes")
print("NumPy array size:", sys.getsizeof(numpy_array), "bytes")

# 5. Four corner elements of a 6 x 6 array
array5 = np.arange(1, 37).reshape(6, 6)
corners = array5[np.ix_([0, 0, 5, 5], [0, 5, 0, 5])]
print("\n5. Array:\n", array5)
print("Corners:", array5[0, 0], array5[0, -1], array5[-1, 0], array5[-1, -1])

# 6. Every third element starting from index 1
array6 = np.arange(12)
print("\n6.", array6[1::3])

# 7. Reverse the rows of a 5 x 5 array
array7 = np.arange(1, 26).reshape(5, 5)
print("\n7.\n", array7[::-1])

# 8. Replace values divisible by 3 with -1
array8 = np.arange(1, 13)
array8[array8 % 3 == 0] = -1
print("\n8.", array8)

# 9. Normalize values between 0 and 1
array9 = np.array([10, 20, 30, 40, 50])
normalized = (array9 - array9.min()) / (array9.max() - array9.min())
print("\n9.", normalized)

# 10. Transpose and transpose again
array10 = np.arange(1, 10).reshape(3, 3)
transpose10 = array10.T
print("\n10. Transpose:\n", transpose10)
print("Transpose of transpose is original:", np.array_equal(transpose10.T, array10))

# 11. Maximum value and its index
array11 = np.random.randint(1, 100, 10)
maximum_index = np.argmax(array11)
print("\n11. Array:", array11)
print("Maximum:", array11[maximum_index], "Index:", maximum_index)

# 12. Element-wise remainder
array12_a = np.array([10, 20, 30, 40])
array12_b = np.array([3, 6, 7, 9])
print("\n12.", np.mod(array12_a, array12_b))

# 13. Stack two 2 x 3 arrays into a 3-D array
array13_a = np.array([[1, 2, 3], [4, 5, 6]])
array13_b = np.array([[7, 8, 9], [10, 11, 12]])
stacked13 = np.stack((array13_a, array13_b))
print("\n13. Shape:", stacked13.shape)
print(stacked13)

# 14. Reshape first, then concatenate three arrays
array14_a = np.array([1, 2]).reshape(1, -1)
array14_b = np.array([[3, 4]])
array14_c = np.array([5, 6, 7]).reshape(1, -1)
combined14 = np.concatenate((array14_a, array14_b, array14_c), axis=1)
print("\n14.", combined14)

# 15. Reshape to 4 x 4 and transpose
array15 = np.arange(1, 17).reshape(4, 4)
print("\n15. Column-major equivalent:\n", np.transpose(array15))

# 16. Split a 3-D array into two equal parts along axis 0
array16 = np.arange(32).reshape(2, 4, 4)
parts16 = np.split(array16, 2, axis=0)
print("\n16. Part 1:\n", parts16[0])
print("Part 2:\n", parts16[1])

# 17. Split 17 elements into 4 parts
array17 = np.arange(17)
parts17 = np.array_split(array17, 4)
print("\n17. Part sizes:", [len(part) for part in parts17])

# 18. Remove values beyond 2 standard deviations from the mean
array18 = np.array([10, 11, 12, 13, 12, 11, 100])
mean18 = np.mean(array18)
std18 = np.std(array18)
without_outliers = array18[np.abs(array18 - mean18) <= 2 * std18]
print("\n18. Without outliers:", without_outliers)

# 19. Student averages and subject averages
marks = np.array([
	[80, 75, 90, 85],
	[70, 65, 80, 75],
	[90, 88, 95, 92],
	[60, 70, 65, 68],
	[85, 80, 88, 90]
])
print("\n19. Student averages:", np.mean(marks, axis=1))
print("Subject averages:", np.mean(marks, axis=0))

# 20. Correlation coefficient
array20_a = np.array([1, 2, 3, 4, 5])
array20_b = np.array([2, 4, 6, 8, 10])
print("\n20. Correlation coefficient:\n", np.corrcoef(array20_a, array20_b))

# 21. Save and reload a 5 x 5 array as CSV
array21 = np.random.randint(1, 100, (5, 5))
np.savetxt("array.csv", array21, delimiter=",", fmt="%d")
loaded21 = np.loadtxt("array.csv", delimiter=",", dtype=int)
print("\n21. CSV matches original:", np.array_equal(array21, loaded21))

# 22. Save and load three arrays in one NPZ file
np.savez("arrays.npz", first=np.array([1, 2]), second=np.ones((2, 2)), third=np.arange(6))
loaded22 = np.load("arrays.npz")
print("\n22. Stored array names:", loaded22.files)
loaded22.close()

# 23. Random 3 x 3 matrix and sort each row
array23 = np.random.randint(10, 51, (3, 3))
print("\n23. Sorted rows:\n", np.sort(array23, axis=1))

# 24. Biased coin: 70% heads, 200 flips
coin_flips = np.random.binomial(1, 0.7, 200)
print("\n24. Observed proportion of heads:", np.mean(coin_flips))

# 25. Normal distribution and values outside [-4, 4]
normal_values = np.random.normal(0, 2, 2000)
print("\n25. Outside [-4, 4]:", np.sum((normal_values < -4) | (normal_values > 4)))

# 26. Website visits per minute using Poisson distribution
visits = np.random.poisson(5, 60)
print("\n26. Minute with highest visits:", np.argmax(visits) + 1)
print("Highest visits:", np.max(visits))

# 27. Product choices using the Multinomial distribution
products = np.random.multinomial(200, [0.5, 0.3, 0.2])
print("\n27. Product counts:", products)

# 28. Shuffle a deck and deal five cards
deck = np.arange(1, 53)
np.random.shuffle(deck)
print("\n28. Five-card hand:", deck[:5])
