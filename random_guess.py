import random
player_guess = int(input('Enter a number: '))
computer_guess = random.randint(1, 10)

for guess in range(1, 3):
	if player_guess == computer_guess:
		print('You are a genius! your guess is correct')
		break;
	if player_guess != computer_guess:
		print('Wrong guess! Try again')
		guess += 1
		player_guess = int(input('Enter a number: '))
print('Sorry, You lost!')



