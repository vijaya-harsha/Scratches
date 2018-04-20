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

for android in ['CupCake', 'Donut', 'Eclair', 'Froyo', 'GingerBread', 'HoneyComb', 'Icecream Sandwich', 'JellyBean',
                'Kitkat', 'Lolipop', 'Marshmallow', 'Nogut', 'Oreo']:
    # format 1
    # print("Android CodeNames are {}".format(android))
    # format 2
    print("Android CodeNames are " + android)

# Output
# Android CodeNames are CupCake
# Android CodeNames are Donut
# Android CodeNames are Eclair
# Android CodeNames are Froyo
# Android CodeNames are GingerBread
# Android CodeNames are HoneyComb
# Android CodeNames are Icecream Sandwich
# Android CodeNames are JellyBean
# Android CodeNames are Kitkat
# Android CodeNames are Lolipop
# Android CodeNames are Marshmallow
# Android CodeNames are Nogut
# Android CodeNames are Oreo

# In below example we can see range (x,y,z)
# 'z' is a step where number start with x and end with y skipping z items

for i in range(0, 50, 5):
    print("i is {}".format(i))

