from boards import board, board2, board3, board4, board5, board6, board7, board8, board9
import display
import main
import globalVars

def placeX1():
    print("CURRENT SECTION IS 1")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board["a"]== "   ":
        board["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board["b"]== "   ":
        board["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board["c"]== "   ":
        board["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board["d"]== "   ":
        board["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board["e"]== "   ":
        board["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board["f"]== "   ":
        board["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board["g"]== "   ":
        board["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board["h"]== "   ":
        board["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board["i"]== "   ":
        board["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.boardComp == "DoneX" or globalVars.boardComp == "Done)": 
        globalVars.gameBoardPlaying
    elif globalVars.boardComp == "DoneX" or globalVars.boardComp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX1()

def placeX2():
    print("CURRENT SECTION IS 2")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board2["a"]== "   ":
        board2["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board2["b"]== "   ":
        board2["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board2["c"]== "   ":
        board2["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board2["d"]== "   ":
        board2["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board2["e"]== "   ":
        board2["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board2["f"]== "   ":
        board2["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board2["g"]== "   ":
        board2["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board2["h"]== "   ":
        board2["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board2["i"]== "   ":
        board2["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board2Comp == "DoneX" or globalVars.board2Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX2()

def placeX3():
    print("CURRENT SECTION IS 3")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board3["a"]== "   ":
        board3["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board3["b"]== "   ":
        board3["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board3["c"]== "   ":
        board3["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board3["d"]== "   ":
        board3["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board3["e"]== "   ":
        board3["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board3["f"]== "   ":
        board3["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board3["g"]== "   ":
        board3["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board3["h"]== "   ":
        board3["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board3["i"]== "   ":
        board3["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board3Comp == "DoneX" or globalVars.board3Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX3()

def placeX4():
    print("CURRENT SECTION IS 4")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board4["a"]== "   ":
        board4["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board4["b"]== "   ":
        board4["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board4["c"]== "   ":
        board4["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board4["d"]== "   ":
        board4["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board4["e"]== "   ":
        board4["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board4["f"]== "   ":
        board4["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board4["g"]== "   ":
        board4["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board4["h"]== "   ":
        board4["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board4["i"]== "   ":
        board4["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board4Comp == "DoneX" or globalVars.board4Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX4()

def placeX5():
    print("CURRENT SECTION IS 5")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board5["a"]== "   ":
        board5["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board5["b"]== "   ":
        board5["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board5["c"]== "   ":
        board5["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board5["d"]== "   ":
        board5["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board5["e"]== "   ":
        board5["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board5["f"]== "   ":
        board5["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board5["g"]== "   ":
        board5["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board5["h"]== "   ":
        board5["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board5["i"]== "   ":
        board5["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board5Comp == "DoneX" or globalVars.board5Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX5()

def placeX6():
    print("CURRENT SECTION IS 6")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board6["a"]== "   ":
        board6["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board6["b"]== "   ":
        board6["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board6["c"]== "   ":
        board6["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board6["d"]== "   ":
        board6["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board6["e"]== "   ":
        board6["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board6["f"]== "   ":
        board6["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board6["g"]== "   ":
        board6["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board6["h"]== "   ":
        board6["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board6["i"]== "   ":
        board6["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board6Comp == "DoneX" or globalVars.board6Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX6()

def placeX7():
    print("CURRENT SECTION IS 7")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board7["a"]== "   ":
        board7["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board7["b"]== "   ":
        board7["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board7["c"]== "   ":
        board7["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board7["d"]== "   ":
        board7["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board7["e"]== "   ":
        board7["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board7["f"]== "   ":
        board7["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board7["g"]== "   ":
        board7["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board7["h"]== "   ":
        board7["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board7["i"]== "   ":
        board7["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board7Comp == "DoneX" or globalVars.board7Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX7()

def placeX8():
    print("CURRENT SECTION IS 8")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board8["a"]== "   ":
        board8["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board8["b"]== "   ":
        board8["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board8["c"]== "   ":
        board8["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board8["d"]== "   ":
        board8["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board8["e"]== "   ":
        board8["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board8["f"]== "   ":
        board8["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board8["g"]== "   ":
        board8["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board8["h"]== "   ":
        board8["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board8["i"]== "   ":
        board8["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board8Comp == "DoneX" or globalVars.board8Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX8()      

def placeX9():
    print("CURRENT SECTION IS 9")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board9["a"]== "   ":
        board9["a"]=" X "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board9["b"]== "   ":
        board9["b"]=" X "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board9["c"]== "   ":
        board9["c"]=" X "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board9["d"]== "   ":
        board9["d"]=" X "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board9["e"]== "   ":
        board9["e"]=" X "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board9["f"]== "   ":
        board9["f"]=" X "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board9["g"]== "   ":
        board9["g"]=" X "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board9["h"]== "   ":
        board9["h"]=" X "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board9["i"]== "   ":
        board9["i"]=" X "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board9Comp == "DoneX" or globalVars.board9Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartX()
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeX9()


def placeO1():
    print("CURRENT SECTION IS 1")
    print(f"{globalVars.boardComp} BOARD 1")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board["a"]== "   ":
        board["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board["b"]== "   ":
        board["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board["c"]== "   ":
        board["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board["d"]== "   ":
        board["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board["e"]== "   ":
        board["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board["f"]== "   ":
        board["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board["g"]== "   ":
        board["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board["h"]== "   ":
        board["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board["i"]== "   ":
        board["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.boardComp == "DoneX" or globalVars.boardComp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO()    
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO1()

def placeO2():
    print("CURRENT SECTION IS 2")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board2["a"]== "   ":
        board2["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board2["b"]== "   ":
        board2["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board2["c"]== "   ":
        board2["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board2["d"]== "   ":
        board2["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board2["e"]== "   ":
        board2["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board2["f"]== "   ":
        board2["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board2["g"]== "   ":
        board2["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board2["h"]== "   ":
        board2["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board2["i"]== "   ":
        board2["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board2Comp == "DoneX" or globalVars.board2Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO()    
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO2()

def placeO3():
    print("CURRENT SECTION IS 3")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board3["a"]== "   ":
        board3["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board3["b"]== "   ":
        board3["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board3["c"]== "   ":
        board3["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board3["d"]== "   ":
        board3["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board3["e"]== "   ":
        board3["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board3["f"]== "   ":
        board3["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board3["g"]== "   ":
        board3["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board3["h"]== "   ":
        board3["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board3["i"]== "   ":
        board3["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board3Comp == "DoneX" or globalVars.board3Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO3()

def placeO4():
    print("CURRENT SECTION IS 4")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board4["a"]== "   ":
        board4["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board4["b"]== "   ":
        board4["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board4["c"]== "   ":
        board4["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board4["d"]== "   ":
        board4["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board4["e"]== "   ":
        board4["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board4["f"]== "   ":
        board4["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board4["g"]== "   ":
        board4["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board4["h"]== "   ":
        board4["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board4["i"]== "   ":
        board4["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board4Comp == "DoneX" or globalVars.board4Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO4()

def placeO5():
    print("CURRENT SECTION IS 5")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board5["a"]== "   ":
        board5["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board5["b"]== "   ":
        board5["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board5["c"]== "   ":
        board5["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board5["d"]== "   ":
        board5["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board5["e"]== "   ":
        board5["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board5["f"]== "   ":
        board5["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board5["g"]== "   ":
        board5["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board5["h"]== "   ":
        board5["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board5["i"]== "   ":
        board5["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board5Comp == "DoneX" or globalVars.board5Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO5()

def placeO6():
    print("CURRENT SECTION IS 6")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board6["a"]== "   ":
        board6["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board6["b"]== "   ":
        board6["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board6["c"]== "   ":
        board6["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board6["d"]== "   ":
        board6["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board6["e"]== "   ":
        board6["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board6["f"]== "   ":
        board6["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board6["g"]== "   ":
        board6["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board6["h"]== "   ":
        board6["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board6["i"]== "   ":
        board6["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board6Comp == "DoneX" or globalVars.board6Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO6()

def placeO7():
    print("CURRENT SECTION IS 7")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board7["a"]== "   ":
        board7["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board7["b"]== "   ":
        board7["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board7["c"]== "   ":
        board7["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board7["d"]== "   ":
        board7["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board7["e"]== "   ":
        board7["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board7["f"]== "   ":
        board7["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board7["g"]== "   ":
        board7["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board7["h"]== "   ":
        board7["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board7["i"]== "   ":
        board7["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board7Comp == "DoneX" or globalVars.board7Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO7()

def placeO8():
    print("CURRENT SECTION IS 8")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board8["a"]== "   ":
        board8["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board8["b"]== "   ":
        board8["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board8["c"]== "   ":
        board8["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board8["d"]== "   ":
        board8["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board8["e"]== "   ":
        board8["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board8["f"]== "   ":
        board8["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board8["g"]== "   ":
        board8["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board8["h"]== "   ":
        board8["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board8["i"]== "   ":
        board8["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board8Comp == "DoneX" or globalVars.board8Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO8()

def placeO9():
    print("CURRENT SECTION IS 9")
    globalVars.position= int(input("\nWhere would you like to go (1-9): "))
    if globalVars.position==1 and board9["a"]== "   ":
        board9["a"]=" O "
        globalVars.gameBoardPlaying = 1
    elif globalVars.position==2 and board9["b"]== "   ":
        board9["b"]=" O "
        globalVars.gameBoardPlaying = 2
    elif globalVars.position==3 and board9["c"]== "   ":
        board9["c"]=" O "
        globalVars.gameBoardPlaying = 3
    elif globalVars.position==4 and board9["d"]== "   ":
        board9["d"]=" O "
        globalVars.gameBoardPlaying = 4
    elif globalVars.position==5 and board9["e"]== "   ":
        board9["e"]=" O "
        globalVars.gameBoardPlaying = 5
    elif globalVars.position==6 and board9["f"]== "   ":
        board9["f"]=" O "
        globalVars.gameBoardPlaying = 6
    elif globalVars.position==7 and board9["g"]== "   ":
        board9["g"]=" O "
        globalVars.gameBoardPlaying = 7
    elif globalVars.position==8 and board9["h"]== "   ":
        board9["h"]=" O "
        globalVars.gameBoardPlaying = 8
    elif globalVars.position==9 and board9["i"]== "   ":
        board9["i"]=" O "
        globalVars.gameBoardPlaying = 9
    elif globalVars.board9Comp == "DoneX" or globalVars.board9Comp == "DoneO": 
        globalVars.gameBoardPlaying = int(input("That Board Is Filled. What Board Would You Like To Go To Instead (1-9): "))
        boardStartO() 
    else:
        print("That Space Is Filled, Place In Different Spot!")
        placeO9()


def wonX():
        # Left and Right B1
        if (board["a"] == " X " and board["b"] == " X " and board["c"]== " X ") or (board["d"] == " X " and board["e"] == " X " and board["f"]== " X ") or (board["g"] == " X " and board["h"] == " X " and board["i"]== " X "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " X "
            globalVars.boardComp = "DoneX"
        # Up and Down B1
        elif (board["a"] == " X " and board["d"] == " X " and board["g"]== " X ") or (board["b"] == " X " and board["e"] == " X " and board["h"]== " X ") or (board["c"] == " X " and board["f"] == " X " and board["i"]== " X "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " X "
            globalVars.boardComp = "DoneX"
        # Diagonal B1
        elif (board["a"] == " X " and board["e"] == " X " and board["i"]== " X ") or (board["c"] == " X " and board["e"] == " X " and board["g"]== " X "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " X "
            globalVars.boardComp = "DoneX"


        # Left and Right B2
        if (board2["a"] == " X " and board2["b"] == " X " and board2["c"]== " X ") or (board2["d"] == " X " and board2["e"] == " X " and board2["f"]== " X ") or (board2["g"] == " X " and board2["h"] == " X " and board2["i"]== " X "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " X "
            globalVars.board2Comp = "DoneX"
        # Up and Down B2
        elif (board2["a"] == " X " and board2["d"] == " X " and board2["g"]== " X ") or (board2["b"] == " X " and board2["e"] == " X " and board2["h"]== " X ") or (board2["c"] == " X " and board2["f"] == " X " and board2["i"]== " X "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " X "
            globalVars.board2Comp = "DoneX"
        # Diagonal B2
        elif (board2["a"] == " X " and board2["e"] == " X " and board2["i"]== " X ") or (board2["c"] == " X " and board2["e"] == " X " and board2["g"]== " X "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " X "
            globalVars.board3Comp = "DoneX"


        # Left and Right B3
        if (board3["a"] == " X " and board3["b"] == " X " and board3["c"]== " X ") or (board3["d"] == " X " and board3["e"] == " X " and board3["f"]== " X ") or (board3["g"] == " X " and board3["h"] == " X " and board3["i"]== " X "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " X "
            globalVars.board3Comp = "DoneX"
        # Up and Down B3
        elif (board3["a"] == " X " and board3["d"] == " X " and board3["g"]== " X ") or (board3["b"] == " X " and board3["e"] == " X " and board3["h"]== " X ") or (board3["c"] == " X " and board3["f"] == " X " and board3["i"]== " X "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " X "
            globalVars.board3Comp = "DoneX"
        # Diagonal B3
        elif (board3["a"] == " X " and board3["e"] == " X " and board3["i"]== " X ") or (board3["c"] == " X " and board3["e"] == " X " and board3["g"]== " X "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " X "
            globalVars.board3Comp = "DoneX"


        # Left and Right B4
        if (board4["a"] == " X " and board4["b"] == " X " and board4["c"]== " X ") or (board4["d"] == " X " and board4["e"] == " X " and board4["f"]== " X ") or (board4["g"] == " X " and board4["h"] == " X " and board4["i"]== " X "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " X "
            globalVars.board4Comp = "DoneX"
        # Up and Down B4
        elif (board4["a"] == " X " and board4["d"] == " X " and board4["g"]== " X ") or (board4["b"] == " X " and board4["e"] == " X " and board4["h"]== " X ") or (board4["c"] == " X " and board4["f"] == " X " and board4["i"]== " X "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " X "
            globalVars.board4Comp = "DoneX"
        # Diagonal B4
        elif (board4["a"] == " X " and board4["e"] == " X " and board4["i"]== " X ") or (board4["c"] == " X " and board4["e"] == " X " and board4["g"]== " X "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " X "
            globalVars.board4Comp = "DoneX"


        # Left and Right B5
        if (board5["a"] == " X " and board5["b"] == " X " and board5["c"]== " X ") or (board5["d"] == " X " and board5["e"] == " X " and board5["f"]== " X ") or (board5["g"] == " X " and board5["h"] == " X " and board5["i"]== " X "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " X "
            globalVars.board5Comp = "DoneX"
        # Up and Down B5
        elif (board5["a"] == " X " and board5["d"] == " X " and board5["g"]== " X ") or (board5["b"] == " X " and board5["e"] == " X " and board5["h"]== " X ") or (board5["c"] == " X " and board5["f"] == " X " and board5["i"]== " X "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " X "
            globalVars.board5Comp = "DoneX"
        # Diagonal B5
        elif (board5["a"] == " X " and board5["e"] == " X " and board5["i"]== " X ") or (board5["c"] == " X " and board5["e"] == " X " and board5["g"]== " X "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " X "
            globalVars.board5Comp = "DoneX"


        # Left and Right B6
        if (board6["a"] == " X " and board6["b"] == " X " and board6["c"]== " X ") or (board6["d"] == " X " and board6["e"] == " X " and board6["f"]== " X ") or (board6["g"] == " X " and board6["h"] == " X " and board6["i"]== " X "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " X "
            globalVars.board6Comp = "DoneX"
        # Up and Down B6
        elif (board6["a"] == " X " and board6["d"] == " X " and board6["g"]== " X ") or (board6["b"] == " X " and board6["e"] == " X " and board6["h"]== " X ") or (board6["c"] == " X " and board6["f"] == " X " and board6["i"]== " X "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " X "
            globalVars.board6Comp = "DoneX"
        # Diagonal B6
        elif (board6["a"] == " X " and board6["e"] == " X " and board6["i"]== " X ") or (board6["c"] == " X " and board6["e"] == " X " and board6["g"]== " X "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " X "
            globalVars.board6Comp = "DoneX"


        # Left and Right B7
        if (board7["a"] == " X " and board7["b"] == " X " and board7["c"]== " X ") or (board7["d"] == " X " and board7["e"] == " X " and board7["f"]== " X ") or (board7["g"] == " X " and board7["h"] == " X " and board7["i"]== " X "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " X "
            globalVars.board7Comp = "DoneX"
        # Up and Down B7
        elif (board7["a"] == " X " and board7["d"] == " X " and board7["g"]== " X ") or (board7["b"] == " X " and board7["e"] == " X " and board7["h"]== " X ") or (board7["c"] == " X " and board7["f"] == " X " and board7["i"]== " X "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " X "
            globalVars.board7Comp = "DoneX"
        # Diagonal B7
        elif (board7["a"] == " X " and board7["e"] == " X " and board7["i"]== " X ") or (board7["c"] == " X " and board7["e"] == " X " and board7["g"]== " X "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " X "
            globalVars.board7Comp = "DoneX"


        # Left and Right B8
        if (board8["a"] == " X " and board8["b"] == " X " and board8["c"]== " X ") or (board8["d"] == " X " and board8["e"] == " X " and board8["f"]== " X ") or (board8["g"] == " X " and board8["h"] == " X " and board8["i"]== " X "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " X "
            globalVars.board8Comp = "DoneX"
        # Up and Down B8
        elif (board8["a"] == " X " and board8["d"] == " X " and board8["g"]== " X ") or (board8["b"] == " X " and board8["e"] == " X " and board8["h"]== " X ") or (board8["c"] == " X " and board8["f"] == " X " and board8["i"]== " X "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " X "
            globalVars.board8Comp = "DoneX"
        # Diagonal B8
        elif (board8["a"] == " X " and board8["e"] == " X " and board8["i"]== " X ") or (board8["c"] == " X " and board8["e"] == " X " and board8["g"]== " X "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " X "
            globalVars.board8Comp = "DoneX"

        # Left and Right B9
        if (board9["a"] == " X " and board9["b"] == " X " and board9["c"]== " X ") or (board9["d"] == " X " and board9["e"] == " X " and board9["f"]== " X ") or (board9["g"] == " X " and board9["h"] == " X " and board9["i"]== " X "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " X "
            globalVars.board9Comp = "DoneX"
        # Up and Down B9
        elif (board9["a"] == " X " and board9["d"] == " X " and board9["g"]== " X ") or (board9["b"] == " X " and board9["e"] == " X " and board9["h"]== " X ") or (board9["c"] == " X " and board9["f"] == " X " and board9["i"]== " X "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " X "
            globalVars.board9Comp = "DoneX"
        # Diagonal B9
        elif (board9["a"] == " X " and board9["e"] == " X " and board9["i"]== " X ") or (board9["c"] == " X " and board9["e"] == " X " and board9["g"]== " X "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " X "
            globalVars.board9Comp = "DoneX"

def wonO():
        # Left and Right B1
        if (board["a"] == " O " and board["b"] == " O " and board["c"]== " O ") or (board["d"] == " O " and board["e"] == " O " and board["f"]== " O ") or (board["g"] == " O " and board["h"] == " O " and board["i"]== " O "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " O "
            globalVars.boardComp = "DoneY"
        # Up and Down B1
        elif (board["a"] == " O " and board["d"] == " O " and board["g"]== " O ") or (board["b"] == " O " and board["e"] == " O " and board["h"]== " O ") or (board["c"] == " O " and board["f"] == " O " and board["i"]== " O "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " O "
            globalVars.boardComp = "DoneY"
        # Diagonal B1
        elif (board["a"] == " O " and board["e"] == " O " and board["i"]== " O ") or (board["c"] == " O " and board["e"] == " O " and board["g"]== " O "):
            board["a"] = board["b"] = board["c"] = board["d"] = board["e"] = board["f"] = board["g"] = board["h"] = board["i"] = " O "
            globalVars.boardComp = "DoneY"

        # Left and Right B2
        if (board2["a"] == " O " and board2["b"] == " O " and board2["c"]== " O ") or (board2["d"] == " O " and board2["e"] == " O " and board2["f"]== " O ") or (board2["g"] == " O " and board2["h"] == " O " and board2["i"]== " O "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " O "
            globalVars.board2Comp = "DoneY"
        # Up and Down B2
        elif (board2["a"] == " O " and board2["d"] == " O " and board2["g"]== " O ") or (board2["b"] == " O " and board2["e"] == " O " and board2["h"]== " O ") or (board2["c"] == " O " and board2["f"] == " O " and board2["i"]== " O "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " O "
            globalVars.board2Comp = "DoneY"
        # Diagonal B2
        elif (board2["a"] == " O " and board2["e"] == " O " and board2["i"]== " O ") or (board2["c"] == " O " and board2["e"] == " O " and board2["g"]== " O "):
            board2["a"] = board2["b"] = board2["c"] = board2["d"] = board2["e"] = board2["f"] = board2["g"] = board2["h"] = board2["i"] = " O "
            globalVars.board2Comp = "DoneY"


        # Left and Right B3
        if (board3["a"] == " O " and board3["b"] == " O " and board3["c"]== " O ") or (board3["d"] == " O " and board3["e"] == " O " and board3["f"]== " O ") or (board3["g"] == " O " and board3["h"] == " O " and board3["i"]== " O "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " O "
            globalVars.board3Comp = "DoneY"
        # Up and Down B3
        elif (board3["a"] == " O " and board3["d"] == " O " and board3["g"]== " O ") or (board3["b"] == " O " and board3["e"] == " O " and board3["h"]== " O ") or (board3["c"] == " O " and board3["f"] == " O " and board3["i"]== " O "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " O "
            globalVars.board3Comp = "DoneY"
        # Diagonal B3
        elif (board3["a"] == " O " and board3["e"] == " O " and board3["i"]== " O ") or (board3["c"] == " O " and board3["e"] == " O " and board3["g"]== " O "):
            board3["a"] = board3["b"] = board3["c"] = board3["d"] = board3["e"] = board3["f"] = board3["g"] = board3["h"] = board3["i"] = " O "
            globalVars.board3Comp = "DoneY"


        # Left and Right B4
        if (board4["a"] == " O " and board4["b"] == " O " and board4["c"]== " O ") or (board4["d"] == " O " and board4["e"] == " O " and board4["f"]== " O ") or (board4["g"] == " O " and board4["h"] == " O " and board4["i"]== " O "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " O "
            globalVars.board4Comp = "DoneY"
        # Up and Down B4
        elif (board4["a"] == " O " and board4["d"] == " O " and board4["g"]== " O ") or (board4["b"] == " O " and board4["e"] == " O " and board4["h"]== " O ") or (board4["c"] == " O " and board4["f"] == " O " and board4["i"]== " O "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " O "
            globalVars.board4Comp = "DoneY"
        # Diagonal B4
        elif (board4["a"] == " O " and board4["e"] == " O " and board4["i"]== " O ") or (board4["c"] == " O " and board4["e"] == " O " and board4["g"]== " O "):
            board4["a"] = board4["b"] = board4["c"] = board4["d"] = board4["e"] = board4["f"] = board4["g"] = board4["h"] = board4["i"] = " O "
            globalVars.board4Comp = "DoneY"


        # Left and Right B5
        if (board5["a"] == " O " and board5["b"] == " O " and board5["c"]== " O ") or (board5["d"] == " O " and board5["e"] == " O " and board5["f"]== " O ") or (board5["g"] == " O " and board5["h"] == " O " and board5["i"]== " O "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " O "
            globalVars.board5Comp = "DoneY"
        # Up and Down B5
        elif (board5["a"] == " O " and board5["d"] == " O " and board5["g"]== " O ") or (board5["b"] == " O " and board5["e"] == " O " and board5["h"]== " O ") or (board5["c"] == " O " and board5["f"] == " O " and board5["i"]== " O "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " O "
            globalVars.board5Comp = "DoneY"
        # Diagonal B5
        elif (board5["a"] == " O " and board5["e"] == " O " and board5["i"]== " O ") or (board5["c"] == " O " and board5["e"] == " O " and board5["g"]== " O "):
            board5["a"] = board5["b"] = board5["c"] = board5["d"] = board5["e"] = board5["f"] = board5["g"] = board5["h"] = board5["i"] = " O "
            globalVars.board5Comp = "DoneY"


        # Left and Right B6
        if (board6["a"] == " O " and board6["b"] == " O " and board6["c"]== " O ") or (board6["d"] == " O " and board6["e"] == " O " and board6["f"]== " O ") or (board6["g"] == " O " and board6["h"] == " O " and board6["i"]== " O "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " O "
            globalVars.board6Comp = "DoneY"
        # Up and Down B6
        elif (board6["a"] == " O " and board6["d"] == " O " and board6["g"]== " O ") or (board6["b"] == " O " and board6["e"] == " O " and board6["h"]== " O ") or (board6["c"] == " O " and board6["f"] == " O " and board6["i"]== " O "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " O "
            globalVars.board6Comp = "DoneY"
        # Diagonal B6
        elif (board6["a"] == " O " and board6["e"] == " O " and board6["i"]== " O ") or (board6["c"] == " O " and board6["e"] == " O " and board6["g"]== " O "):
            board6["a"] = board6["b"] = board6["c"] = board6["d"] = board6["e"] = board6["f"] = board6["g"] = board6["h"] = board6["i"] = " O "
            globalVars.board6Comp = "DoneY"


        # Left and Right B7
        if (board7["a"] == " O " and board7["b"] == " O " and board7["c"]== " O ") or (board7["d"] == " O " and board7["e"] == " O " and board7["f"]== " O ") or (board7["g"] == " O " and board7["h"] == " O " and board7["i"]== " O "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " O "
            globalVars.board7Comp = "DoneY"
        # Up and Down B7
        elif (board7["a"] == " O " and board7["d"] == " O " and board7["g"]== " O ") or (board7["b"] == " O " and board7["e"] == " O " and board7["h"]== " O ") or (board7["c"] == " O " and board7["f"] == " O " and board7["i"]== " O "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " O "
            globalVars.board7Comp = "DoneY"
        # Diagonal B7
        elif (board7["a"] == " O " and board7["e"] == " O " and board7["i"]== " O ") or (board7["c"] == " O " and board7["e"] == " O " and board7["g"]== " O "):
            board7["a"] = board7["b"] = board7["c"] = board7["d"] = board7["e"] = board7["f"] = board7["g"] = board7["h"] = board7["i"] = " O "
            globalVars.board7Comp = "DoneY"


        # Left and Right B8
        if (board8["a"] == " O " and board8["b"] == " O " and board8["c"]== " O ") or (board8["d"] == " O " and board8["e"] == " O " and board8["f"]== " O ") or (board8["g"] == " O " and board8["h"] == " O " and board8["i"]== " O "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " O "
            globalVars.board8Comp = "DoneY"
        # Up and Down B8
        elif (board8["a"] == " O " and board8["d"] == " O " and board8["g"]== " O ") or (board8["b"] == " O " and board8["e"] == " O " and board8["h"]== " O ") or (board8["c"] == " O " and board8["f"] == " O " and board8["i"]== " O "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " O "
            globalVars.board8Comp = "DoneY"
        # Diagonal B8
        elif (board8["a"] == " O " and board8["e"] == " O " and board8["i"]== " O ") or (board8["c"] == " O " and board8["e"] == " O " and board8["g"]== " O "):
            board8["a"] = board8["b"] = board8["c"] = board8["d"] = board8["e"] = board8["f"] = board8["g"] = board8["h"] = board8["i"] = " O "
            globalVars.board8Comp = "DoneY"

        # Left and Right B9
        if (board9["a"] == " O " and board9["b"] == " O " and board9["c"]== " O ") or (board9["d"] == " O " and board9["e"] == " O " and board9["f"]== " O ") or (board9["g"] == " O " and board9["h"] == " O " and board9["i"]== " O "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " O "
            globalVars.board9Comp = "DoneY"
        # Up and Down B9
        elif (board9["a"] == " O " and board9["d"] == " O " and board9["g"]== " O ") or (board9["b"] == " O " and board9["e"] == " O " and board9["h"]== " O ") or (board9["c"] == " O " and board9["f"] == " O " and board9["i"]== " O "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " O "
            globalVars.board9Comp = "DoneY"
        # Diagonal B9
        elif (board9["a"] == " O " and board9["e"] == " O " and board9["i"]== " O ") or (board9["c"] == " O " and board9["e"] == " O " and board9["g"]== " O "):
            board9["a"] = board9["b"] = board9["c"] = board9["d"] = board9["e"] = board9["f"] = board9["g"] = board9["h"] = board9["i"] = " O "
            globalVars.board9Comp = "DoneY"


def boardStartX():
    if globalVars.gameBoardPlaying == 1:
        placeX1()
    elif globalVars.gameBoardPlaying == 2:
        placeX2()
    elif globalVars.gameBoardPlaying == 3:
        placeX3()
    elif globalVars.gameBoardPlaying == 4:
        placeX4()
    elif globalVars.gameBoardPlaying == 5:
        placeX5()
    elif globalVars.gameBoardPlaying == 6:
        placeX6()
    elif globalVars.gameBoardPlaying == 7:
        placeX7()
    elif globalVars.gameBoardPlaying == 8:
        placeX8()
    elif globalVars.gameBoardPlaying == 9:
        placeX9()
def boardStartO():
    if globalVars.gameBoardPlaying == 1:
        placeO1()
    elif globalVars.gameBoardPlaying == 2:
        placeO2()
    elif globalVars.gameBoardPlaying == 3:
        placeO3()
    elif globalVars.gameBoardPlaying == 4:
        placeO4()
    elif globalVars.gameBoardPlaying == 5:
        placeO5()
    elif globalVars.gameBoardPlaying == 6:
        placeO6()
    elif globalVars.gameBoardPlaying == 7:
        placeO7()
    elif globalVars.gameBoardPlaying == 8:
        placeO8()
    elif globalVars.gameBoardPlaying == 9:
        placeO9()


def endGameX():
        # Left and Right B9
        if (globalVars.boardComp == "DoneX" and globalVars.board2Comp == "DoneX" and globalVars.board3Comp== "DoneX") or (globalVars.board4Comp == "DoneX" and globalVars.board5Comp == "DoneX" and globalVars.board6Comp== "DoneX") or (globalVars.board7Comp == "DoneX" and globalVars.board8Comp == "DoneX" and globalVars.board9Comp== "DoneX"):
            globalVars.gameWon = True
        # Up and Down B9
        elif (globalVars.boardComp == "DoneX" and globalVars.board4Comp == "DoneX" and globalVars.board7Comp== "DoneX") or (globalVars.board2Comp == "DoneX" and globalVars.board5Comp == "DoneX" and globalVars.board8Comp== "DoneX") or (globalVars.board3Comp == "DoneX" and globalVars.board6Comp == "DoneX" and globalVars.board9Comp== "DoneX"):
            globalVars.gameWon = True
        # Diagonal B9
        elif (globalVars.boardComp == "DoneX" and globalVars.board5Comp == "DoneX" and globalVars.board9Comp== "DoneX") or (globalVars.board3Comp == "DoneX" and globalVars.board5Comp == "DoneX" and globalVars.board7Comp== "DoneX"):
            globalVars.gameWon = True
def endGameO():
        # Left and Right
        if (globalVars.boardComp == "DoneY" and globalVars.board2Comp == "DoneY" and globalVars.board3Comp== "DoneY") or (globalVars.board4Comp == "DoneY" and globalVars.board5Comp == "DoneY" and globalVars.board6Comp== "DoneY") or (globalVars.board7Comp == "DoneY" and globalVars.board8Comp == "DoneY" and globalVars.board9Comp== "DoneY"):
            globalVars.gameWon = True
        # Up and Down
        elif (globalVars.boardComp == "DoneY" and globalVars.board4Comp == "DoneY" and globalVars.board7Comp== "DoneY") or (globalVars.board2Comp == "DoneY" and globalVars.board5Comp == "DoneY" and globalVars.board8Comp== "DoneY") or (globalVars.board3Comp == "DoneY" and globalVars.board6Comp == "DoneY" and globalVars.board9Comp== "DoneY"):
            globalVars.gameWon = True
        # Diagonal
        elif (globalVars.boardComp == "DoneY" and globalVars.board5Comp == "DoneY" and globalVars.board9Comp== "DoneY") or (globalVars.board3Comp == "DoneY" and globalVars.board5Comp == "DoneY" and globalVars.board7Comp== "DoneY"):
            globalVars.gameWon = True