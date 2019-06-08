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
        if(i == 0):
            return "rock"
        elif(i == 1):
            return "scissors"
        else:
            return "paper"

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
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score = [0, 0, 0]

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        update_score(move1, move2, self.score)
        print(
            f"Score: " +
            "Player One: {self.score[0]}, " +
            "Player Two: {self.score[1]}, " +
            "Ties: {self.score[2]}\n")

    def play_game(self):
        print("Game start!")
        round = 0
        while(abs(self.score[0] - self.score[1]) < 3):
            print(f"Round {round}:")
            self.play_round()
            round += 1
        print("Game over!\n")
        print(
            f"Final Score\n\t" +
            "Player One: {self.score[0]}\n\t" +
            "Player Two: {self.score[1]}\n\t" +
            "Ties: {self.score[2]}")
        winner = ""
        if(self.score[0] > self.score[1]):
            print("WINNER: PLAYER ONE!!!!\n")
        elif(self.score[1] > self.score[0]):
            print("WINNER: PLAYER TWO!!!!\n")
        else:
            print("TIE GAME!!!!\n")


if __name__ == '__main__':
    game = Game(CyclePlayer(), RandomPlayer())
    game.play_game()
