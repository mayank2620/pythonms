character = input("Enter a character: ")


if character.isalpha():
    print(character, "is an alphabet")


elif character.isdigit():
    print(character, "is a digit")


else:
    print(character, "is a special character")