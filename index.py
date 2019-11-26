print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("LET'S PLAY!")
from random import randint
import time
mynumber = randint(1,100)
guesses = 0
while True:
	number = int(input('Enter the number:' )) 
	guesses = guesses + 1
	if number < 1 or number > 100:
		print("OUT OF THE BOUNDS!! Please try again")
		continue
		guesses.append(number)
	if number == mynumber:
		print("Congrats!! you guessed in %d guesses." % (guesses))
		break
	if mynumber < number :
		time.sleep(2)
		print("Guess below")
	elif mynumber > number:
		time.sleep(2)
		print("Guess  above")
