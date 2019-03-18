test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(str_input):
    if '-' in str_input:
        (date1,date2) = str_input.split('-')        
        return round((int(date1)+int(date2))/2)
    else:
        return int(str_input)

#Acá lo que hacemos es probar con un set de datos pequeñopara probar :)
processed_test_data = []

for data in stripped_test_data:
    dateVal = process_date(data)
    processed_test_data.append(dateVal)
    
# Después de ver que si funciona entonces procedemos al procesamiento real
# la candela :)

for data in moma:
    dateVal = data[6]
    stripped_val = strip_characters(dateVal)
    dateV_int = process_date(stripped_val)
    data[6] = dateV_int