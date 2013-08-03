import sys
from time import sleep
from os import system

system('clear')

with open('/Users/jacobbarrow/Desktop/Code/Scrabble/dictionary.txt', 'r') as thefile:
	all_words = thefile.read().split()

all_words = dict([(word, 1) for word in all_words])


reset = 1
while reset == 1:
	system('clear')

	print("At any time, press '1' to end the program")
	inp = raw_input("Enter a word: ")

	if inp in all_words:
		print("Word allowed")
		sleep(4)

	elif inp == "1":
		print("Goodbye")
		sleep(2)
		reset = 2

	else:
		print("Word not allowed")
		sleep(3)
sys.exit()
