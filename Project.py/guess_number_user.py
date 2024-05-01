#guess number
import random 
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high) 
        else:
            guess = high
        feedback = input(f"Is {guess} is too high (H) or guess is too low (L) or guess is correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("the computer guessed the number right Amazing")
computer_guess(10)            
