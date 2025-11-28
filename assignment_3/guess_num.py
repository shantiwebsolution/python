import random
print("Welcome to the Number Guessing Game!  You have 10 attempts to guess the number between 1 and 50.")
number = random.randint(1, 50)
loop =1
while loop <= 10:
    
    guess = int(input("Guess a number between 1 and 50: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    else:
        if guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    loop += 1
