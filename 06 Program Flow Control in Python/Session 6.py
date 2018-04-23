_Author = 'Harsha'

# Session 6

# Continue , Break & Else

groceries_list = ["Atta", "Coffee Powder", "Biscuits", "Chips", "Oats"]

for item in groceries_list:
    if item == 'Chips':
        break
    print("Buy " + item)

# Output
# Buy Atta
# Buy Coffee Powder
# Buy Biscuits

print("\n")

junk_item = ''
for item in groceries_list:
    if item == 'Chips':
        junk_item = item
        continue
    else:
        print("Please bill me item {}".format(item))

# Output
# Please bill me item Atta
# Please bill me item Coffee Powder
# Please bill me item Biscuits
# Please bill me item Oats
