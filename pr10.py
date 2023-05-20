def remove_spaces_from_dict_keys(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_key = key.replace(" ", "")
        new_dict[new_key] = value
    return new_dict
dictionary = {'first name': 'John', 'last name': 'Doe',
'age': 30}
new_dict =
remove_spaces_from_dict_keys(dictionary)
print(new_dict)