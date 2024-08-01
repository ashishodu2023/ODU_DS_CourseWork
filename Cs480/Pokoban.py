# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:33:38 2023

@author: Ashish
"""


class PokobanSolve:
    
    def __init__(self,board):
        self.board = board
        
        
    
    def show_board(self,board):
        for row in board:
            print(row.join(' '))
            
            
        
        
        



if __name__=='__main__':
    print('Enter the board configuration')
    board = []
    while(1):
        boardline = input()
        if boardline!='':
            boardline +=1
            board.append(boardline)
            
    solve = PokobanSolve(board)
    solve.show_board()
        