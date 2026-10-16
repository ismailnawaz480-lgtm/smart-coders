"""Problem 003: Calculate simple interest given P, R, T → (P × R × T) / 100"""

p = float(input("Enter principal: "))
r = float(input("Enter annual rate (%): "))
t = float(input("Enter time in years: "))
simple_interest = (p * r * t) / 100
print("Simple interest:", simple_interest)
