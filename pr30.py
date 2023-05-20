
a = int(input())
b = int(input())


print(f"Before swapping: a = {a}, b = {b}")


a = a ^ b
b = a ^ b
a = a ^ b


print(f"After swapping: a = {a}, b = {b}")