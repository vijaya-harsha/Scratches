_Author = "Harsha"

# abcabdeab
#
# find the max repeated character and its frequency
#
# Example:
# a-100
#
#
# 2.
# ab-count
#
# 3. three characters...
# abc

# char = "abcabdeaba"
# count = 0
# counter = 0
# for i in range(0, len(char)):
#     # print(char[i])
#     for j in range(0, len(char)):
#         # print(char[i]+char[j])
#         if char[i] + char[j] == "ab":
#             count += 1
#         for k in range(0, len(char)):
#             # print(char[i] + char[j]+char[k])
#             if char[i] + char[j] + char[k] == "abc":
#                 counter += 1
#
#
# print("Count of ab is {}".format(count))
# print("Count of abc is {}".format(counter))


char = "abcabdeaba"
count = coun = cou = co = 0

for i in range(0, len(char)):
    if char[i] == "a":
        count += 1
    if char[i] == "b":
        coun += 1
    if char[i] == "c":
        cou += 1
    if char[i] == "d":
        co += 1

print("Count for a {}".format(count))
print("Count for b {}".format(coun))
print("Count for c {}".format(cou))
print("Count for d {}".format(co))

char = "abcabdeaba"
counter=0
for i in range(0, len(char)):
    for j in range(0, len(char)):
        if j == (i+1):
            if char[i]+char[j] == "ab":
                counter += 1
print("ab is repeated for {}".format(counter))

counter1=0
for i in range(0, len(char)):
    for j in range(0, len(char)):
        for k in range(0, len(char)):
            if j == (i+1) and k == (i+2):
                if char[i]+char[j]+char[k] == "abc":
                    counter1 += 1
print("abc is repeated for {}".format(counter1))


char = "abcabdeaba"
incre=0
prevCount=0
index = -1
for i in range(0, len(char)):
    incre = 0
    for j in range(0, len(char)):
        if char[i] == char[j]:
            incre += 1
    if i == 0:
        prevCount = incre
    else:
        if prevCount < incre:
            prevCount = incre
            index = char[i]

print(str(prevCount)+" with "+char[index])