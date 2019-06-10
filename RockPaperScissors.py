#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        i = random.randint(0, 2)
        return moves[i]

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while(True):
            move = input("Rock, paper, scissors? > ")
            if move.lower() in moves:
                return move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        i = random.randint(0, 2)
        if(i == 0):
            self.nextMove = "rock"
        elif(i == 1):
            self.nextMove = "scissors"
        else:
            self.nextMove = "paper"

    def move(self):
        return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        i = random.randint(0, 2)
        if(i == 0):
            self.nextMove = "rock"
        elif(i == 1):
            self.nextMove = "scissors"
        else:
            self.nextMove = "paper"

    def move(self):
        return self.nextMove

    def learn(self, my_move, their_move):
        if(my_move == "rock"):
            self.nextMove = "paper"
        elif(my_move == "paper"):
            self.nextMove = "scissors"
        else:
            self.nextMove = "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def update_score(move1, move2, score):
    if(beats(move1, move2) is True):
        score[0] += 1
        print("** PLAYER ONE WINS **")
    elif(beats(move2, move1) is True):
        score[1] += 1
        print("** PLAYER TWO WINS **")
    else:
        print("** TIE **")
        score[2] += 1


class Game:
    def __init__(self):
        self.score = [0, 0, 0]
        self.round = 0
        self.p1 = HumanPlayer()
        self.select_opponent()

    def select_opponent(self):
        opponentInt = input(
            "Select which version you would like to play against.\n"
            "1: Random Player\n"
            "2: Mirroring Player\n"
            "3: Cycling Player\n"
            "4: Human Player\n"
            "5: Surprise Me (Picks betweens options 1-3)\n")
        while(opponentInt not in ['1', '2', '3', '4', '5']):
            opponentInt = input("Invalid Input. Please select a number between 1 and 5: ")
        opponent = [RandomPlayer(), ReflectPlayer(),
                    CyclePlayer(), HumanPlayer()]
        if(opponentInt == "5"):
            self.p2 = opponent[random.randint(0, 2)]
        else:
            self.p2 = opponent[int(opponentInt) - 1]

    def play_round(self):
        print(f"Round {self.round + 1}:")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        update_score(move1, move2, self.score)
        print(
            "Score: " +
            f"Player One: {self.score[0]}, " +
            f"Player Two: {self.score[1]}, " +
            f"Ties: {self.score[2]}\n")

    def end_game(self):
        print("Game over!\n")
        print(
            "Final Score\n\t" +
            f"Player One: {self.score[0]}\n\t" +
            f"Player Two: {self.score[1]}\n\t" +
            f"Ties: {self.score[2]}")
        winner = ""
        if(self.score[0] > self.score[1]):
            print("WINNER: PLAYER ONE!!!!\n")
        elif(self.score[1] > self.score[0]):
            print("WINNER: PLAYER TWO!!!!\n")
        else:
            print("TIE GAME!!!!\n")

    def play_game(self):
        gameType = input("Enter the number of rounds to play, "
                         "or hit 0 to play until someone is up by 3: ")
        while(True):
            try:
                gameType = int(gameType)
                break
            except:
                gameType = input(
                    "Invalid response. Please Enter an integer number: ")
        print("Game start!")
        if(gameType == 0):
            while(abs(self.score[0] - self.score[1]) < 3):
                self.play_round()
                self.round += 1
        else:
            for roundNum in range(gameType):
                self.play_round()
                self.round += 1
        self.end_game()


if __name__ == '__main__':
    game = Game()
    game.play_game()
