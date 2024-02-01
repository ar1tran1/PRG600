"""
Firstname: Aritra
Lastname: Nandy
Username: anandy
StudentID: 137916227
Email: anandy@myseneca.ca
"""

import sys
import os
import random

import sys
import os
import random

class TicTacToe:
    players = []
    winninggames = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7],]
    player1entry = []
    player2entry = []
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self) -> None:
        print("Initializing a 3X3 TicTacToe")
        self.getplayernames()
        self.printboard()
        self.rungame()

    def getplayernames(self):
        player1 = input("What is the name of the player 1: ")
        player2 = input("What is the name of the player 2: ")
        self.players = [player1, player2]

    def printboard(self):
        for i in range(0, 9, 3):
            print(f"|{self.board[i]}|{self.board[i + 1]}|{self.board[i + 2]}|")

    def getavailablenumbers(self):
        return [num for num in self.board if isinstance(num, int)]

    def getwinner(self):
        for game in self.winninggames:
            if all(self.board[i - 1] == "X" for i in game):
                return self.players[0]
            elif all(self.board[i - 1] == "O" for i in game):
                return self.players[1]
        return None

    def rungame(self):
        player_turn = 0

        while True:
            current_player = self.players[player_turn % 2]
            symbol = "X" if player_turn % 2 == 0 else "O"

            print(
                f"{current_player} Enter the number to play your symbol {symbol} (Available Numbers {','.join(map(str, self.getavailablenumbers()))}):",
                end=" "
            )
            try:
                chosen_number = int(input())
                if chosen_number not in self.getavailablenumbers():
                    raise ValueError("Number already played, choose a different number.")
            except ValueError as e:
                print("Enter available Number")
                continue

            self.board[chosen_number - 1] = symbol

            winner = self.getwinner()
            if winner:
                print(f"Player {winner} is the winner")
                break

            self.printboard()  # This line is removed

            if not self.getavailablenumbers():
                print("No one wins!")
                break

            player_turn += 1

if __name__ == "__main__":
    game = TicTacToe()
