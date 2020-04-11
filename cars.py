# **************************** Challenge: Showroom & Junkyard ****************************
print("************ Showroom & Junkyard *************************")
"""
Author: Trinity Terry
pyrun: python cars.py
"""
# Create an empty set named showroom.
showroom = set()
print("1 .************************************************** \n Create an empty set named showroom. \n ")
print(showroom, "\n")


# Add four of your favorite car model names to the set.
showroom.add("BMW")
showroom.add("Audi")
showroom.add("Bentley")
showroom.add("Cadillac")
print("2. ************************************************** \n Add four of your favorite car model names to the set \n ")
print(showroom, "\n")

# Print the length of your set.
print("3. ************************************************** \n Print the length of your set \n")
print(len(showroom), "\n")

# Pick one of the items in your show room and add it to the set again.
showroom.add("Audi")
# Print your showroom. Notice how there's still only one instance of that model in there.
print("4. ************************************************** \n Pick one of the items in your show room and add it to the set again \n Print your showroom. Notice how there's still only one instance of that model in there \n")
print(showroom, "\n")

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Ferrari", "Nissan"})
print("5. ************************************************** \n Using update(), add two more car models to your showroom with another set")
print(showroom, "\n")

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Ferrari")
print("6. ************************************************** \n You've sold one of your cars. Remove it from the set with the discard() method \n")
print(showroom, "\n")


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"Nissan", "Honda", "Dodge", "Cooper", "Mini"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print("7. ************************************************** \n Use the intersection method to see which cars exist in both the showroom and that junkyard \n")
print(junkyard.intersection(showroom), "\n")

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print("8. ************************************************** \n Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom \n")
print(showroom, "\n")

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
showroom.discard("Audi")
showroom.discard("Mini")
showroom.discard("Cooper")

print("9. ************************************************** \n Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom. \n")
print(showroom, "\n")