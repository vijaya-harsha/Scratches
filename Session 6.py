# Session 6
# String Formating
_author_ = 'Harsha'

age = 27

Name = "Vijaya Harsha"

print(Name + " " + str(age) + "Years")
# Output Vijaya Harsha 27Years

# We use str method to convert the int to string

print("My age is {0} years".format(age))
# Output My age is 27 years

# {0} is called a Replacement field and we replace by using it with using .format()

# Example 2

print("There are {0} in {1},{2},{3},{4},{5},{6},{7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# Output There are 31 in Jan,Mar,May,Jul,Aug,Oct,Dec

# Example 3
# In below example we can see that replacement field can start with 2 1 or 0

print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

# Output
# Jan: 31
# Feb: 28
# Mar: 31
# Apr: 30
# May: 31
# Jun: 30
# Jul: 31
# Aug: 31
# Sep: 30
# Oct: 31
# Nov: 30
# Dec: 31

# Example 4

for i in range(1, 10):
    print("No. {0:2} squared is {2:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# Here in {0:2}
# 0 is called the replacement field
# 2 is the width where the value is assigned to


# Output
# No.  1 squared is    1 and cubed is    1
# No.  2 squared is    8 and cubed is    8
# No.  3 squared is   27 and cubed is   27
# No.  4 squared is   64 and cubed is   64
# No.  5 squared is  125 and cubed is  125
# No.  6 squared is  216 and cubed is  216
# No.  7 squared is  343 and cubed is  343
# No.  8 squared is  512 and cubed is  512
# No.  9 squared is  729 and cubed is  729
