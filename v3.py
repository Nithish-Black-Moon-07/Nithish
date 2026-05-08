principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (e.g., 5 for 5%): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest:.2f}")
