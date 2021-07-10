# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:31:19 2021

@author: User
"""

def Equality(a,b,c):
    
    if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        return True
    
    elif int(a) == int(b) == int(c):
        return True
    
    else: 
        return False
    
print(Equality(1,2,8))
print(Equality("1",1,6))