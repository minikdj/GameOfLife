import time
import os
from random import *

extinct = False

# O for alive, blank area for dead
#board that is being printed and used to compare for the next generation
board = [['O' for x in range(30)] for y in range(20)]

#where the new values go for the new generation
new_board = list(board)

def initialize_board():
	for x in range(len(board)):
		for y in range(len(board[x])):
			if randint(1,2) == 1:
				board[x][y] = 'O'
			else:
				board[x][y] = ' '

def draw_board():
	#clearing the terminal beforehand so everything prints evenly
	os.system('clear')
	for x in range(len(board)):
		for y in range(len(board[x])):
			print(board[x][y], end=' ')
		print('\n')

def check_top_left():
	count = 0
	
	if board[0][1] == 'O':
		count += 1
	if board[1][1] == 'O':
		count += 1
	if board[1][0] == 'O':
		count += 1
	
	if board[0][0] == 'O':
		if count < 2:
			new_board[0][0] = ' '
		else:
			new_board[0][0] = 'O'
	else:
		if count == 3:
			new_board[0][0] = 'O'
		else:
			new_board[0][0] = ' '
def check_top_right():
	count = 0

	if board[0][len(board[0]) - 2] == 'O':
		count += 1
	if board[1][len(board[0]) - 2] == 'O':
		count += 1
	if board[1][len(board[0]) - 1] == 'O':
		count += 1
	
	if board[0][len(board[0]) - 1] == 'O':
		if count < 2:
			new_board[0][len(board[0]) - 1] = ' '
		else:
			new_board[0][len(board[0]) - 1] = 'O'
	else:
		if count == 3:
			new_board[0][len(board[0]) - 1] = 'O'
		else:
			new_board[0][len(board[0]) - 1] = ' '
def check_top_middle():
	for i in range(1,len(board[0]) - 1):
		count = 0

		if board[0][i - 1] == 'O':
			count += 1
		if board[1][i - 1] == 'O':
			count += 1
		if board[1][i] == 'O':
			count
		if board[1][i + 1] == 'O':
			count += 1
		if board[0][i + 1] == 'O':
			count += 1
		
		if board[0][i] == 'O':
			if count < 2:
				new_board[0][i] = ' '
			elif count > 3:
				new_board[0][i] = ' '
			else:
				new_board[0][i] = 'O'
		else:
			if count == 3:
				new_board[0][i] = 'O'
			else:
				new_board[0][i] = ' '

def check_bottom_left():
	count = 0
	
	if board[len(board) - 1][1] == 'O':
		count += 1
	if board[len(board) - 2][1] == 'O':
		count += 1
	if board[len(board) - 2][0] == 'O':
		count += 1

	if board[len(board) - 1][0] == 'O':
		if count < 2:
			new_board[len(board) - 1][0] = ' '
		else:
			new_board[len(board) - 1][0] = 'O'
	else:
		if count == 3:
			new_board[len(board) - 1][0] = 'O'
		else:
			new_board[len(board) - 1][0] = ' '	

def check_bottom_right():
	count = 0

	if board[len(board) - 1][len(board[0]) - 2] == 'O':
		count += 1
	if board[len(board) - 2][len(board[0]) - 2] == 'O':
		count += 1
	if board[len(board) - 2][len(board[0]) - 1] == 'O':
		count += 1

	if board[len(board) - 1][len(board[0]) - 1] == 'O':
		if count < 2:
			new_board[len(board) - 1][len(board[0]) - 1] = ' '
		else:
			new_board[len(board) - 1][len(board[0]) - 1] = 'O'
	else:
		if count == 3:
			new_board[len(board) - 1][len(board[0]) - 1] = 'O'
		else:
			new_board[len(board) - 1][len(board[0]) - 1] = ' '

