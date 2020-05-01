# Secrect Number Game.
import random
max_secret_number=random.randint(5,10)
secret_number= random.randint(0,max_secret_number)
tries=0

tries_max=4
tries_left=tries_max

print(f'''
Welcome to the Secret Number Game!

I'm thinking about a number between 0 and {str(max_secret_number)}.

What do you think it is?
''')

guess=int(input('''
Guess: '''))

while guess!=secret_number and tries<tries_max-1:
    tries+=1
    tries_left-=1
    print(f'''
    Wrong number!
    
    You have {tries_left} tries left!''')
    guess=int(input('''
    Guess: '''))
if guess==secret_number and tries<tries_max: 
    print('''
    Correct! 
    
    Thanks for playing!''')
else:
    print(f'''
    Sorry, you have run out of tries! 
    
    Please play again!
    
    The secret number was {secret_number}''')
