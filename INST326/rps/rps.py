def rps():
    while True:
        player1 = input("Player One's Turn: \nWhat Is Your Hand Sign? (R, P, or S)")
        player1 = player1.lower()
        if player1 == "r" or player1 == "p" or player1 == "s":
            break
    while True:
        player2 = input("Player Two's Turn: \nWhat Is Your Hand Sign? (R, P, or S)")
        player2 = player2.lower()
        if player2 == "r" or player2 == "p" or player2 == "s":
            break
    if (player1 == player2):
        print("Tie!")
    elif (player1 == "r" and player2 == "s"):
        print("Player 1 wins!")
    elif (player1 == "r" and player2 == "p"):
        print("Player 2 wins!")
    elif (player1 == "p" and player2 == "r"):
         print("Player 1 wins!")
    elif (player1 == "p" and player2 == "s"):
         print("Player 2 wins!")
    elif (player1 == "s" and player2 == "p"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

def start_game():
    rps()
    while True:    
        while True:
            playAgain = input("Do You Want To Play Again? ")
            playAgain = playAgain.lower()
            if playAgain == "y" or playAgain =="n":
                break
        if (playAgain == "y"):
            rps()
        elif (playAgain == "n"):
            print("Have A Nice Day")
            break
    
start_game()