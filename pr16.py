def combine_values(list_of_dicts):
    combined_dict = {}
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if key in combined_dict:
                combined_dict[key].append(value)
            else:
                combined_dict[key] = [value]
    return combined_dict
list_of_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'b': 5, 'c': 6}]
combined_dict = combine_values(list_of_dicts)
print(combined_dict)