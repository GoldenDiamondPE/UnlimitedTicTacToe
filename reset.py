import boards
import globalVars

def resets():
    globalVars.gameWon = False
    globalVars.playerTurn = True #Determines Who Turn It Is
    globalVars.turnCount = 0
    globalVars.gameBoardPlaying = int(input("What Board Would You Like To Start On (1-9): "))
    globalVars.position = 0

    globalVars.boardComp = globalVars.board2Comp = globalVars.board9Comp = globalVars.board3Comp = globalVars.board4Comp = globalVars.board5Comp = globalVars.board6Comp = globalVars.board7Comp = globalVars.board8Comp = globalVars.board9Comp = "Not Filled"

    boards.board = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
}
    boards.board2 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board3 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board4 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board5 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board6 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board7 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board8 = {
        'a': '   ',
        'b': '   ',
        'c': '   ',
        'd': '   ',
        'e': '   ',
        'f': '   ',
        'g': '   ',
        'h': '   ',
        'i': '   ',
    }
    boards.board9 = {
    'a': '   ',
    'b': '   ',
    'c': '   ',
    'd': '   ',
    'e': '   ',
    'f': '   ',
    'g': '   ',
    'h': '   ',
    'i': '   ',
}