# Game Startup Engine

print('''
Welcome to Ben's Game Startup Engine!

Type 'help' in the console for instruction:

''')

user_input=input('> ')

while True:
    if user_input=='start':
        print('''
        The game has been started!
        ''')
        user_input=input('> ')
    elif user_input.lower()=='help':
                print('''
        Type 'start' to start the game

        Type 'stop' to pause the game

        Type 'quit' to quit the game
        ''')
                user_input=input('> ')
    elif user_input=='stop':
        print('''
        Game paused
        ''')
        user_input=input('> ')
    elif user_input=='quit':
        
        print('''
        Game exited! Thank you for playing!''')
        break 
    else: 
        print("sorry I do not understand that")
        user_input=input('> ')
