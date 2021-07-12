# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:12:26 2021

@author: User
"""

"""
The 6x7 board:

|  |  |  |  |  |  |  |  1
----------------------  2
|  |  |  |  |  |  |  |  3
----------------------  4
|  |  |  |  |  |  |  |  5
----------------------  6
|  |  |  |  |  |  |  |  7
----------------------  8
|  |  |  |  |  |  |  |  9
----------------------  10
|  |  |  |  |  |  |  |  11
----------------------  12
1  3  5  7  9  11 13 15

"""
##Still need to put it inside board


def Board(rows,columns):

    print()
    for i in range(rows+1):
        if i%2 == 0:
            for j in range(0,columns+1):
                if j%2 == 1:
                    if j != columns:
                        print("  ",end="")
                    else:
                        print("  ")
                else:
                    print("|",end="")
        else:
            print("----------------------")

Board(11,15)


currentField = [[" ", " "," "," "," "," "," "],
                [" ", " "," "," "," "," "," "],
                [" ", " "," "," "," "," "," "],
                [" ", " "," "," "," "," "," "],
                [" ", " "," "," "," "," "," "],
                [" ", " "," "," "," "," "," "]]

Player = 1
CurrentRow = 5
print(currentField)
while True:
    print("Player's turn: ", Player)
    ChosenColumn = int(input("Choose your column: ")) - 1
    if Player == 1:
        if currentField[CurrentRow][ChosenColumn] == " ":
            currentField[CurrentRow][ChosenColumn] = "X"
            Player = 2
        else:
            CurrentRow -= 1
            currentField[CurrentRow][ChosenColumn] = "X"
            Player = 2
    else:
        if currentField[CurrentRow][ChosenColumn] == " ":
            currentField[CurrentRow][ChosenColumn] = "O"
            Player = 1
        else:
            CurrentRow -= 1
            currentField[CurrentRow][ChosenColumn] = "O"
            Player = 1
    print(currentField)

    
