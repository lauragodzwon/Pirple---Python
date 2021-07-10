# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:11:12 2021

@author: User
"""

def FizzBuzz():
    for i in range (1,100):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0 and i%5 != 0:
            print("Fizz")
        elif i%3 != 0 and i%5 == 0:
            print("Buzz")
        else:
            print(i)
        
FizzBuzz()