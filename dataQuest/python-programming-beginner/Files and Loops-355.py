## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(data)

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for rw in ten_rows:
 print(rw)

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows[0:5])
final_data = []
for rw in rows:
    splited_rw = rw.split(",")
    final_data.append(splited_rw)
    
print(final_data)

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = []
for elem in range(0, len(five_elements)):
    cities_list.append(five_elements [elem] [0])
    
print(cities_list)

## 9. Looping Through a List of Lists ##

crime_rates = []
cities_list = []
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
for row in final_data:
    citie =  row[0]
    cities_list.append(citie)




## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []

for rw in rows:
    in_crime_rate = int(rw.split(",")[1])
    int_crime_rates.append(in_crime_rate)
    
print(int_crime_rates)