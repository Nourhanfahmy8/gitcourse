# File: CS112_A1_T2_2_20230560
# Purpose: Number scrabble, the player who collects numbers that sum up to 15 wins
# Author: Nourhan Mohammed Ahmed Fahmy
# ID: 20230560

# defining a function for player 1 to check if any 3 numbers in the list (player 1) add up to 15
def p1check(player1):
    for a in range(len(player1)):
        for b in range(a+1, len(player1)):
            for c in range(b+1, len(player1)):
                for d in range(c+1, len(player1)):
                    if (player1[a] + player1[b] + player1[c] == 15
                            or player1[a] + player1[b] + player1[d] == 15
                            or player1[a] + player1[c] + player1[d] == 15
                            or player1[b] + player1[c] + player1[d] == 15):
                        return True
                    else:
                        return False

# defining a function for player 2 to check if any numbers in the list (player 2) add up to 15
def p2check(player2):
    for a in range(len(player2)):
        for b in range(a+1, len(player2)):
            for c in range(b+1, len(player2)):
                for d in range(c+1, len(player2)):
                    if (player2[a] + player2[b] + player2[d] == 15
                            or player2[a] + player2[c] + player2[d] == 15
                            or player2[b] + player2[c] + player2[d] == 15):
                        return True
                    else:
                        return False
# a list is designed to store the numbers chosen of each player
player1 = []
player2 = []
# defining a function containing the game
def game():
    gamelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The game's list is: ", gamelist)
    total1 = 0
    total2 = 0
    while True:
        # Player 1's turn
        p1 = input(f"Player 1: Please enter a number from the list\nYour current list is: {player1}\n")
        while True:
            # validation check to make sure number input by player 1 is not a string and is a number in the list
            try:
                p1 = int(p1)
                if (p1 < 1 or p1 > 9) and (p1 not in gamelist):
                    p1 = int(input("Please enter a valid number between 1 and 9\n"))
                elif p1 not in gamelist:
                    p1 = int(input("Please select a number from the list \n"))
                else:
                    break
            except ValueError:
                p1 = input("Please enter an integer number\n")
        total1 += p1
        player1.append(p1)
        gamelist.remove(p1)
        # checking if the sum of the first 3 numbers of player 1 equal 15
        if total1 == 15 and len(player1) == 3:
            print("--Player 1 is the winner--")
            print("***The list of player 1*** ", player1)
            break
        # calling the check function of player 1
        elif p1check(player1) == (True):
            print("--Player 1 is the winner--")
            print("***The list of player 1 is*** ", player1)
            break
        # displaying the list of player 1 if player 1 doesn't win
        print("->>Player 1s list is: ", player1)
        # checking if the game's list is empty
        if len(gamelist) == 0:
            print("\nThe game is a draw")
            print("List of player 1: ", player1)
            print("List of player 2: ", player2)
            print("\n--------------------------\n")
            break
        # displaying the list after removing the number chosen by player 1
        print("-------The new game list is: ", gamelist, "-------\n")
        # Player 2's turn
        p2 = input(f"Player 2: Please enter a number from the list\nYour current list is: {player2}\n")
        while True:
            # validation check to make sure number input by player 2 is not a string and is a number in the list
            try:
                p2 = int(p2)
                if (p2 < 1 or p2 > 9) and (p2 not in gamelist):
                    p2 = int(input("Please enter a valid number between 1 and 9\n"))
                elif p2 not in gamelist:
                    p2 = int(input("Please select a number from the list \n"))
                else:
                    break
            except ValueError:
                p2 = input("Please enter an integer number \n")
        total2 += p2
        player2.append(p2)
        gamelist.remove(p2)
        # checking if the sum of the first 3 numbers of player 2 equal 15
        if total2 == 15 and len(player2) == 3:
            print("--Player 2 is the winner--")
            print("***The list of player 2 is*** ", player2)
            break
        # calling the check function of player 2
        elif p2check(player2) == (True):
            print("--Player 2 is the winner--")
            print("***The list of player 2 is*** ", player2)
            break
        # displaying the list of player 2 if player 2 doesn't win
        print("->>Player 2s list is: ", player2)
        # displaying the new list after removing the number chosen by player 2
        print("-------The new game list is: ", gamelist, "-------\n")

# printing a welcoming message to the user and explaining the rule of the game
print("---Welcome to the Number Scrabble game---\n"
      "Each player will take turns by choosing a number from 1 to 9\n"
      "Each number may be chosen only once\nThe player whose numbers add up to 15 wins\n"
      "If none of the players numbers add to 15 then the game is a draw\n")
print("*******************************************\n")
# calling the game function to start the game
game()
# after the game ends, will ask the players if they want to play again
while True:
    again = input("Would you like to play another game? Y/N\n").lower()
    if again == "y":
        player1.clear()
        player2.clear()
        print("============================")
        print("\nStarting a new game")
        game()
    elif again == "n":
        input("\nPlease click the enter button to exit the game...")
        break
    else:
        continue