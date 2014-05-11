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

    myboard = [["_"]*9 for x in xrange(7)]
    for i in myboard:
        print ' '.join(i)

    myboard[2][3] = "adf"

    print len(myboard)
    print_board(myboard)

    while True:
        if playerX:
            playerX_input = raw_input("Player X - Choose a column: ")
            playerX = False
            playerO = True
        if playerO:
            playerO_input = raw_input("Player O - Choose a column: ")
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

def place_piece(board, column):
    return

main()


