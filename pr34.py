n = int(input())
a = 0
b = 1
for i in range(n + 1):
    c = a + b
    a = b
    b = c
if a == n or b == n:
    print("Fibonaccy")
else:
    print("Not Fibonaccy")