import random
compGuess = random.randint(0,100) #Computer selects a random number
attemptCount = 0 #Counter on Number of attempts

while True:
    userGuess = int(input("Please guess a number between 0 - 100:"))
    if userGuess<0 or userGuess>100: #Checking if it is a valid user input or not
        print("Please enter a correct number")
        continue
    attemptCount = attemptCount + 1 #Incrementing by 1 everytime a user guesses a number
    if userGuess > compGuess:
        print("You need to guess a lower number.")
    elif userGuess < compGuess:
        print("You need to guess a higher number.")
    else:
        print("Well Done, you have guessed the correct after " + str(attemptCount) + " attempts")
        attemptCount = 0
        break