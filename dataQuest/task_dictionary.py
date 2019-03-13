opened_file = open('AppleStore.csv')
from csv import reader
import math
read_file = reader(opened_file)
apps_data = list(read_file)
rating_count_tot  = []

for data in apps_data[1:]:
    rating_count_tot .append(float(data[5]))

min_rating = min(rating_count_tot)
max_rating = max(rating_count_tot)
interval_base_value = (max_rating-min_rating)/10
print(math.ceil(0.2))
frecuency_dic = {}

for record in rating_count_tot:
    dic_key = math.ceil(record/interval_base_value)
    real_key = math.ceil(dic_key * interval_base_value)
    #if dic_key == 0:
        #print("key => "+ str(dic_key)+" ; record => "+ str(record))
    if real_key in frecuency_dic:
        frecuency_dic[real_key] += 1
    else:
        frecuency_dic[real_key] = 1

    

