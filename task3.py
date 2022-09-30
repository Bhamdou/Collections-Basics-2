# Task 3
# Create a variable ages which holds a dictionary with the key Peter and the value 36, the key Robin and the value 29 and the key Michael with the value 33. Loop over the dictionary and print the name with the age.

# Your result should look like this:
# Peter is 36 years old
# Robin is 29 years old
# Michael is 33 years old

ages = {"Peter":"36", "Robin": "29", "Michael": "33"}

for key, value in ages.items():
    print(f"{key} is {value} years old.")
