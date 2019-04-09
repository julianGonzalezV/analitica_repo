# NumPy
 NumPy is the fundamental package for scientific computing with Python. It contains among other things:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

NumPy’s main object is the homogeneous multidimensional array
In NumPy dimensions are called axes.

multidimensional or N-dimensional refers to the fact of having severals dimension : see dimensions.png in this 
folder

Restrictions:
Unlike with Python lists, every value in an ndarray must be of the same types:
Por eso en el ejemplo convertimos todo a float

functions:
ndarray.shape --> it retunrs a tuple(inmutable lists in python) where the first value is the the amount of records in the 
first dimmension or ROWS IN THE DATA SET axe and 
the second refers to the number of columns ON THE DATA SET or the number of items long in the second dimension

ndarray[row,column]: row = cantidad de registros que dese, column=cantidad de columnas que deseo seleccionar
 - Si tuvieramos un list of list normalito entonces sería list[row][column]

Both row and column can be one of the following:

- An integer, indicating a specific location, eg ndarray[3,0].
- A slice, indicating a range of locations, eg ndarray[0:5,6:].
- A colon, indicating every location, eg ndarray[:,2].
- A list of values, indicating specific locations, eg ndarray[[0,1,3,4],0].
- A boolean array, indicating specific locations - we'll look at this method in detail in the second mission of this course.
Or any combination of the above.

Ventajas:

- Las operaciones y funciones contra matrices son muy ganadoras en cuanto a sintactic sugar.
- Las operaciones YA VIENEN OPTIMIZADAS!!! NO REINVENTE LA RUEDA SEÑOR!!


:::::::::::::::::::::::Vector Math:::::::::::::::
No son mas que operaciones entre vectores como sura, resta, mult, div, refuerce con el siguiente link
https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.math.html#arithmetic-operations

Eje: sums2 = my_numbers[:,0] + my_numbers[:,1]
Operaciones 
vector_a + vector_b - Addition
vector_a - vector_b - Subtraction
vector_a * vector_b - Multiplication (this is unrelated to the vector multiplication used in linear algebra).
vector_a / vector_b - Division
vector_a % vector_b - Modulus (find the remainder when vector_a is divided by vector_b)
vector_a ** vector_b - Exponent (raise vector_a to the power of vector_b)
vector_a // vector_b - Floor Division (divide vector_a by vector_b, rounding down to the nearest integer)





:::::::::::::::::::::::::::::::::::::::::::::::::::PANDAS:::::::::::::::::::::::::::::::::::::::::::::::::::


Problema de numpy:
The lack of support for column names forces us to frame the questions we want to answer as multi-dimensional array operations.
Support for only one data type per ndarray makes it more difficult to work with data that contains both numeric and string data.
There are lots of low level methods, however there are many common analysis patterns that don't have pre-built methods.


The pandas library provides solutions to all of these pain an more :) :) :)...........
The underlying code for pandas uses the NumPy library extensively



