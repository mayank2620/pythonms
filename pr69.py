import random
n = random.randint(1,10)
score = 0
while True:
  x = int(input("Enter The Number You Guessed:"))
  if n < x:
    print("Go Lower")
    score+=1
  elif n > x:
    print("Go Higher")
    score+=1
  elif n == x:
    print("Hey You Guessed it Right")
    score+=1
    break
print(f"You Guessed Correct in {score} attemps")