# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:15:42 2021

@author: User
"""

    
def Guess():
    print("You can guess Genre, Artist, Title, Year_of_release,\
           DurationSeconds or DurationMinutes, Album or Producer")
    Value = input("Which value would you like to guess? \
                   Please use the form used above: ")
    Answer = input("What is your guess? :")
    if Song[Value] == Answer:
        print(True)
        return True
    else:
        print(False)
        return False

Song = {"Genre":"Pop", "Artist":"Ke$ha", "Title":"Learn to let go", 
        "Year_of_release": "2017", "DurationSeconds" : "289",
        "DurationMinutes":"4.49", "FromAlbum": "Rainbow", "Availability_Spotify":"Avaible",
        "Availability_ITunes":"Yes",
        "Availability_YouTube":"Yes",
        "Producer": "Ricky Reed"}
        
for Value in Song:
    print(Song[Value])

Guess()