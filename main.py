from boards import board, board2, board3, board4, board5, board6, board7, board8, board9
import display
import tileControl
import play
import reset
import globalVars

playingGame=True

if __name__ == '__main__':
    print("Hello and Welcome to Unlimited Tic Tac Toe By Brandon Bula!\n")
    print("The game follows the rules of Ultimate Tic Tac Toe with some slight alterations.\nTry and get as far as you can!")
    
    globalVars.gameBoardPlaying = int(input("What Board Would You Like To Start On (1-9): "))
    
    while playingGame==True:
        if globalVars.gameWon == False:
            play.playGame()
        if globalVars.gameWon == True:
            globalVars.gamesWon+=1
            print(f"\nThats The Game! You finished in: {globalVars.turnCount} Turns!")
            print(f"You Won {globalVars.gamesWon} Game(s) So Far, Keep It Up!\n")
            keepGoing = input("Would You Like To Keep Going (Y/N): ")
            if keepGoing == "Y":
                reset.resets()
            else:
                playingGame = False

