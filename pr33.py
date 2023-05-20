n = int(input())
a = 0
b = 1
sum = 1
for i in range(n + 1):

    c = a + b
    a = b
    b = c
    sum *= a
print(sum)