# Jacob Cardon
# CS1400 - MWF - 8:30am

print("Welcome to the Future Value Calculator")

#asks user for investment details and return values
investment = float(input("Enter the starting investment amount: $"))
monthly_payment = float(input("Enter the monthly payment amount: $"))#this is the 'annuity'
annual_rate = float(input("Enter the annual interest rate: %"))
years = float(input("Enter the number of years: "))

#converts percentage to a decimal divided up as monthly instead of anually
monthly_rate = (annual_rate / 100) / 12
#calculates total months based on on expected years of investment
total_months = years * 12

growth_rate = (1 + monthly_rate) ** total_months
# '* (1 + monthly_rate)' at the end makes this the annuity 'due' formula instead of orginary annuity 
# annuity due means payments are due at the begining of each month instead of the end...giving 1 extra month of accural
annuity_due_rate = ((growth_rate - 1) / monthly_rate) * (1 + monthly_rate)

initial_future_value = investment * growth_rate
annuitiy_future_value = monthly_payment * annuity_rate
combined_future_value = round(initial_future_value + annuitiy_future_value, 2)

print(f"Your future value is: ${combined_future_value}")