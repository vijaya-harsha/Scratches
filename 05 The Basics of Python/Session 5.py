# Session 5
# Session About Variables

var1 = "Lionel Messi\n"
var2 = "Osamane Dembele\n"
var3 = "Luis Suarez\n"

var4 = "FC Barcelona"

print(var1 + var2 + var3 + 'are in ' + var4)

# we get the letter of a particular string by using below syntax

print(var1[0])
print(var2[8])
print(var3[5])

# We can get the letter of particular string in reverse order by using belopw syntax

print(var3[-2])

# To print get particular value of a string

print(var1[0:5])  # we can also use print(var1[:5])
print(var2[0:7])  # we can also use print(var1[:7])
print(var3[:4])  # we can also use print(var1[0:4])

# From below example we can see printing var1 skipping every 2 nd letter including space

print(var1[0:11:2])  # L i o n e l  M e s s i

# Output of above is Loe es
# Position           0246810

# From below example we can see printing skipping every 3rd letter

print(var4[0:11:3])    # F C  B a r c e l o n a

# Output of above is FBco
# Position           0369

var5= "1,456,789,101,121,314"

print(var5[1::4])

# Output of above is ,,,,,

# We can do multiplication of string
# See below example for reference

print("Good Noon " * 5 )
# Output is Good Noon Good Noon Good Noon Good Noon Good Noon 


