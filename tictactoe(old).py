import random
import sys

theBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ','5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):  # prints the board
    screenWhipe()
    print()
    print()
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('-- --- --')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('-- --- --')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print()
    print()


def resetBoard():
    global theBoard
    theBoardCopy = {'7': ' ', '8': ' ', '9': ' ', '4': ' ',
                    '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
    theBoard.update(theBoardCopy)


def screenWhipe():
    clear = "\n" * 100
    print(clear)


# what happenes when its the players turn
def playerTurn(player):
    while True:
        playerPos = input('your turn: ')
        # validating input
        if playerPos in theBoard and theBoard[playerPos] == ' ':
            # updating the board with the player's input
            theBoard[playerPos] = player
            return
        else:
            print('invalid input, try again!')


# what happens when it is the opponents turn
def enemyTurn(enemy):
    potentialPos = None
    while True:
        # getting a random board position
        potentialPos = random.choice(list(theBoard.keys()))
        # checking that the position is valid
        if potentialPos != None and theBoard[potentialPos] == ' ':
            # updating the valid position in the board with the enemies Char
            theBoard[potentialPos] = enemy
            return

# ask the player if they want to play first or second.


def startingPlayer():
    while True:
        firstTurn = input('Would you like to take the first turn? (y/n): ')
        firstTurn = firstTurn.lower()
        if firstTurn == 'y':
            return True
        elif firstTurn == 'n':
            return False
        else:
            print('invalid input!')


def checkWinning(player, enemy):
    # convert the board dictionary to a list
    boardList = list(theBoard.items())
    checkRow(boardList, player, enemy)
    checkColumn(boardList, player, enemy)
    checkDiagonal(boardList, player, enemy)


def checkRow(boardList, player, enemy):
    # checking rows
    for i in range(0, 9, 3):
        row = boardList[i:i + 3]  # seperate the list into rows
        # create a sanitized list of rows (aka only keep the "values")
        sRow = []
        for j in range(0, 3):  # remove the "key" from the list
            x = row[j][1]
            sRow.append(x)

        checkIfWon(sRow, player, enemy)
        sRow.clear()  # reset the list so we can use it in the next row


def checkColumn(boardList, player, enemy):
    # checking columns
    for i in range(0, 3):
        column = boardList[i] + boardList[i + 3] + \
            boardList[i + 6]  # seperate the list into columns
        sCol = []
        for j in range(1, 7, 2):  # remove the "key" from the list
            x = column[j]
            sCol.append(x)
        checkIfWon(sCol, player, enemy)
        sCol.clear()


def checkDiagonal(boardList, player, enemy):
    topLeft = boardList[0][1] + boardList[4][1] + boardList[8][1]
    topRight = boardList[2][1] + boardList[4][1] + boardList[6][1]
    checkIfWon(topLeft, player, enemy)
    checkIfWon(topRight, player, enemy)

# checks if a line has 3 of the same char in a row


def checkIfWon(line, player, enemy):
    if ' ' in line:  # checking if the row has any empty square
        return
    if player in line and enemy in line:  # checking if both players have a square in the row
        return
    if player in line:  # if true, player has won
        # if the player wins, update the board here so that the opponent does not make their turn
        printBoard(theBoard)
        endGame(1)
    if enemy in line:  # if true, opponent has won
        # if the opponent wins, update the bord so that the player does not make their turn
        endGame(2)


def checkIfDraw(playerStart):
    boardState = ''
    boardState = boardState.join(theBoard.values())
    if len(boardState) != 0:
        if ' ' not in boardState:
            # If here, the board is full, it is eather a draw or a player has won, så checkifwon before checkifdraw.
            if playerStart:
                printBoard(theBoard)
            print('The game is a draw.')
            replay()


def replay():
    while True:
        again = input('Do you want to play again?: (y/n)')
        again = again.lower()
        if again == 'n':
            sys.exit(0)
        if again == 'y':
            screenWhipe()
            resetBoard()
            main()

        else:
            print('invalid input, try again!')


# ends the game if a player has won
def endGame(winner):
    if winner == 1:
        print('You won')
        replay()
    if winner == 2:
        print('you lost')
        replay()


def main():
    screenWhipe()
    turn = startingPlayer()  # initialising who should start.
    # set player and opponent icon
    if turn == True:
        player = 'X'
        enemy = 'O'
    else:
        player = 'O'
        enemy = 'X'

    if turn == True:
        # print a blank board if the player wants to start.
        printBoard(theBoard)

    # check who goes first. check if anyone won. let both players make their move as long as the opponent has not won.
    while turn == True:
        if turn == True:
            playerTurn(player)
            checkWinning(player, enemy)
            checkIfDraw(turn)
            enemyTurn(enemy)
            printBoard(theBoard)
            checkWinning(player, enemy)
    while turn == False:
        if turn == False:
            enemyTurn(enemy)
            printBoard(theBoard)
            checkWinning(player, enemy)
            checkIfDraw(turn)
            playerTurn(player)
            checkWinning(player, enemy)


main()
