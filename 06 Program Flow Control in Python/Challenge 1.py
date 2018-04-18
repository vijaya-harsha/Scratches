# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

print("Please give below data to check eligibilty for going to holidays")
Name = input("Enter your Name :")
Age = int(input("Enter your Age:"))

if (Age >= 18) and (Age < 31):
    print("Welcome to Holiday ..!! {}".format(Name))
else:
    print("Sorry ..!! {} you are not allowed to go to Holiday".format(Name))