'''

 | |
-----
 | |       Mijn awesome grid.
-----
 | |

'''
import random

def drawBoard(board):

    print("          "+ board[0] + "|" + board[1] + "|" + board[2])
    print("          "+ "-----")
    print("          "+ board[3] + "|" + board[4] + "|" + board[5])
    print("          "+ "-----")
    print("          "+ board[6] + "|" + board[7] + "|" + board[8])

def getPlayerMove():

    move = 0
    while (move < 1 or move > 9 or isSpaceFree(board, move-1) == False):
        print("\n""Give a number between 1-9")
        move = int(input())

    move -= 1
    
    return move

def getComputerMove():

    cmove = random.randint(1,9)
    while (isSpaceFree(board, cmove-1) == False):
        print("Computer is playing..", cmove)
        cmove = random.randint(1,9)

    cmove -= 1
    
    return cmove



def isSpaceFree(board, spot):
    if board[spot] == " ":
        return True
    else:
        return False

def isWinner(board, icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon
        or board[3] == icon and board[4] == icon and board[5] == icon
        or board[6] == icon and board[7] == icon and board[8] == icon
        or board[0] == icon and board[4] == icon and board[8] == icon
        or board[2] == icon and board[4] == icon and board[6] == icon
        or board[0] == icon and board[3] == icon and board[6] == icon
        or board[1] == icon and board[4] == icon and board[7] == icon
        or board[2] == icon and board[5] == icon and board[8] == icon):
        return True
    else:
        return False

board = [" "," "," "," "," "," "," "," "," ",]

isPlaying = True
playerIcon = "X"
computerIcon = "O"
turn = "computer"

def isBoardFull(board):
    for i in range(1, 9):
        if isSpaceFree(board, i):
            return False
    return True

while isPlaying:
    
    if turn == "player":
        drawBoard(board)
        move = getPlayerMove()
        board[move] = playerIcon

        if (isWinner(board, playerIcon) == True):
            drawBoard(board)
            print("You have won! You are amazing!")
            isPlaying = False
        else:
            if isBoardFull(board):
                drawBoard(board)
                print("You have ended in a tie! Mehh..")
                break
            else:
                turn = "computer"

    elif turn == "computer":
        move = getComputerMove()
        board[move] = computerIcon

        if (isWinner(board, computerIcon) == True):
            drawBoard(board)
            print("You have lost! Loser..")
            isPlaying = False
        else:
            if isBoardFull(board):
                drawBoard(board)
                print("You have ended in a tie! Mehh..")
                break
            else:
                turn = "player"
        
        


