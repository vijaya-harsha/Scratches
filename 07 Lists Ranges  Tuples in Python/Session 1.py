_Author = "Harsha"

# Reference for Functions and Menthods for Python
# https://www.tutorialspoint.com/python/python_lists.htm

# Session 1

# Lists

groceries = ['Atta', 'Jam', 'Ketchup', 'Pasta']
groceries2 = ['Chocolates', 'Drink', 'Beer', 'Vodka']

# We can add one item to a list using append() method

groceries.append('PaperBoat')

groceries3 = groceries + groceries2

groceries.count('Atta')

for items in groceries3:
    print("Groceries that are needed " + items)

print(groceries.count("Atta"))


