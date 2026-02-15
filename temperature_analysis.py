import numpy as np
import time
#Task 1: Create an Array and Basic Math
print("/*************Task:1***************/")
temp_celsius=np.array([22,25,28,24,26])
F=temp_celsius*1.8+32
Avg_Fah=np.mean(F)
print("Celsius:",temp_celsius)
print("Fahrenheit: ",F)
print(f"Average Fahrenheit: {Avg_Fah:.1f}")
print("/************Task:2***************")

#Task 2: Array Shapes and Statistics

test_scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape:",test_scores.shape)
print("Total Elements:",test_scores.size)
print("Highest Scores:",np.max(test_scores))
print("Lowest Scores:",np.min(test_scores))
range1=np.max(test_scores)-np.min(test_scores)
print("Range:",range1)
print("/************Task:3***************")
#Task 3: Performace Comparison

np_array=np.arange(1,50001)
py_list= list(range(1, 50001))

print("NumPy sum:",np.sum(np_array))
print("Python Sum:", sum(py_list))

start = time.time()
total = sum(py_list)
python_time = time.time() - start

start = time.time()
total = np.sum(np_array)
numpy_time = time.time() - start

print(f"Python Time: {python_time:.4f} seconds")
print(f"NumPy Time: {numpy_time:.4f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster")

