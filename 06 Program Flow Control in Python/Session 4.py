import string

# importing string module to get alphabets

_Author = 'Harsha'

# Session 4

# For Loops


for i in range(0, 10):
    print("i is now {}".format(i))

character = 'VijayaHarsha23111991'

# 'len' is function used to get length of the string

for i in range(0, len(character)):
    print(character[i])

# Output
# V
# i
# j
# a
# y
# a
# H
# a
# r
# s
# h
# a
# 2
# 3
# 1
# 1
# 1
# 9
# 9
# 1

alpha = string.ascii_lowercase

for i in range(0, len(character)):
    if character[i] in alpha:
        print(character[i])

# Output
# i
# j
# a
# y
# a
# a
# r
# s
# h
# a

num = string.digits

for i in range(0, len(character)):
    if character[i] in num:
        print(character[i])

# Output
# 2
# 3
# 1
# 1
# 1
# 9
# 9
# 1

# In the below example we can see in print statement after , end = ' '
# This will print the output by seperating them by ' '
# By Default the output is separated by newline character

for i in range(0, len(character)):
    if character[i] in num:
        print(character[i], end=' ')

# Output
# 2 3 1 1 1 9 9 1
