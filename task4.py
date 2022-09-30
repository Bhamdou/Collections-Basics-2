# Task 4
# Store the animals Alligator, Tiger, Parrot, Hamster, and Dolphin as keys in a dict. Use random numbers as values. Now remove all keys ending with r from the dictionary and print the resulting dict to the screen.

# Your result should look similar to this:
# {'Dolphin': 8, 'Parrot': 2}



animals = {"Alligator":1, "Tiger": 5, "Parrot": 6, "Hamster": 9, "Dolphin": 3}

for key,value in list(animals.items()):
    if key[-1] == "r":
        del animals[key]
print(animals)