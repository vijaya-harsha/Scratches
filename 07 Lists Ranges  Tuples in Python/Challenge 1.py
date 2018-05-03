# add to the program below so that if it finds a meal without Buttermilk
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

meal = []

meal.append(["Potato Curry", "Sambar", "Veg Gravy", "Curd"])
meal.append(["Brijal Fry", "Palak Dal", "Papad", "Curd"])
meal.append(["Okra Fry", "Methi Dal", "Rajma", "Buttermilk"])
meal.append(["Tomato Cashew Curry", "Roti", "Biryani", "Raita", "Buttermilk"])

# print(meal)

# Output
# [['Potato Curry', 'Sambar', 'Veg Gravy', 'Curd'], ['Brijal Fry', 'Palak Dal', 'Papad', 'Curd'], ['Okra Fry', 'Methi Dal', 'Rajma', 'Curd'], ['Tomato Cashew Curry', 'Roti', 'Biryani', 'Raita', 'Buttermilk']]
item = ""
for menu in meal:
    if "Buttermilk" not in menu:  # this check the content in sub lists
        print(menu)
        for item in menu:
            print(item)
