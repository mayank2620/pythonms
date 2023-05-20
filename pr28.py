
char = input("Enter a character: ")


if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")