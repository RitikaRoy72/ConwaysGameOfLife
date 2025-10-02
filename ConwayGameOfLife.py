# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:13:29 2025

@author: ritik
"""

import time
import os

class ConwaysGame:
    def __init__(self, board):
        #Initialize variables
        self.board = board
    
    def boardINIT(self):
        """Create initial board state append false to represent initial conditions. 
        True forms the center three initial starting conditions
        @self.board represent current frame of the board
        @ n, m are coordinates to reference appending true and false """
        self.board = []
        for n in range (0, 5):
            self.board.append([])
            for m in range (0, 5):
                if (n == 1 or n == 2 or n == 3): 
                    if (m == 2):
                        self.board[n].append(True)
                    else: 
                        self.board[n].append(False)
                else:
                    self.board[n].append(False)
        self.draw()
    
    def countNeighbors(self):
        """A method to count the neighbors, 
        @ newBoard represents the changes made to the original board before reassignment
        @ surround represents the collection of points around the cell
        @r, v, h, v, h_neigh, and v_heigh all reference the respective points in the cell
        Live cells with 0 or 1 neighbors die due to underpopulation
        Live cells with 3 or more neighbors die due to overpopulation
        Dead cells with 2 live neighbors become alive
        BUGS: Error with the appending of live cells, live cells to the lower entrypoint
        """
      
        newBoard = self.board.copy()
        surround = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for r in range (0, 5):
            for c in range (0, 5):
                count = 0
                for h, v in surround:
                    h_neigh, v_neigh = r+h, c+v
                    
                    if 0<= h_neigh < 5 and 0 <= v_neigh < 5 and (newBoard[h_neigh][v_neigh] == 1):
                        count +=1
                        
                if self.board[r][c] == 1 and (count < 2 or count > 3):
                    newBoard[r][c] == False
                
                elif self.board[r][c] == 0 and count == 3:
                    newBoard[r][c] = True
        self.board = newBoard
        
        
    def draw(self):
        """Method to represent board in consol
        TODO: Re-implement as a numpy graphical representation
        """
        os.system("cls")
        for n in range (0, len(self.board)):
            print(self.board[n])
        print("\n")
        time.sleep(1)
        return
        
            
    def execute(self):
        """A function to drive the playing of the game"""
        self.boardINIT()
        while True:
            self.countNeighbors()
            self.draw()
            
ConwaysGame([]).execute()
        
                
                
        
        
