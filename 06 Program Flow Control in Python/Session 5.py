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

# Output
# i is 0
# i is 5
# i is 10
# i is 15
# i is 20
# i is 25
# i is 30
# i is 35
# i is 40
# i is 45

for i in range(1, 11):
    for j in range(1, 11):
        print("{} times {} is {}".format(i, j, i * j))
    print("----------------")

# Output
# 1 times 1 is 1
# 1 times 2 is 2
# 1 times 3 is 3
# 1 times 4 is 4
# 1 times 5 is 5
# 1 times 6 is 6
# 1 times 7 is 7
# 1 times 8 is 8
# 1 times 9 is 9
# 1 times 10 is 10
# ----------------
# 2 times 1 is 2
# 2 times 2 is 4
# 2 times 3 is 6
# 2 times 4 is 8
# 2 times 5 is 10
# 2 times 6 is 12
# 2 times 7 is 14
# 2 times 8 is 16
# 2 times 9 is 18
# 2 times 10 is 20
# ----------------
# 3 times 1 is 3
# 3 times 2 is 6
# 3 times 3 is 9
# 3 times 4 is 12
# 3 times 5 is 15
# 3 times 6 is 18
# 3 times 7 is 21
# 3 times 8 is 24
# 3 times 9 is 27
# 3 times 10 is 30
# ----------------
# 4 times 1 is 4
# 4 times 2 is 8
# 4 times 3 is 12
# 4 times 4 is 16
# 4 times 5 is 20
# 4 times 6 is 24
# 4 times 7 is 28
# 4 times 8 is 32
# 4 times 9 is 36
# 4 times 10 is 40
# ----------------
# 5 times 1 is 5
# 5 times 2 is 10
# 5 times 3 is 15
# 5 times 4 is 20
# 5 times 5 is 25
# 5 times 6 is 30
# 5 times 7 is 35
# 5 times 8 is 40
# 5 times 9 is 45
# 5 times 10 is 50
# ----------------
# 6 times 1 is 6
# 6 times 2 is 12
# 6 times 3 is 18
# 6 times 4 is 24
# 6 times 5 is 30
# 6 times 6 is 36
# 6 times 7 is 42
# 6 times 8 is 48
# 6 times 9 is 54
# 6 times 10 is 60
# ----------------
# 7 times 1 is 7
# 7 times 2 is 14
# 7 times 3 is 21
# 7 times 4 is 28
# 7 times 5 is 35
# 7 times 6 is 42
# 7 times 7 is 49
# 7 times 8 is 56
# 7 times 9 is 63
# 7 times 10 is 70
# ----------------
# 8 times 1 is 8
# 8 times 2 is 16
# 8 times 3 is 24
# 8 times 4 is 32
# 8 times 5 is 40
# 8 times 6 is 48
# 8 times 7 is 56
# 8 times 8 is 64
# 8 times 9 is 72
# 8 times 10 is 80
# ----------------
# 9 times 1 is 9
# 9 times 2 is 18
# 9 times 3 is 27
# 9 times 4 is 36
# 9 times 5 is 45
# 9 times 6 is 54
# 9 times 7 is 63
# 9 times 8 is 72
# 9 times 9 is 81
# 9 times 10 is 90
# ----------------
# 10 times 1 is 10
# 10 times 2 is 20
# 10 times 3 is 30
# 10 times 4 is 40
# 10 times 5 is 50
# 10 times 6 is 60
# 10 times 7 is 70
# 10 times 8 is 80
# 10 times 9 is 90
# 10 times 10 is 100
# ----------------