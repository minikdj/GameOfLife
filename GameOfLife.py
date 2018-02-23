import time
import os
from random import *

extinct = False

# O for alive, blank area for dead
#board that is being printed and used to compare for the next generation
board = [['O' for x in range(20)] for y in range(10)]

#where the new values go for the new generation
new_board = [['' for x in range(20)] for y in range(10)]

def initialize_board():
	for x in range(len(board)):
		for y in range(len(board[x])):
			if randint(1,5) == 1:
				board[x][y] = 'O'
			else:
				board[x][y] = ''

def draw_board():
	#clearing the terminal beforehand so everything prints evenly
	os.system('clear')
	for x in range(len(board)):
		for y in range(len(board[x])):
			print(board[x][y], end=' ')
		print('\n')

def check_top_left():
	count = 0

def check_top_right():
	count = 0

def check_bottom_left():
	count = 0

def check_bottom_right():
	count = 0

def check_top():
	check_top_left()
	check_top_right()
	
def check_left():

def check_right():

def check_bottom():
	check_bottom_left()
	check_bottom_right()

def check_border():
	check_top()
	check_left()
	check_right()
	check_bottom()

def check_middle():

def update_board():
	check_border()
	check_middle()	


initialize_board()

while extinct == False:
	draw_board()
	update_board()
	check_extinct()
