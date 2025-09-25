# Jacob Cardon
# CS1400 - MWF - 8:30am

import random

#welcome message with instructions
print("Welcome to the Guessing Game")
print("The Computer has picked a number from 1 - 10. Try to match it.")

#random number chosen then asks user to input guess
solution = random.randint(1,10)
answer = int(input("What number do you choose (1-10): "))

#reveals correct answer and repeases user's guess
print(f"You picked {answer} and the actual number was {solution}.")

#checks for correct answer and appropriate message printed based on how correct or how far off answer is
if answer == solution:# if correct
    print("Honored to play with you, True Aggie.")
elif abs(solution - answer) == 1:# off by one
    print("You are a worthy apponent, Big Blue.")
elif abs(solution - answer) == 2:# off by two
    print("You have much to learn, Hurd.")
elif abs(solution - answer) == 3:# off by three
    print("Little Blue, your time will come.")
else:# off by four or more
    print("Keep working hard on the Quad.")