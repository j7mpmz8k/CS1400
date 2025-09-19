# Jacob Cardon
# CS1400 - MWF - 8:30am

print("Welcome to the Future Value Calculator")

#asks user for investment details and return values
investment = float(input("Enter the starting investment amount: $"))
monthly_payment = float(input("Enter the monthly payment amount: $"))#this is the 'annuity'
annual_rate = float(input("Enter the annual interest rate: %"))
years = float(input("Enter the number of years: "))

try:
    #converts percentage to decimal divided monthly
    monthly_rate = (annual_rate / 100) / 12
    #calculates total months based on on years of investment
    total_months = years * 12
    growth_rate = (1 + monthly_rate) ** total_months
    #orginary annuity formula doesn't contain '* (1 + monthly_rate)' at the end
    # annuity 'due' means payments are due at the begining of each month instead of the end...giving extra month of accural
    annuity_due_rate = ((growth_rate - 1) / monthly_rate) * (1 + monthly_rate)

    #seperates compound interest from initial contribution from monthly annuity contributions, then combines
    initial_future_value = investment * growth_rate
    annuitiy_future_value = monthly_payment * annuity_due_rate
    combined_future_value = round(initial_future_value + annuitiy_future_value, 2)

except ZeroDivisionError:# APY of zero creates error
    combined_future_value = round(investment + (monthly_payment * years), 2)

print(f"Your future value is: ${combined_future_value}")