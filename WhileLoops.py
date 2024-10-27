### Part Two -- your code goes here. 
import random
x = random.randint(1,100)
guess = None

while guess != x:
    guess = int(input("Guess the number between 1 and 100."))
    if guess < x:
        print("Too low")
    elif guess > x:
        print("Too high")
    else:
        print("You guessed it right!")