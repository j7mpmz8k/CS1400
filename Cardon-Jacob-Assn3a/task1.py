# Jacob Cardon
# CS1400 - MWF - 8:30am

print("Welcome to the Grokian Clendar Leap Year Calculator")
year = int(input("\tEnter a year to find out if it is a Leap Year: "))

#extracts each digit from year
first = int(str(year)[0])
second = int(str(year)[1])
third = int(str(year)[2])
last = int(str(year)[3])

#Case 1 conditions
divisible_by_9 = year % 9 == 0
unique_last_2_num = third != last
case_1 = divisible_by_9 and unique_last_2_num

#Case 2 conditions
sum_of_halves_match = first * 10 + second == third + last
third_digit_even = third % 2 == 0
third_less_than_last = third < last
case_2 = sum_of_halves_match and third_digit_even and third_less_than_last

#ending message
end_mssg = "\nThank you for using the Frokian Calendar Leap Year Calculator"
leap_year_msg = f"\n\tYor year, {year} is a leap year!"
regular_year_msg = f"\n\tYour year, {year}, is just a plain old year! Happy Nothing!"

#Checks if leap year...finds relevant concluding end message
if case_1 or case_2 == True:
    end_mssg += leap_year_msg
else: end_mssg += regular_year_msg

print(end_mssg)