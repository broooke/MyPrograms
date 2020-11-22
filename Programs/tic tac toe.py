import random, time, sys
#Window game
board = ["-","-","-",
         "-","-","-",
         "-","-","-",
         ]
#Choosing a suit for the player and the computer
choice_suit = input("You choose a suit: ")
if choice_suit=="X":
    time.sleep(1)
    print("You suit a X")
    time.sleep(1)
    print("Comp suit a O")
    suit_player='X'
    suit_comp='O'
else:
    time.sleep(1)
    print("You suit a O")
    time.sleep(1)
    print("Comp suit a X")
    suit_player='O'
    suit_comp='X'



while True:
    #Check win
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    time.sleep(1)
    if row_1==True:
        if board[0]==suit_player:
            print("Won player with suit: " + board[0])
        else:
            print("Won comp with suit: " + board[0])
        sys.exit(0)
    elif row_2==True:
        if board[3]==suit_player:
            print("Won player with suit: " + board[3])
        else:
            print("Won comp with suit: " + board[3])
        sys.exit(0)
    elif row_3==True:
        if board[6]==suit_player:
            print("Won player with suit: " + board[6])
        else:
            print("Won comp with suit: " + board[6])
        sys.exit(0)
    elif col_1==True:
        if board[0]==suit_player:
            print("Won player with suit: " + board[0])
        else:
            print("Won comp with suit: " + board[0])
        sys.exit(0)
    elif col_2==True:
        if board[1]==suit_player:
            print("Won player with suit: " + board[1])
        else:
            print("Won comp with suit: " + board[1])
        sys.exit(0)
    elif col_3==True:
        if board[2]==suit_player:
            print("Won player with suit: " + board[2])
        else:
            print("Won comp with suit: " + board[2])
        sys.exit(0)
    elif diag_1==True:
        if board[0]==suit_player:
            print("Won player with suit: " + board[0])
        else:
            print("Won comp with suit: " + board[0])
        sys.exit(0)
    elif diag_2==True:
        if board[2]==suit_player:
            print("Won player with suit: " + board[2])
        else:
            print("Won comp with suit: " + board[2])
        sys.exit(0)
    

    time.sleep(1)   
    #Wrote game window
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    time.sleep(1)
    #Wrote a suit("O","X")
    Valid = False
    while not Valid:
        choice_player = int(input("You choose a cage: "))
        #choice_comp = random.randint(0,8)
        if board[choice_player]=="-":
            Valid=True
        else:
            print("Enter the correct a cage.(player)")
    #board[choice_comp]=suit_comp
    board[choice_player]=suit_player
    time.sleep(1)
    Valid1= False
    while not Valid1:
        choice_comp = random.randint(0,8)
        if board[choice_comp]=="-":
            Valid1=True

    board[choice_comp]=suit_comp
        
    