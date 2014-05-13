import sys

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
            playerX_input = get_input("X", 10)
            if playerX_input == "skip":
                playerX = False
                playerO = True
            else:
                place_piece("x", myboard, int(playerX_input))
                print_board(myboard)
                scan_board(myboard)
                playerX = False
                playerO = True
        if playerO:
            playerO_input = get_input("O", 10)
            if playerX_input == "skip":
                playerX = True
                playerO = False
            else:
                place_piece("o", myboard, int(playerO_input))
                print_board(myboard)
                scan_board(myboard)
                playerX = True
                playerO = False

def get_input(player, num_tries):
    itor = 0
    while itor < num_tries:
        input = raw_input("Player {0} - Choose a column: ".format(player))
        if not input.isdigit():
            itor += 1
            print "Bad input. Try again."
            continue
        if int(input) in range(9):
            return input
        else:
            print "Bad input. Try again."
            itor += 1

    # if player tries too many times, skip turn
    print "PLAYER {0}'s TURN SKIPPED".format(player)
    return "skip"

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
    letters = ["x", "o"]

    # For X and O
    for letter in letters:
        # Horizontal
        #print "Row"
        for row in board:
            if row.count(letter) >= 5:
                if check("row", row, letter):
                    win_game(letter)
            #print "{0} ~ {1}".format(row, row.count("x"))

        # Vertical
        #print "Column"
        for column in range(len(board)):
            col = [row[column] for row in board]
            if col.count(letter) >= 5:
                if check("col", col, letter):
                    win_game(letter)
            #print "{0} ~ {1}".format(col, col.count("x"))

    # Diagonal Right
    for i in range(7):
        for j in range(9):
            for k in range(18):
                if j == i-9+k:
                    board[i][j] = chr(j+100).upper()


    print print_board(board)


    # col[0][0]
    # col[0][1] [1][0]
    # col[0][2] [1][1] [2][0]
    # col[0][3] [1][2] [2][1] [3][0]

    # Diagonal Left
    return

def win_game(player):
    print "Player {0} has won the game!".format(player.upper())
    sys.exit(0)

def check(type, row, letter):
    # if itor is 5 for 5 consecutive
    # consider a successful match
    itor = 0
    is_winner_found = False

    if type == "row":
        rangenum = 4
    elif type == "col":
        rangenum = 3

    for i in range(rangenum):
        for j in range(5):
            if row[i+j] != letter:
                is_winner_found = False
                break
            else:
                is_winner_found = True
            if j == 4 and is_winner_found:
                return True

    return False

main()


