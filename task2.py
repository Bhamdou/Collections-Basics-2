# Task 2
# Create two variables one called bart and the other called homer. Each stores a dictionary, one with the key name and the value Bart Simpson, the other one with the same key but the value Homer Simpson. Create a third variable address with a dictionary which only has one key address.

# Use update to add the address to both bart and homer. Print bart['address'] to the screen.

# Your result should look like this:
# 742 Evergreen Terrace

bart = {"name":"Bart Simpson"}
homer = {"name":"Homer Simpson"}
address = {"address":"742 Evergreen Terrace"}

bart.update(address)
homer.update(address)
