def get_key_value_items(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
        print(f"Item: {key}, {value}\n")
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3,
'mango': 2, 'pear': 1}
get_key_value_items(dictionary)