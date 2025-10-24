# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:13:29 2025

@author: ritik
"""

import time
import os
import numpy as np

class ConwaysGame:
    def __init__(self, size, kernelSize):
        # Initialize variables
        # self.board = board
        self.size = size
        self.kernelSize = kernelSize

    def init_board(self):
        """Create initial board state append false to represent initial conditions.
        True forms the center three initial starting conditions
        @self.board represent current frame of the board
        @ n, m are coordinates to reference appending true and false"""
        self.board = np.zeros((self.size, self.size))
        # self.board[1:3, 1:3] = 1  # block

        # beehive
        # self.board[1, 2:4] = 1
        # self.board[2, 1] = 1
        # self.board[3, 2:4] = 1
        # self.board[2, 4] = 1

        self.board[1, 2:5] = 1

        self.draw()

    def count_neighbors(self):
        """A method to count the neighbors,
        @ new_board represents the changes made to the original board before reassignment
        @ surround represents the collection of points around the cell
        @r, v, h, v, h_neigh, and v_heigh all reference the respective points in the cell
        Live cells with 0 or 1 neighbors die due to underpopulation
        Live cells with 3 or more neighbors die due to overpopulation
        Dead cells with 2 live neighbors become alive
        BUGS: Error with the appending of live cells, live cells to the lower entrypoint
        """
        new_board = self.board.copy()
        surround = []
        self.kernelSize = 3
        kernel = int(self.kernelSize/2)
        for x in range (-1*kernel, kernel+1):
            for y in range (-1*kernel, kernel+1):
                surround.append((x, y))
                if((x == 0) and (y == 0)):
                    surround.pop(-1)     
        
        for r in range(0, self.size):
            for c in range(0, self.size):
                count = 0
                for h, v in surround:
                    h_neigh, v_neigh = r + h, c + v

                    if (
                        0 <= h_neigh < self.size
                        and 0 <= v_neigh < self.size
                        and (self.board[h_neigh][v_neigh] == 1)
                    ):
                        count += 1

                if self.board[r, c] == 1 and (count < 2 or count > 3):
                    new_board[r, c] = 0

                elif (self.board[r, c] != 1 and (count >2 and count <4)):
                    new_board[r, c] = 1
        self.board = new_board

    def draw(self):
        """Method to represent board in consol
        TODO: Re-implement as a numpy graphical representation
        """
        os.system("clear")
        for n in range(0, len(self.board)):
            print(self.board[n])
        print("\n")
        time.sleep(1)
        return

    def execute(self):
        """A function to drive the playing of the game"""
        self.init_board()
        while True:
            self.count_neighbors()
            self.draw()


ConwaysGame(9, 5).execute()  
""" (0, 1),
 (1, 0),
 (0, -1),
 (-1, 0),
 (1, 1),
 (-1, -1),
 (1, -1),
 (-1, 1),"""
