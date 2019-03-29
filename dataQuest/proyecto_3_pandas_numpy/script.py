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

