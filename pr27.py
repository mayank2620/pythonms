alphabet = input("Enter an alphabet: ")


if alphabet in ('a', 'e', 'i', 'o', 'u'):
    print(alphabet, "is a vowel")


elif alphabet.isalpha():
    print(alphabet, "is a consonant")


else:
    print("Error: Please enter a letter of the alphabet.")