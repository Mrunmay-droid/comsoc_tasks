import random as rd

lown=int(input("Enter the lower limit of range"))
highn=int(input("Enter the upper limit of your range"))

guess=rd.randint(lown,highn)
user_guess=int(input("Guess the number"))

while(user_guess != guess):
    if(user_guess > guess):
        print("Should go lower")
        user_guess=int(input("Guess again"))
    elif(user_guess < guess):
        print("Should go higher")
        user_guess=int(input("Guess again"))
    else:
        break
print("That is correct")
