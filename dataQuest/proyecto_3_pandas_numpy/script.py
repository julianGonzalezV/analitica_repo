import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
# our list of lists is stored as data_list
taxi = np.array(converted_taxi_list)

# slicing:
taxi_five = taxi[:5]
taxi_ten = taxi[:10]
print(taxi_ten)

row_0 = taxi[0]
#Select every column for the rows at indexes 391 to 500 inclusive
rows_391_to_500 = taxi[391:501]

#Select the item at row index 21 and column index 5
row_21_column_5 = taxi[21,5] 

# 5. Selecting Columns and Custom Slicing ndarrays

# Select every row for the columns at indexes 1, 4, and 7
columns_1_4_7 = taxi[:, [1,4,7]]

#Select the columns at indexes 5 to 8 inclusive for the row at index 99
row_99_columns_5_to_8 = taxi[99,5:9]

#Select the rows at indexes 100 to 200 inclusive for the column at index 14  
rows_100_to_200_column_14 = taxi[100:201, 14]

# Vector Math::::::::::::::::::::::::.

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

#miles per hour is:
trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
#Tarea
trip_mph = trip_distance_miles / trip_length_hours

#Fin tarea
# Antes 
my_numbers = [
              [6, 5],
              [1, 3],
              [5, 6],
              [1, 4],
              [3, 7],
              [5, 8],
              [3, 5],
              [8, 4]
             ]

sums = []

for row in my_numbers:
    row_sum = row[0] + row[1]
    sums.append(row_sum)
    
#Con numpy
# convert the list of lists to an ndarray
my_numbers = np.array(my_numbers)

# select each of the columns - the result
# of each will be a 1D ndarray
col1 = my_numbers[:,0]
col2 = my_numbers[:,1]

# add the two columns
sums = col1 + col2
#We could simplify this further if we wanted to:
sums2 = my_numbers[:,0] + my_numbers[:,1]
# lo anterior se conoce como vector math!!

#8. Calculating Statistics For 1D ndarrays
mph_min = trip_mph.min()
mph_max = trip_mph.max()

mph_mean = trip_mph.mean()


# operaciones de narrays con umpy: https://docs.scipy.org/doc/numpy-1.14.0/reference/arrays.ndarray.html#calculation


#::::::::9. Calculating Statistics For 2D ndarrays:::::::::::::::::

taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13] 
# select the total_amount column
fare_totals = taxi_first_five[:,13]

# sum the component columns
fare_sums = fare_components.sum(axis=1)

# compare the summed columns to the fare_totals
print(fare_totals.round())
print(fare_sums)

#Using a single method, calculate the mean value for each column of taxi
# Ojo note que 0 se va por cada columna y sobre cada fila de esa columna selecciona el mayor
taxi_column_means = taxi.mean(axis=0)

# 10. Adding Rows and Columns to ndarrays::::
#  numpy.concatenate([l1,l2,...ln], axis = 0/1) : 0 will add rows and 1 will add columns

# These `ones` and `zeros` variables
# are different from the ones in the
# main lesson example

print(ones)
print(zeros)
print() # creates a space in our output

print(ones.shape)
print(zeros.shape)
print()

zeros_2d = np.expand_dims(zeros,axis=1)
print(zeros_2d)
print(zeros_2d.shape)
print()
print('\n')
combined = np.concatenate([ones,zeros_2d],axis=1)
print(combined)
print()

# the `trip_mph` variable is still available from the
# previous screen


#task:

# Expand the dimensions of trip_mph to be a single column in a 2D ndarray
# axis = 1 porque lo que deseamos es agregar una columna, si lo que deseo
# es agregar una fila entonces axis = 0
trip_mph_2d = np.expand_dims(trip_mph ,axis=1)

#Add trip_mph_2d as a new column at the end of taxi:
taxi = np.concatenate([taxi,trip_mph_2d],axis=1)
print(taxi)

# 11. Sorting ndarrays::::::::::::::::::::::
 # Use numpy.argsort() to get the indices which would sort the trip_mph column from the taxi ndarray. The trip_mph column is at column index 15
# Para mayor entendimiento, he creado la variable  last_column para obtener la columna por la cual deseo ordenar, puede ser cualquier index   
last_column = taxi[:,15]
# acá vemos como numpy obtiene los indices que debe ordenar y especifica el orden ej e indice 2 va en la 1ra posiciín el 1 en la ultima
#ojo el indice es MUY DIFERENTE AL VALOR
sorted_order = np.argsort(last_column)
#aplicamos la ordenación de indices a todo al narray de numpy
taxi_sorted = taxi[sorted_order]
print(taxi_sorted)