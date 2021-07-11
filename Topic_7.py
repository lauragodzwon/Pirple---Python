# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 13:14:38 2021

@author: User
"""

import os

ChosenFile = input("Hello, please give the name of the file you wish to open: ")
Existance = os.path.isfile(ChosenFile)  ##Checks, if the file exists

if Existance == True:
    print("The file you are trying to open already exsist")
    print("What do you want to do with this file?")
    print("If you want to only read the file type: 1")
    print("If you want to delete the file and start over type: 2")
    print("If you want append something to the file type: 3")
    print("If you want to replace a singe line in this file type: 4")
    Option = int(input("Chosen option: "))
    if Option == 1:
        with open(ChosenFile, "r") as File:
            TheWholeFile = File.read()
            print("\nThe contents of the file: \n")
            print(TheWholeFile)
        File.close()
    if Option == 2:
       with open(ChosenFile, "w") as File:
           File.write(input("What should be the contents? \n"))
       File.close()
       with open(ChosenFile, "r") as File:
            TheWholeFile = File.read()
            print("\nThe contents of the file: \n")
            print(TheWholeFile)
       File.close()
    if Option == 3:
        with open(ChosenFile, "a") as File:
            File.write("\n")
            Text = input("\nThe text that should be appended to the file: \n")
            File.write(Text)
        File.close()
        with open(ChosenFile, "r") as File:
            TheWholeFile = File.read()
            print("\nThe contents of the file: \n")
            print(TheWholeFile)
        File.close()
    if Option == 4:                                     #Doesn't work, repair later
        with open(ChosenFile, "r+") as File:
            Line = int(input("The number of line you wish to replace: "))
            OldText = File.readlines()
            Text = input("The text that should be written into this line: \n")
        #with open(ChosenFile, "w") as File:
            for i, line in enumerate(OldText):
                if i == Line - 1:
                    OldText[i].replace(OldText[i],Text)
        File.close()
else:
    print("The file you are trying to open does not exist")
    print("We are going to create it")
    with open(ChosenFile, "w") as File:
           File.write(input("What should be the contents? \n"))
    File.close()
    with open(ChosenFile, "r") as File:
            TheWholeFile = File.read()
            print("\nThe contents of the file: \n")
            print(TheWholeFile)
    File.close()
