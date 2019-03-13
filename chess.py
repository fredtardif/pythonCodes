
def initializeBoard():

	board = [['_' for _ in range(8)] for _ in range(8)]
	board[0] = [piece for piece in 'rnbqkbnr']	# black pieces
	board[1] = ['p' for _ in range(8)]	# black pawns
	board[6] = ['P' for _ in range(8)]	# white pawns
	board[7] = [piece for piece in 'rnbqkbnr'.upper()]	# white pieces

	return board


def printBoard(board,alpha):
	''' Function that prints the current board'''
	if alpha: print('  ',end='')
	print(' _ _ _ _ _ _ _ _ ')
	for i in range(len(board)):
		if alpha: print(8-i,end=' ')
		print('|',end='')
		for square in board[i]:
			print(square,end='|')
		print('')
	if alpha: print('   a b c d e f g h')



if __name__=='__main__':

	board=initializeBoard()

	ans=''
	while ans!='y' and ans!='n':
		ans=input('Chess! Do you want alphanumerical help on the board? (y/n) ')
	if ans=='y': alpha=True
	else: alpha = False

	win=False
	while not win:
		printBoard(board,alpha)
		whiteMove=input('\nWhite to move: ')
		printBoard(board,alpha)
		blackMove=input('\nBlack to move: ')