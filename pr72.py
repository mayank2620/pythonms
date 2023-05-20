def count_items_in_list_values(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            count += len(value)
    return count
dictionary = {'apple': [2, 3, 5], 'banana': 1.5, 'orange': [3, 4], 'mango': [2, 7], 'pear': 1}
count = count_items_in_list_values(dictionary)
print(f"The dictionary contains {count} items in list values.")