# import random module
import random


# Prompt user to provide an upper and lower range of numbers
# Use the int() to convert the given value to an integer
lower_limit = int(input('Enter your lower limit please: '))
upper_limit = int(input('Enter your upper limit please: '))

# A random number is generated between the lower_limit and upper_limit including both endpoints.
# This will be stored in a variable called lucky_number
lucky_number = random.randint(lower_limit, upper_limit)

# user has 3 chances to guess what random number is which is assigned to the variable 'chances'
chances = 3
print('You have', chances, 'chances to choose the lucky number between',
      lower_limit, 'and', upper_limit, 'with both numbers inclusive')

while True:
    chances -= 1
    guess = int(input('What is the lucky number: '))
    if guess == lucky_number:
        print('Congratulations, you are a pro at guessing.')
    elif guess < lucky_number:
        print(guess, 'is lower than the lucky number.\nTry again')
    elif guess > lucky_number:
        print(guess, 'is higher than lucky number.\nTry again')
    if chances == 0:
        print('sorry, you have ran out of luck.')
        print('The lucky number is', lucky_number)
        print('Better luck next time')
        break
