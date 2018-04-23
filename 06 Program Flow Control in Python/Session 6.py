_Author = 'Harsha'

# Session 6

# Continue , Break & Else

groceries_list = ["Atta", "Coffee Powder", "Biscuits","Chips", "Oats"]

for item in groceries_list:
    if item == 'Chips':
        break
    print("Buy " + item)

print("\n")

junk_item = ''
for item in groceries_list:
    if item == 'Chips':
        junk_item = item
        continue
    else:
        print("Please bill me item {}".format(item))

# if junk_item:
#     print("Don't eat junk food like {}".format(item))
