# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:10:41 2021

@author: User
"""

def Board(rows, columns):
    
    for i in range (rows+1):
        if i%2 == 0:
            for j in range (1, columns+1):
                if j%2 == 1:
                    if j != columns:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-------")
            
Board(6,7)