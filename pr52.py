#first assign a dictionary u can take by user
d1 = {1:2,2:4,3:6}#all items are in integers
#first we take sum of keys
sum_keys = 0
for i in d1:
  sum_keys += i
#then we take sum of values
sum_values = 0
for i in d1:
  sum_values += d1[i]
#for taking sum of all items we add keys and values
sum_items = sum_keys + sum_values
print(sum_items)