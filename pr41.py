# Get user input for the principal, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (as a percentage): "))
time = float(input("Enter the time (in years): "))

# Calculate the simple interest and total amount
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

# Print the results
print("The simple interest is:", simple_interest)
print("The total amount is:", total_amount)