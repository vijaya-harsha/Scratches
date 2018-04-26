_Author = "Harsha"

# Session 8

# While Loop

i = 0

while i < 10:
    print("I value is {}".format(i))
    i += 1

food_items= ["Dal", "Rice", "Curry", "Curd", "Chips"]

choose=""
while choose not in food_items:
    choose = input("Enter food: ")
    if choose == "Over":
        print("I'm done")
        break
    elif choose in food_items:
        print("Proceed with your Favorite meal")
    else:
        print("Item not available in the list .. !! \nRetry with Other Option")
