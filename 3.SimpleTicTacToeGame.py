theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}        #dict defines the board

def printBoard(board):        #func prints out the board
    print(board['top-L'] + '|'+ board['top-M']+ '|'+ board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+ board['mid-M']+ '|'+ board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|'+ board['low-M']+ '|'+ board['low-R'])
    
turn= 'X'     #starts on X’s turn
for i in range(9):    #limited to 9 coz only 9 spaces on board
    printBoard(theBoard) #prints the board
    #print('Now it is '+turn+"'s turn. Which space?") #self-explan
    move=input('Now it is '+turn+"'s turn. Which space?") #input move(must use same names as theBoard)
    theBoard[move] = turn #edits theBoard to store the turn just played
    if turn == 'X':    #swaps turn from X to O
        turn ='O'
    else:        #swaps turn from O to X
        turn = 'X'

printBoard(theBoard)
