def print_dict_line_by_line(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3,
'mango': 2, 'pear': 1}
print_dict_line_by_line(dictionary)