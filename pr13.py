def count_values_by_key(input_dict, key):
    count = 0
    for k, v in input_dict.items():
        if k == key:
            if type(v) == list:
                count += len(v)
            else:
                count += 1
    return count
dictionary = {'a': 1, 'b': [2, 3, 4], 'c': 5, 'd': [6, 7]}
key = 'd'
count = count_values_by_key(dictionary, key)
print('The key "{}" has {} associated values in the
dictionary.'.format(key, count))