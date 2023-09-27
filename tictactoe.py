##
##START
##
print("\n\t\tTIC TAC TOE")

Player_1 = input("\nPlayer 1's Name : ").title().strip()
Player_2 = input("Player 2's Name : ").title().strip()

print("\nWelcome", Player_1, "and", Player_2 + "!\n")

##
##Choosing X or O
##
Player_1_XO = input(Player_1 + ", please choose 'X' or 'O' \n> ").upper().strip()

while Player_1_XO != "X" and Player_1_XO != "O":
    Player_1_XO = input(Player_1 + ", please either choose only 'X' or 'O'. \n> ").upper().strip()
    if Player_1_XO == "X" or Player_1_XO == "O":
        if Player_1_XO == "X":
            Player_2_XO = "O"
            print("\n" + Player_1, "will be playing (" + Player_1_XO +")")
            print(Player_2, "will be playing (" + Player_2_XO +")")
            break

        elif Player_1_XO == "O":
            Player_2_XO = "X"
            print("\n" + Player_1, "will be playing (" + Player_1_XO +")")
            print(Player_2, "will be playing (" + Player_2_XO +")")
            break
else:
    if Player_1_XO == "X":
        Player_2_XO = "O"
        print("\n" + Player_1, "will be playing (" + Player_1_XO +")")
        print(Player_2, "will be playing (" + Player_2_XO +")")

    elif Player_1_XO == "O":
        Player_2_XO = "X"
        print("\n" + Player_1, "will be playing (" + Player_1_XO +")")
        print(Player_2, "will be playing (" + Player_2_XO +")")

ready = input("\nPress ENTER when you're both ready")
print("\n\nLET THE GAME BEGIN!")

##
##FUNCTIONS
##
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def grid():
    print("\t|       |")
    print("   ", positions[0], "  |  ", positions[1], "  |  ", positions[2])
    print("\t|       |")
    print("-------------------------")
    print("\t|       |")
    print("   ", positions[3], "  |  ", positions[4], "  |  ", positions[5])
    print("\t|       |")
    print("-------------------------")
    print("\t|       |")
    print("   ", positions[6], "  |  ", positions[7], "  |  ", positions[8])
    print("\t|       |")

def player1_turn():
    print("\n\n" + Player_1 + "'s turn (" + Player_1_XO + ")\n")

def player2_turn():
    print("\n\n" + Player_2 + "'s turn (" + Player_2_XO + ")\n")

def player1_moves():
    players_position = int(input("\nChoose 1 ~ 9 \n> "))
    while players_position not in range(1, len(positions) + 1):
        print("\nInvalid Number!")
        players_position = int(input("You can only choose from 1 ~ 9 \n> "))
    else:
        while positions[players_position - 1] != " ":
            print("\nPosition taken!")
            players_position = int(input("Please choose again \n> "))
        for numbers in range(1, len(positions) + 1):
            if players_position == numbers:
                positions[numbers - 1] = Player_1_XO

def player2_moves():
    players_position = int(input("\nChoose 1 ~ 9 \n> "))
    while players_position not in range(1, len(positions) + 1):
        print("\nInvalid Number!")
        players_position = int(input("You can only choose from 1 ~ 9 \n> "))
    else:
        while positions[players_position - 1] != " ":
            print("\nPosition taken!")
            players_position = int(input("Please choose again \n> "))
        for numbers in range(1, len(positions) + 1):
            if players_position == numbers:
                positions[numbers - 1] = Player_2_XO

def P1_check_win():
    #Horizontal Check
    if (positions[0] == Player_1_XO and positions[1] == Player_1_XO and positions[2] == Player_1_XO) or \
       (positions[3] == Player_1_XO and positions[4] == Player_1_XO and positions[5] == Player_1_XO) or \
       (positions[6] == Player_1_XO and positions[7] == Player_1_XO and positions[8] == Player_1_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_1, "won!")
        exit()
    #Vertical Check
    elif (positions[0] == Player_1_XO and positions[3] == Player_1_XO and positions[6] == Player_1_XO) or \
         (positions[1] == Player_1_XO and positions[4] == Player_1_XO and positions[7] == Player_1_XO) or \
         (positions[2] == Player_1_XO and positions[5] == Player_1_XO and positions[8] == Player_1_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_1, "won!")
        exit()
    #Diagonal Check
    elif (positions[0] == Player_1_XO and positions[4] == Player_1_XO and positions[8] == Player_1_XO) or \
         (positions[2] == Player_1_XO and positions[4] == Player_1_XO and positions[6] == Player_1_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_1, "won!")
        exit()

def P2_check_win():
    #Horizontal Check
    if (positions[0] == Player_2_XO and positions[1] == Player_2_XO and positions[2] == Player_2_XO) or \
       (positions[3] == Player_2_XO and positions[4] == Player_2_XO and positions[5] == Player_2_XO) or \
       (positions[6] == Player_2_XO and positions[7] == Player_2_XO and positions[8] == Player_2_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_2, "won!")
        exit()
    #Vertical Check
    elif (positions[0] == Player_2_XO and positions[3] == Player_2_XO and positions[6] == Player_2_XO) or \
         (positions[1] == Player_2_XO and positions[4] == Player_2_XO and positions[7] == Player_2_XO) or \
         (positions[2] == Player_2_XO and positions[5] == Player_2_XO and positions[8] == Player_2_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_2, "won!")
        exit()
    #Diagonal Check
    elif (positions[0] == Player_2_XO and positions[4] == Player_2_XO and positions[8] == Player_2_XO) or \
         (positions[2] == Player_2_XO and positions[4] == Player_2_XO and positions[6] == Player_2_XO):
        print("\n\n\tGAME OVER!\n")
        grid()
        print("\n" + Player_2, "won!")
        exit()

##
##Player 1's First Turn
##
player1_turn()
grid()
players_position = int(input("\nChoose 1 ~ 9 \n> "))
while players_position not in range(1, len(positions) + 1):
    print("\nInvalid Number!")
    players_position = int(input("You can only choose from 1 ~ 9 \n> "))
else:
    for numbers in range(1, len(positions) + 1):
        if players_position == numbers:
            positions[:] = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            positions[numbers - 1] = Player_1_XO

##
##Player 2's First Turn
##
player2_turn()
grid()
player2_moves()

##
##Player 1's Second Turn
##
player1_turn()
grid()
player1_moves()

##
##Player 2's Second Turn
##
player2_turn()
grid()
player2_moves()

##
##Player 1's Third Turn
##
player1_turn()
grid()
player1_moves()
P1_check_win()

##
##Player 2's Third Turn
##
player2_turn()
grid()
player2_moves()
P2_check_win()

##
##Player 1's Fourth Turn
##
player1_turn()
grid()
player1_moves()
P1_check_win()

##
##Player 2's Fourth Turn
##
player2_turn()
grid()
player2_moves()
P2_check_win()

##
##Player 1's Final Turn
##
player1_turn()
grid()
player1_moves()
P1_check_win()

##
##END
##
print("\n\n\tGAME OVER!\n")
grid()
print("\nIt's a TIE!")
exit()