# Jacob Cardon
# CS1400 - MWF - 8:30am

print("Welcome to the Omni-Calculator, your one-stop shop for all of your arithmetic needs")
first_num = float(input("What is the first number? "))
second_num = float(input("What is the second number? "))

print(f"unary + applied to {first_num} is", +first_num)
print(f"unary + applied to {second_num} is", +second_num)
print(f"unary - applied to {first_num} is", -first_num)
print(f"unary - applied to {second_num} is", -second_num)
print(f"{first_num} ** {second_num} =", first_num ** second_num)
print(f"{first_num} * {second_num} =", first_num * second_num)
print(f"{first_num} / {second_num} =", first_num / second_num)
print(f"{first_num} // {second_num} =", first_num // second_num)
print(f"{first_num} % {second_num} =", first_num % second_num)
print(f"{first_num} + {second_num} =", first_num + second_num)
print(f"{first_num} - {second_num} =", first_num - second_num)
print("Thank you for using the Omni-Calculator!")
