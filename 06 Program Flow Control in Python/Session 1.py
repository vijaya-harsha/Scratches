_author = "Harsha"
# Session 1
# If Program Flow

# Name = input("Please enter your name: ")
# Age = int(input("Please enter your age ,{}: ".format(Name)))
#
# if Age >= 18:
#     print("Your are eligible for getting Driving License")
# else:
#     print(
#         "You are age is lower than 18 \nand not eligible for getting a Driving License\nPlease try after {} Years".format(
#             18 - Age))

# Convert string to int using below 'int' function

# We get below error when print Name with Age2 since Age2 is int datatype and Name is String

# TypeError: must be str, not int

# If -- Elif -- Else

Name = input("Please enter your name: ")
Age = int(input("Please enter your age ,{}: ".format(Name)))

if Age > 18 and Age < 60:
    print("{},You are eligible for getting Driving License \nPlease apply..!!".format(Name))
elif Age > 60:
    print("Don't Apply for Driving License , Take assistance of your Children")
elif Age < 15:
    print("You are too young to Drive .. !! Stay at home ")
elif Age == 18:
    print("Congrats {}..!! \nYou are Just Eligible for Applying Driving License".format(Name))
else:
    print(
        "You are age is lower than 18 \nand not eligible for getting a Driving License\nPlease try after {} Years".format(
            18 - Age))
