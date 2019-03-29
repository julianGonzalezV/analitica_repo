# solo es rquerido numpy import ya no el csv como antes lo haciamos 
import numpy as np

# 1. Reading CSV files with NumPy
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',',skip_header=1)
#use the ndarray.dtype attribute to see the internal datatype that has been use
print(taxi.dtype)
print(taxi)

# 2. Boolean Arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

# Evaluate whether the elements in array -a- are less than 3 
a_bool = np.array(a<3)
print(a_bool)

# Evaluate whether the elements in array b are equal to "blue"
b_bool = np.array(b== "blue")
print(b_bool)

# Evaluate whether the elements in array c are greater than 100
c_bool = np.array(c>100)
print(c_bool)