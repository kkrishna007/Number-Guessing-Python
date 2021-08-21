import random
import math

lower=int(input("Enter Lower Bound - ")) #takes the lower bound of range as input from the user
upper=int(input("Enter Upper Bound - ")) #takes the upper bound of range as input from the user
print("")

number=random.randint(lower,upper) #chooses a random numbere from the range
chances = round(math.log(upper-lower,2))
print ("You've only", chances, "chances to guess the integer")

for i in range(0,chances): #loop initialization
    inp=int(input("Enter your guess - ")) #takes the guess from the user
    if inp==number: #check if the guess is correct
        print("You guessed the number correctly") #output on correct guess
        break #comes out of the loop
    else:
        i=i+1
        if inp>number:
            print ("Number is too high")
        else:
            print ("Number is too low.")
    if i==chances:
        print("You ran out of chances")
        break


