#guess number
import random
def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num: 
        guess = int(input(f"Enter a number between 1 and {x}"))
        if guess < random_num:
            print("sorry man!! you guessed it too low")
        elif guess > random_num:
            print("sorry man!! you guessed it too high")
    print(f"Bravoo {random_num} is right guess")


guess(10)