def check_bottom_middle():
	
	for i in range(1, len(board[0]) - 1):
		count = 0		

		if board[len(board) - 1][i - 1] == 'O':
			count += 1
		if board[len(board) - 2][i - 1] == 'O':
			count += 1
		if board[len(board) - 2][i] == 'O':
			count += 1
		if board[len(board) - 2][i + 1] == 'O':
			count += 1
		if board[len(board) - 1][i + 1] == 'O':
			count += 1
	
		if board[len(board) - 1][i] == 'O':
			if count < 2:
				new_board[len(board) - 1][i] = ' '
			elif count > 3:
				new_board[len(board) - 1][i] = ' '
			else:
				new_board[len(board) - 1][i] = 'O'
		else:
			if count == 3:
				new_board[len(board) - 1][i] = 'O'
			else:
				new_board[len(board) - 1][i] = ' ' 	

def check_top():
	check_top_left()
	check_top_right()
	check_top_middle()

def check_left():
	
	for i in range(1, len(board) - 1):
		count = 0
	
		if board[i - 1][0] == 'O':
			count += 1
		if board[i - 1][1] == 'O':
			count += 1
		if board[i][1] == 'O':
			count += 1
		if board[i + 1][1] == 'O':
			count += 1
		if board[i + 1][0] == 'O':
			count += 1
		
		if board[i][0] == 'O':
			if count < 2:
				new_board[i][0] = ' '
			elif count > 3:
				new_board[i][0] = ' '
			else:
				new_board[i][0] = 'O'
		else:
			if count == 3:
				new_board[i][0] = 'O'
			else:
				new_board[i][0] = ' '
	

def check_right():
	
	for i in range(1, len(board) - 1):
		count = 0

		if board[i - 1][len(board[i]) - 1] == 'O':
			count += 1
		if board[i - 1][len(board[i]) - 2] == 'O':
			count += 1
		if board[i][len(board[i]) - 2] == 'O':
			count += 1
		if board[i + 1][len(board[i]) - 2] == 'O':
			count += 1
		if board[i + 1][len(board[i]) - 1] == 'O':
			count += 1
		
		if board[i][len(board[i]) - 1] == 'O':
			if count < 2:
				new_board[i][len(board[i]) - 1] = ' '
			elif count > 3:
				new_board[i][len(board[i]) - 1] = ' '
			else:
				new_board[i][len(board[i]) - 1] = 'O'
		else:
			if count == 3:
				new_board[i][len(board[i]) - 1] = 'O'
			else:
				new_board[i][len(board[i]) - 1] = ' '


def check_bottom():
	check_bottom_left()
	check_bottom_right()
	check_bottom_middle()
	
def check_border():
	check_top()
	check_left()
	check_right()
	check_bottom()

def check_middle():

	for i in range(1, len(board) - 1):
		for j in range(1, len(board[0]) - 1):
			count = 0
			
			if board[i - 1][j - 1] == 'O':
				count += 1
			if board[i - 1][j] == 'O':
				count += 1
			if board[i - 1][j + 1] == 'O':
				count += 1
			if board[i][j - 1] == 'O':
				count += 1
			if board[i][j + 1] == 'O':
				count += 1
			if board[i + 1][j - 1] == 'O':
				count += 1
			if board[i + 1][j] == 'O':
				count += 1
			if board[i + 1][j + 1] == 'O':
				count += 1

			if board[i][j] == 'O':
				if count < 2:
					new_board[i][j] = ' '
				elif count > 3:
					new_board[i][j] = ' '
				else:
					new_board[i][j] = 'O'
			else:
				if count == 3:
					new_board[i][j] = 'O'
				else:
					new_board[i][j] = ' '

def update_board():
	check_border()
	check_middle()	

def check_extinct():
	global extinct
	not_extinct = False
	for i in range(0, len(board)):
		if not_extinct == True:
			break
		for j in range(0, len(board[i])):
			if board[i][j] == 'O':
				extinct = False
				not_extinct = True			
	

initialize_board()

while extinct == False:
	draw_board()
	update_board()
	check_extinct()
	board = list(new_board)
	time.sleep(0.1)
