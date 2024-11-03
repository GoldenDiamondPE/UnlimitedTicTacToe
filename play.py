from boards import board, board2, board3, board4, board5, board6, board7, board8, board9
import display
import tileControl
import globalVars

def playGame():
    globalVars.gameBoardPlaying
    while globalVars.gameWon == False:
        if globalVars.gameWon == False and globalVars.playerTurn == True: # While No Winner
            tileControl.boardStartX()
            tileControl.wonX()
            tileControl.endGameX()
            display.gameBoard()
            globalVars.turnCount =globalVars.turnCount+1
            globalVars.playerTurn=False
            print(f"X JUST PLACED IN SECTION AT POINT {globalVars.position}")

        if globalVars.gameWon == False and globalVars.playerTurn == False:
            tileControl.boardStartO()
            tileControl.wonO()
            tileControl.endGameO()
            display.gameBoard()
            globalVars.turnCount =globalVars.turnCount+1
            globalVars.playerTurn=True
            print(f"O JUST PLACED IN SECTION AT POINT {globalVars.position}")