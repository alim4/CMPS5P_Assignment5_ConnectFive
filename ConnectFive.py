import sys

__author__ = 'anthonylim'

# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 5
#

def main():

    """
    Main

    """
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
    """

    :param player: x or o player
    :param num_tries: number of times to try input
    :return: input string
    """
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
    """

    :param board: the connect five board
    """
    print ("")
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
    """

    :param piece: x or o player
    :param board: the connect five board 2D array
    :param column: column the player will be placing into
    :return: the connect five board
    """
    for i in range(len(board)-1, -1, -1):
        if board[i][column] == "_":
            board[i][column] = piece
            break

    return board

def scan_board(board):
    """

    :param board:
    :return: nothing
    This function scans the board and calls win_game
    if a correct match is found
    """

    emptyfound = 0
    for ele in board:
        if ele.count("_") == 0:
            emptyfound += 1

    if emptyfound == 7:
        win_game("NOBODY")

    letters = ["x", "o"]

    # For X and O
    for letter in letters:
        # Horizontal
        #print "Row"
        for row in board:
            if row.count(letter) >= 5:
                if check(row, letter):
                    win_game(letter)
            #print "{0} ~ {1}".format(row, row.count("x"))

        # Vertical
        #print "Column"
        for column in range(len(board)):
            col = [row[column] for row in board]
            if col.count(letter) >= 5:
                if check(col, letter):
                    win_game(letter)
            #print "{0} ~ {1}".format(col, col.count("x"))

    newboard = []

    # Diagonal Right
    # Debugging
    # for i in range(7):
    #     for j in range(9):
    #         for k in range(18):
    #             if i == j-9+k:
    #                 board[i][j] = (chr(j+110-i)).upper()

    for j in range(1,18):
        diag = [row[(i+j)-9] for i, row in enumerate(board) if 0 <= i+j-9 < len(row)]
        newboard.append(diag)

    # Diagonal Left
    # Debugging
    # for i in range(7):
    #     for j in range(9):
    #         for k in range(18):
    #             if i == j-9+k:
    #                 try:
    #                     board[i][8-j] = (chr(j+110-i)).upper()
    #                 except IndexError:
    #                     print "eh"

    for j in range(1,18):
        diag = [row[-i-j+18] for i, row in enumerate(board) if 0 <= -i-j+18 < len(row)]
        newboard.append(diag)

    # Process diagonals
    for ele in newboard:
        if len(ele) >= 5:
            if check(ele, "x"):
                win_game("X")
            if check(ele, "o"):
                win_game("O")

    print_board(board)

    return

def win_game(player):
    """

    :param player: x or o player
    win the game
    """
    print "Player {0} has won the game!".format(player.upper())
    sys.exit(0)

def check(row, letter):
    # if itor is 5 for 5 consecutive
    # consider a successful match
    """

    :param row: list of characters to check
    :param letter: x or o player
    :return: boolean True or False
    checks a row of at least length 5 for a connect five match
    """
    itor = 0
    is_winner_found = False

    if len(row)-5 == 0:
        rangenum = 1
    else:
        rangenum = len(row)-5

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


