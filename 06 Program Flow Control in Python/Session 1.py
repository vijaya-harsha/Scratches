_author = "Harsha"
# Session 1
# If Program Flow

Name = input("Please enter your name: ")
Age = int(input("Please enter your age ,{}: ".format(Name)))

if Age >= 18:
    print("Your are eligible for getting Driving License")
else:
    print("You are age is lower than 18 \nand not eligible for getting a Driving License\nPlease try after {} Years".format(18 - Age))

# Convert string to int using below 'int' function

# We get below error when print Name with Age2 since Age2 is int datatype and Name is String

# TypeError: must be str, not int
