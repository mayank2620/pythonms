def check_keys_exist(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True
dictionary = {'apple': 2.5, 'banana': 1.5, 'orange': 3, 'mango': 2, 'pear': 1}
keys = ['apple', 'banana', 'pear', 'watermelon']
if check_keys_exist(dictionary, keys):
    print("All keys exist in the dictionary")
else:
    print("One or more keys do not exist in the dictionary")