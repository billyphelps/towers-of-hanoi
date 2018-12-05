game = [[],[],[]];

def createGame(numBlocks):
	return [list(range(numBlocks,0,-1)),[],[]]

def moveTower(source_pile,dest_pile,other_pile,num_of_blocks):
	if(num_of_blocks == 1):
		moveBlock(source_pile,dest_pile)
	else:
		moveTower(source_pile,other_pile,dest_pile,num_of_blocks-1)
		moveBlock(source_pile,dest_pile)
		moveTower(other_pile,dest_pile,source_pile,num_of_blocks-1)

def moveBlock(source_pile,dest_pile):
	game[dest_pile].append(game[source_pile].pop())
	print(game)

def solveGame(dest_pile):
	piles = [1,2]
	piles.remove(dest_pile)
	moveTower(0,dest_pile,piles[0],len(game[0]))

game = createGame(5)
print(game)
solveGame(2)




