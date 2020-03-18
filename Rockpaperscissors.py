import random

while True: 
	print("Make your move: Rock, Paper, Scissors?")

	playermove = str(input())
	playermove = playermove.lower()

	print("Ahh..so you chose", playermove)

	moves = ['rock', 'paper', 'scissors']

	computermove = random.choice(moves)

	print("Well, the computer chose", computermove)
	if playermove in moves:
		if playermove == computermove:
			print("Wrap it up folks! We have a tie!")
		if playermove == 'rock':
			if computermove == 'paper':
				print("Sorry buddy! You lose!")
			elif computermove == 'scissors':
				print("Yay! You win!")
		if playermove == 'paper':
			if computermove == 'scissors':
				print("Sorry buddy! You lose!")
			elif computermove == 'rock':
				print("Yay! You win!")
		if playermove == 'scissors':
			if computermove == 'rock':
				print("Sorry buddy! You lose!")
			elif computermove == 'paper':
				print("Yay! You win!")
	else:
		print("Hey! What was that? Please try again!")

	print()
