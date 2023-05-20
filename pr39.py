# Get user input for the principal, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (as a percentage): "))
time = float(input("Enter the time (in years): "))

# Calculate the compound interest and total amount
compound_interest = principal * ((1 + (rate/100)) ** time - 1)
total_amount = principal + compound_interest

# Print the results
print("The compound interest is:", compound_interest)
print("The total amount is:", total_amount)