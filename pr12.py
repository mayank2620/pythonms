def list_to_nested_dict(keys, value):
    if len(keys) == 1:
        return {keys[0]: value}
    else:
        return {keys[0]: list_to_nested_dict(keys[1:],
value)}
def convert_list_to_nested_dict(input_list):
    nested_dict = {}
    for item in input_list:
        keys = item[:-1]
        value = item[-1]
        current_dict = nested_dict
        for key in keys[:-1]:
            current_dict = current_dict.setdefault(key, {})
        current_dict[keys[-1]] = value
    return nested_dict
input_list = [['a', 'b', 'c', 1], ['a', 'b', 'd', 2], ['a', 'e', 'f', 3]]
nested_dict = convert_list_to_nested_dict(input_list)
print(nested_dict)