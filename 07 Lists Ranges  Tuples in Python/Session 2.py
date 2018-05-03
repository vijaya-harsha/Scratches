_Author = "Harsha"

# Lists

list_1 = []
list_2 = list()

print("List 1 {}".format(list_1))
print("List 2 {}".format(list_2))

if list_1 == list_2:
    print("They are equal")
else:
    print("Not equal")

product = ['milk', 'curd', 'paneer', 'yogurt']
products = ['Coke', 'Mountain Dew', 'Sprite', 'Minute Maid']

another_product = product

# We get true because both the list are equal
print(another_product is product)

print(product)
print(another_product)

another_product = list(product)

# we get false because list constructor
# is added to product list which makes it another list
print(another_product is product)


# we get true because the content in both the lists are compared and they are equal
print(another_product == product)

product = ['milk', 'curd', 'paneer', 'yogurt']
products = ['Coke', 'Mountain Dew', 'Sprite', 'Minute Maid']


all_products = [product, products]

print(all_products)
# Output
# [['milk', 'curd', 'paneer', 'yogurt'], ['Coke', 'Mountain Dew', 'Sprite', 'Minute Maid']]


for i in all_products:
    print(i)
    for j in i:
        print(j)

# Output
# ['milk', 'curd', 'paneer', 'yogurt']
# milk
# curd
# paneer
# yogurt
# ['Coke', 'Mountain Dew', 'Sprite', 'Minute Maid']
# Coke
# Mountain Dew
# Sprite
# Minute Maid