import sys
import os 
import random

"""
Firstname: John
Lastname: Doe
Username: JohnDoe
StudentID: 123456
Email: johndoe@senecacollege.ca
"""

# This is my TicTacToe Class 
class TicTacToe:
    # Declare class variables 
    # players is a list of players (this game will have 2 players)
    # Winninggames is a list of all winning possibilities 
    # Player1entry is a list of entries of first players 
    # Player2 entry is a list of entries of second player 
    players = []
    winninggames = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #This is just sample 
    player1entry = []
    player2entry = []
    board = [1,2,3,4,5,6,7,8,9] #Based on infromation given in the Final Exam Problem Statement

    # This is a constructor 
    """
    This is a constructor that prints an initialization statement
    Then call the getplayernames method to get the names and configure the list of players 
    Also call the printboard method to print the board, since this is a constructor the printboard is called first time here 
    Therefore printboard in this constructor will print initial brand new board ready to be played.
    """
    def __init__(self) -> None:
        print ("Initializing a 3X3 TicTacToe")
        
        
    """
    This is getplayernames method 
    This method asks user to enter the name of the player 1 and 2 one by one and append the names to the players class variable
    """
    def getplayernames(self): 
        player1 = input("What is the name of the player 1: ")
        
    """
    This is a printboard method 
    This method prints current state of the board 
    """
    def printboard(self):
        
    
    """
    This method gets all available numbers to be played at the time this method is called 
    It returns these available numbers 
    :return availablenumbers 
    """
    def getavailablenumbers(self):
        
    
    """
    This function goes through all the winning games and compare them against the each individual players entries
    By comparing the entries against winning game this method identifies the winner if there is one 
    If there is a winner this method returns the winner otherwise return None
    """
    def getwinner(self):


    """
    This is rungame method 
    This method continue to run a loop asking the user to enter the number to play and shows the available numbers as well
    If the user enter something otherthan the available number the prompt will continue to ask the same user to enter the correct values 
    This method assembles all the relevant method we have together, so that 
    First player one is asked to enter the number and then the second and then the first and it keep alternates 
    Until one player wins or the game finishes where there is no further numbers to enter. 
    Ultimately, if there is a winner it prints the winner. If ther eis no winner it prints No Winner. 
    """
    def rungame(self): 
        

# My main method to test this code locally
if __name__ == "__main__":
    game = TicTacToe()
    game.rungame()