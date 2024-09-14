#!/usr/bin/env python3
# Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings
annual_savings = monthly_savings * 12
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)

# Output results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings after one year with interest: ${projected_savings:.2f}")
