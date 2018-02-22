import time
import os

board = [[0 for x in range(20)] for y in range(20)]

for x in range(len(board)):
	for y in range(len(board)):
		print(board[x][y], end=' ')
	print('\n')
time.sleep(5)
os.system('clear')
print('hello')
