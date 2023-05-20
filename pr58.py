import itertools

def letter_combinations(dictionary):
    # Get the values of each key as a list
    value_lists = dictionary.values()
    # Create all combinations of values
    combinations = itertools.product(*value_lists)
    # Join each combination into a string and return as a list
    return [''.join(combination) for combination in combinations]
dictionary = {'A': ['a', 'b'], 'B': ['c', 'd'], 'C': ['e', 'f']}
combinations = letter_combinations(dictionary)
print(combinations)