import random
import math

lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter upper bound: '))

x = random.randint(lower_bound, upper_bound)
print('You have', round(math.log((upper_bound - lower_bound), 2)), 'chances to guess the integer')

count = 0

while count < math.log((upper_bound - lower_bound), 2):
    count += 1

    guess = int(input('Guess the Number: '))
    if x == guess:
         print('Congratulation, you have guessed it in', count, 'times')
         break

    elif x>guess:
         print('You have gone too small')

    elif x<guess:
         print('You have gone too far')

if count >= round(math.log((upper_bound - lower_bound), 2)):
    print('You are chances have been completed, the secret number is: ', x)
