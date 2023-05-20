def unique_values(dictionary):
    unique_values = set()
    for value in dictionary.values():
        if value not in unique_values:
            unique_values.add(value)
    return unique_values
dictionary = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}
unique_values = unique_values(dictionary)
print(unique_values)