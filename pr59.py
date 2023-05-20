def highest_three(dictionary):
    # Get a list of all values in the dictionary
    values = list(dictionary.values())
    # Sort the list of values in descending order
    values.sort(reverse=True)
    # Return the first three values
    return values[:3]
dictionary = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}
highest_three_values = highest_three(dictionary)
print(highest_three_values)