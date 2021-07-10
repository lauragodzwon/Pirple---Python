# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:01:58 2021

@author: User
"""

def Artist():
    Name = "Ke$ha"
    print("The name of the artist is",Name)

def Title():
    Title = "Learn to let go"
    print("The title of the song is",Title)
    
def Duration():
    DurationSeconds = 289
    DurationMinutes = 4.49
    print("Duration of the song in seconds equals", DurationSeconds)
    print("Duration of the song in minutes equals", DurationMinutes)

def Avaibility():
    Availability_Spotify = True
    Availability_ITunes = False
    Availability_YouTube = Availability_Spotify
    print("Avaibility of the song")
    print("Spotify:", Availability_Spotify)
    print("ITunes:", Availability_ITunes)
    print("YouTube:", Availability_YouTube)
    
    
Artist()
Title()
Duration()
print()
Avaibility()