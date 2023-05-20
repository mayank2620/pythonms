amount = int(input("Enter The Amount"))
num_2k = amount//2000
num__500 = amount//500
if amount <= 100:
    num__100 = amount//100
else :
    num__100 = 1
print("2000 notes are",num_2k)
print("500 notes are",num__500)
print("100 notes are",num__100)