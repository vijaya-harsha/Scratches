_Author = 'Harsha'

# Session 6

# Continue , Break & Else

groceries_list = ["Atta", "Coffee Powder", "Biscuits", "Oats", "Chips"]

for item in groceries_list:
    if item == 'Chips':
        break
    print("Buy " + item)

junk_item = ''
for item in groceries_list:
    if item == 'Chips':
        junk_item = item
        break
    else:
        print("Please bill me all items {}".format(item))

# if junk_item:
#     print("Don't eat junk food like {}".format(item))
