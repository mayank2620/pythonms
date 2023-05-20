def print_dict_as_table(input_dict):
    # Get the length of the longest key in the dictionary
    max_key_length = max(len(str(key)) for key in
input_dict.keys())
    # Get the length of the longest value in the
dictionary
    max_value_length = max(len(str(value)) for value in
input_dict.values())
    # Print the table header
    print('| {:{}} | {:{}} |'.format('Key', max_key_length,
'Value', max_value_length))
    print('-' * (max_key_length + 3) + '|' + '-' *
(max_value_length + 3))
    # Print the table rows
    for key, value in input_dict.items():
        print('| {:{}} | {:{}} |'.format(key,
max_key_length, value, max_value_length))
dictionary = {'apple': 2, 'banana': 5, 'cherry': 7}
print_dict_as_table(dictionary)