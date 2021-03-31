import random
initial_board = {'1': '.', '2': '.', '3': '.',
                 '4': '.', '5': '.', '6': '.',
                 '7': '.', '8': '.', '9': '.'}#using a dictionary allows for easier access to values

def showboard(board):#helper function to print board
    print("  1 2 3")
    print("1 "+board['1']+" "+board['2']+" "+board['3'])
    print("2 " + board['4'] + " " + board['5'] + " " + board['6'])
    print("3 " + board['7'] + " " + board['8'] + " " + board['9'])


def checkwin(board):#helper function to check whether the game has been won by one of the players
    if board['7'] == board['8'] == board['9'] or board['3'] == board['6'] == board['9']:
        if board['9'] == "X":
            print("Player X won!")
            return True
        elif board['9'] == "O":
            print("Player O won!")
            return True
    elif board['1'] == board['2'] == board['3'] or board['1'] == board['4'] == board['7']:
        if board['1'] == "X":
            print("Player X won!")
            return True
        elif board['1'] == "O":
            print("Player O won!")
            return True
    elif board['4'] == board['5'] == board['6'] or board['2'] == board['5'] == board['8']:
        if board['5']=="X":
            print("Player X won!")
            return True
        elif board['5'] == "O":
            print("Player O won!")
            return True
    elif board['1'] == board['5'] == board['9'] or board['3'] == board['5'] == board['7']:
        if board['5'] == "X":
            print("Player X won!")
            return True
        elif board['5'] == "O":
            print("Player O won!")
            return True
    else:
        return False

def clearboard(board):#cleans the filled board after a game
    for i in range(1,10):
        i=str(i)
        board[i]='.'




def PlayerMove(initial_board):#the actual game itself
    Players = ["X", "O"]
    userRound = input("Please choose to play as X or O:")
    while userRound!="X" and userRound!="O":
        userRound = input("Please only enter X or O")
    Players.remove(userRound)
    ComputerRole = Players[0]
    GameRound = "X"#since X always moves first
    showboard(initial_board)
    counter = 0#round counter
    unused_key = [1,2,3,4,5,6,7,8,9]#keep track of unused keys for computer to choose from
    for i in range(10):
        row = 0
        col = 0
        if GameRound == userRound :#if it is the user's round, prompt for inputs
            print("Player " + userRound + " Please make a move: ")  # first we need to ask the player to move
            row = int(input("Which row?"))
            while row > 3 :
                row = int(input("Row index out of bound, please enter again:"))
            col = int(input("Which column?"))
            while col > 3 :
                col = int(input("Column index out of bound, please enter again:"))
            key = str((row-1)*3 + col)#the above while loops check for valid row and col inputs
            if initial_board[key]!='.':
                row = int(input("Previously chosen spot taken, choose a new spot by first entering row: "))
                while row > 3:
                    row = int(input("Row index out of bound, please enter again:"))
                col = int(input("Then enter column: "))
                while col > 3:
                    col = int(input("Column index out of bound, please enter again:"))
                key = str((row - 1) * 3 + col)
                initial_board[key] = userRound
                unused_key.remove(int(key))#the above control flow prompts for user input when the chosen spot is already taken
            elif initial_board[key]=='.':
                initial_board[key] = userRound
                unused_key.remove(int(key))
        elif GameRound == ComputerRole:#when it's the computer's round, randomly choose an unused spot
            key = random.choice(unused_key)
            initial_board[str(key)]=ComputerRole
            unused_key.remove(int(key))
            print("The computer has made a move.")
        showboard(initial_board)
        #check win condition(same in a row, same in a column, same in the diagonal), to increase efficiency, we only need to check after 5 moves
        if counter>=5:
            if checkwin(initial_board):
                break
        counter += 1
        if counter==9:
            print("The game was a tie.")
            break
        if counter%2 != 0:
            GameRound = "O"
        elif counter%2 == 0:
            GameRound = "X"
    clearboard(initial_board)

PlayerMove(initial_board)









