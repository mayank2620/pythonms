def sort_dict_list(dictionary, key):
    dictionary[key] = sorted(dictionary[key])
    return dictionary
dictionary = {'a': ['apple', 'ant', 'artichoke'], 'b':
['banana', 'butter', 'bread']}
key = 'a'
sorted_dict = sort_dict_list(dictionary, key)
print(sorted_dict)