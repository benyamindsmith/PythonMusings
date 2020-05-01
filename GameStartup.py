# Game Startup Engine

print('''
Welcome to Ben's Game Startup Engine!

Type 'help' in the console for instruction:

''')

user_input=input('> ')

while user_input !='quit':
    if user_input=='start':
        print('''
        The game has been started!
        ''')
    elif user_input.lower()=='help':
                print('''
        Type 'start' to start the game

        Type 'stop' to pause the game

        Type 'quit' to quit the game
        ''')
    elif user_input=='stop':
        print('''
        Game paused
        ''')
    user_input=input('> ')
else: 
        print('''
        Game exited! Thank you for playing!''')
