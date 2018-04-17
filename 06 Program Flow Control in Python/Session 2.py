_Author = 'Harsha'

# Session 2
# If Programming

Name = input("Please enter your name: ")
Age = int(input("Please enter your age ,{}: ".format(Name)))

if (Age > 18) and (Age < 60):  # Format 1 for if condition having two parameters
    print("{},You are eligible for getting Driving License \nPlease apply..!!".format(Name))
elif 11 < Age < 15:
    print("You are too young to Drive .. !! Stay at home ")
elif 60 < Age < 80:  # Format 2 for if condition having two parameters
    print("Don't Apply for Driving License , Take assistance of your Children")
elif Age == 18:
    print("Congrats {}..!! \nYou are Just Eligible for Applying Driving License".format(Name))
elif (Age < 10) or (Age > 80):  # Format 3 for if condition having two parameters
    print("Enjoy .. !! ")
else:
    print(
        "You are age is lower than 18 \nand not eligible for getting a Driving License\nPlease try after {} Years".format(
            18 - Age))
