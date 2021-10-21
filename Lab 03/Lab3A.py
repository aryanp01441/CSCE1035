import math

interest_rate = float(input("Enter interest rate as a percent: "))
compound_period = float(input("Enter number of compounding periods per year: "))

r = interest_rate / 100 # Divding interest rate by 100 to get decimal fork

x = r / compound_period # Solving a part of a equation

effective_rate = ((1 + x)**compound_period - 1) * 100 # Final equation

effective_rate = round(effective_rate, 3) # rounding effective rate to 3 decimal points

print(interest_rate, "% interest with", int(compound_period), "compounding periods has an Effective Yield of", effective_rate, "%")