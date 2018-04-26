# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.
import random

low=1
high=100
answer = random.randint(low, high)
print(answer)
guess = int(input("Please Input the Guess between {} and {} :".format(low, high)))
count=0
while guess < high+1:
    if guess < answer:
        print("guess higher")
        guess = int(input("Guess:"))
        count += 1
    elif guess > answer:
        print("guess lower")
        guess = int(input("Guess:"))
        count += 1
    elif guess == answer:
        print("Voila ..!! Guessed Correct")
        print("You took {} attempts to guess".format(count))
        break
    else:
        print("exit")
        break