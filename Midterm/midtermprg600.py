"""
Firstname: Aritra
Lastname: Nandy
Username: anandy
StudentID: 127916227
Email: anandy@myseneca.ca
"""

import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    # Roll two dice and get random numbers between 1 and 6
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    
    # Calculate the total
    total = die1 + die2
    
    # Print the results
    print(f"{die1} and {die2}")
    
    return total

# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players < 2:
                print("The game requires at least 2 players. Please enter a valid number of players.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number of players.")

    players = []
    for i in range(num_players):
        player_name = input(f"Enter the name of Player {i + 1}: ")
        players.append(player_name)

    return players


# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """

    while True:
        try:
            roundcount = int(input("Enter the number of rounds you want to play: "))
            if roundcount < 1:
                print("Please enter a valid number of rounds (1 or more).")
            else:
                return roundcount
        except ValueError:
            print("Invalid input. Please enter a valid number of rounds.")



# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here 

    # Initialize the game matrix with zeros
    game = [[0] * roundcount for _ in range(len(players))]

    gameset = [game, players, roundcount]
    return gameset

# 1 Marks
 
def asktoroll(players): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    input(f"{players}, press Enter to roll the dice...")
    score = rolldice()
    return score 

# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    max_score = max([sum(round_scores) for round_scores in game])
    winning_players = [players[i] for i, round_scores in enumerate(game) if sum(round_scores) == max_score]

    if len(winning_players) == 1:
        return winning_players[0]
    else:
        return ",".join(winning_players)


# 5 Marks 
def rungame():

    """

    function: This function runs the game

    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame

    It prints the header and Round 1 begining score card first with inital scores set to 0

    It then asks use to roll dices using asktoroll function for all rounds and players

    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.

    """

 

    # The next 5 lines are to get you started

    # Implement the rest of the code

 

    game, players, roundcount = setgame()

    printgame(game, players, 1, roundcount)

    print("*" * (13 + 8 * roundcount))

 

    for roundnum in range(1, roundcount + 1):

        for i, player in enumerate(players):

            game[i][roundnum - 1] = asktoroll(player)

        printgame(game, players, roundnum, roundcount)

 

    winner = findwinner(game, players)

    print(f"Congratulations {winner}! You are the WINNER!")

 

    choice = input("Would you like to play another game? [1] Yes [2] No: ")

    if choice == '1':

        rungame()

    else:

        print("Thank you and see you later!")

# 5 Marks
def printgame(game, players, roundnum, roundcount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    # Calculate the width of the columns based on the number of rounds
    max_name_len = max(len(player) for player in players)
    col_width = max(6, len(f"Round {roundcount}") + 2)

    # Print the header
    header = "*" * (col_width + 1) * (roundcount + 1)
    print(header)
    print(" " * (col_width + 1) + "Rounds", end="   ")
    for round_title in range(1, roundcount + 1):
        print(f"Round {round_title}".ljust(col_width), end="   ")
    print("Total".ljust(col_width))
    print(" " * (col_width + 1) + " ".ljust(col_width), end="   ")
    for _ in range(roundcount):
        print("Score".ljust(col_width), end="   ")
    print("Score".ljust(col_width))

    # Print player scores
    for i, player in enumerate(players):
        print(player.ljust(max_name_len + 1), end="   ")
        total_score = 0
        for j in range(roundcount):
            print(str(game[i][j]).rjust(col_width), end="   ")
            total_score += game[i][j]
        print(str(total_score).rjust(col_width))

    # Print footer
    print(header)

def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block