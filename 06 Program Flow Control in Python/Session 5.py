_Author = 'Harsha'

num = '123,345,455,4353,7567,76867'
sep = ''

for char in num:
    if char in '123456789':
        sep = sep + char

newsep = int(sep)

print("The Num is {}".format(newsep))

# Output
# The Num is 1233454554353756776867

