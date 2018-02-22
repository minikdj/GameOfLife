import time
import os
from random import *

# O for alive, blank area for dead
board = [['O' for x in range(20)] for y in range(10)]

#clearing the terminal beforehand so everything prints evenly
os.system('clear')
for i in range(50):
	for x in range(len(board)):
		for y in range(len(board[x])):
			if(randint(1,6) == 1):
				board[x][y] = 'O'
			else:
				board[x][y] = ''
			print(board[x][y], end=' ')
		print('\n')

	time.sleep(1)
	os.system('clear')

