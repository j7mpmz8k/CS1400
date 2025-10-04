# Jacob Cardon
# CS1400 - MWF - 8:30am
import random

class Animal:
    pass
animal_list = []

#initializing the Animalinator
animalinator = Animal()
animal_list.append(animalinator)
animalinator.name = ""
animalinator.noise = ""
animalinator.count = 0

print("Dr. Doofenlittle Welcomes You to The Animalinator")
print("Tell me about three animals you have seen")

#creates objects of each animal user saw, including how many they saw, and what noise they made
#also appends each attribute of each animal to the Animalinator object
animal_pos = ["first", "second", "third", "forth"]
for i in range(1, 4):
    animal_list.append(Animal())

    animal_list[i].name = str(input(f"What was the {animal_pos[i-1]} kind of animal you saw? "))
    animalinator.name += animal_list[i].name

    animal_list[i].count = int(input("How many did you see? "))
    animalinator.count += animal_list[i].count

    animal_list[i].noise = str(input("What did they say? "))
    animalinator.noise += animal_list[i].noise

#scrambles Animalinator's name
animalinator.name = list(animalinator.name)
random.shuffle(animalinator.name)
animalinator.name = "".join(animalinator.name)
#scrambles Animalinator's sounds
animalinator.noise = list(animalinator.noise)
random.shuffle(animalinator.noise)
animalinator.noise = "".join(animalinator.noise)

print("\nI am adding them to my Animalinator...")
input("\tHit Enter to see the results. ")

#prints number of animals seen
print(f"\nYou saw a total of {animalinator.count} animals. Very imporessive.\nThere were", end=" ")
for i in range(1, 4):
    if i != 3:
        print(animal_list[i].name, end="s, ")
    else:
        print(f"{animal_list[i].name}s.")
#prints what animals said
for i in range(1, 4):
    print(f"The {animal_list[i].name}s all said {animal_list[i].noise}.")

#prints Animalinator items
print("The Animalinator made something for you from all the animals you saw.")
animalinator.count = animalinator.count // (len(animal_list)-1)#finds avg for num of animalinators
print(f"\tYou now have {animalinator.count} {animalinator.name}s that all say {animalinator.noise}.")