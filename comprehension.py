import random
# Import Python's built-in random function
guessesTaken = 0
# This is a variable which will be used to count how many guesses the user have used.
print('Hello! What is your name?') # Display a given output message
myName = input()
# Adds a variable with an input value.
number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# Assign a variable to a random number between 1 and 20
while guessesTaken < 6:
    print('Take a guess.')
    guess = input() # guess variable calls user input
    guess = int(guess) # Convert guess variable's value to integer

    guessesTaken += 1 # Adds 1 to the value of guessesTaken named variable 

    if guess < number: # if the value of the guess variable is less than the random picked number beetween 1-20
        print('Your guess is too low.') # Display a given output message

    if guess > number: # If the value of the guess variable is more than the random picked number beetween 1-20
        print('Your guess is too high.') # Display a given output message

    if guess == number: # If the value of the guess variable is equal to random picked number beetween 1-20
        break # If the condition above is true, quit from the while loop

if guess == number: # Condition, that become true when the values of two operands (guess and number) are equal.
    guessesTaken = str(guessesTaken) # If the condition above is true, converts the guessesTaken variable's value to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Displays a given output, with two
    # variables included.
if guess != number: # Condition, that become true when the values of two operands (guess and number) are not equal.
    number = str(number) #Converts the number variable to a string
    print('Nope. The number I was thinking of was ' + number) #Displays a given output with a given message and the 'number' variable