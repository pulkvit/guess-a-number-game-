import random

def guess(x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess < random_number:
            print('sorry,guess again .Too low.')
        elif guess>random_number:
            print('sorry,guess again.too high.')


    print("congo you have guessed the number correctly")
guess(10)
def computer_guess(x):
    low =1
    high=x
    feedback = ''
    while feedback != 'c':
        if low !=high:
            guess= random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (h) , too low(l), or correct(c)')
        if feedback=="h":
            high = guess-1
        elif  feedback == "l":
            low = guess+1
    print(f"you got the number")

computer_guess(10)
