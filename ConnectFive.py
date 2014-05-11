__author__ = 'anthonylim'

# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 5
#

def main():
    playerX = True
    playerO = False

    # Create the board
    columns = 9
    rows = 7
    myboard = [["_"]*columns for x in xrange(rows)]
    # for i in myboard:
    #     print ' '.join(i)

    print_board(myboard)

    while True:
        if playerX:
            playerX_input = raw_input("Player X - Choose a column: ")
            if 0 > int(playerX_input) > 8:
                raise ValueError("Input must be between integers 0 and 8")
            else:
                place_piece("x", myboard, int(playerX_input))
                scan_board(myboard)
                print_board(myboard)
                playerX = False
                playerO = True
        if playerO:
            playerO_input = raw_input("Player O - Choose a column: ")
            if 0 > int(playerO_input) > 8:
                raise ValueError("Input must be between integers 0 and 8")
            else:
                place_piece("o", myboard, int(playerO_input))
                scan_board(myboard)
                print_board(myboard)
                playerX = True
                playerO = False

def print_board(board):
    # print top row
    for i in range(9):
        print "{0}".format(i),

    print("")

    # print the rest
    for x in range(7):
        for y in range(9):
            print board[x][y],
        print("")

# Goes from bottom up of the board
def place_piece(piece, board, column):
    for i in range(len(board)-1, -1, -1):
        if board[i][column] == "_":
            board[i][column] = piece
            break

    return board

def scan_board(board):
    # Horizontal
    for row in board:
        print row
        itor = 0
        prev = ''
        for val in row:
            prev = val
            
            print val

    # Vertical

    # Diagonal Right

    # Diagonal Left
    return

main()


