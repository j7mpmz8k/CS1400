# Jacob Cardon
# CS1400 - MWF - 8:30am

print("Welcome to the Future Value Calculator")

#asks user for investment details and return values
investment = float(input("Enter the starting investment amount: $"))
monthly_payment = float(input("Enter the monthly payment amount: $"))
annual_APY = float(input("Enter the annual interest rate: %"))
years = float(input("Enter the number of years: "))

#converts percentage to a decimal divided up as monthly instead of anually
monthly_APY = (annual_APY / 100) / 12
#calculates total months based on on expected years of investment
total_months = years * 12



initial_investment_future_value = investment * (1 + monthly_APY)** total_months
monthly_payment_future_value = monthly_payment * ((((1 + monthly_APY) ** total_months)-1)/monthly_APY)
combined_future_value = round(initial_investment_future_value + monthly_payment_future_value, 2)

print(f"Your future value is: ${combined_future_value}")