def combine_dicts(dict1, dict2):
    result_dict = dict(dict1)
    for key, value in dict2.items():
        if key in result_dict:
            result_dict[key] += value
        else:
            result_dict[key] = value
    return result_dict
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 50, 'd': 400}
combined_dict = combine_dicts(dict1, dict2)
print(combined_dict)