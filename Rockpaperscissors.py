import random

computerscore = 0
playerscore = 0

while True: 
        print("Make your move: Rock, Paper, Scissors?")

        playermove = str(input())
        playermove = playermove.lower()

        print("Ahh..so you chose", playermove)

        moves = ['rock', 'paper', 'scissors']

        computermove = random.choice(moves)

        computerwins = "Sorry buddy! You lose! The computer wins."

        playerwins = "Yay! You win!"

        print("Well, the computer chose", computermove)
        if playermove in moves:
                if playermove == computermove:
                        print("Wrap it up folks! We have a tie!")
                        computerscore = computerscore+1
                        playerscore = playerscore+1
                if playermove == 'rock':
                        if computermove == 'paper':
                                print(computerwins)
                                computerscore = computerscore+1
                        elif computermove == 'scissors':
                                print(playerwins)
                                playerscore = playerscore+1
                if playermove == 'paper':
                        if computermove == 'scissors':
                                print(computerwins)
                                computerscore = computerscore+1
                        elif computermove == 'rock':
                                print(playerwins)
                                playerscore = playerscore+1
                if playermove == 'scissors':
                        if computermove == 'rock':
                                print(computerwins)
                                computerscore = computerscore+1
                        elif computermove == 'paper':
                                print(playerwins)
                                playerscore = playerscore+1
        else:
                print("Hey! What was that? Please try again!")

        print("Computer:", computerscore, "- Player:", playerscore)
        print()
