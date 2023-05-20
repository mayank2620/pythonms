def replace_values_with_sum(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], list):
            dictionary[key] = sum(dictionary[key])
    return dictionary
dictionary = {'apple': [2, 3, 5], 'banana': 1.5, 'orange': [3, 4], 'mango': [2, 7], 'pear': 1}
new_dictionary = replace_values_with_sum(dictionary)
print(new_dictionary)

