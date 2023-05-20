def create_dict_from_string(string):
    # Split the string into a list of words
    words = string.split()
    # Create an empty dictionary
    dictionary = {}
    # Loop through each word in the list
    for word in words:
        # If the word is already a key in the dictionary, increment its value by 1
        if word in dictionary:
            dictionary[word] += 1
        # If the word is not a key in the dictionary, create a new key-value pair with value 1
        else:
            dictionary[word] = 1
    return dictionary
string = "the quick brown fox jumps over the lazy dog"
dictionary = create_dict_from_string(string)
print(dictionary)