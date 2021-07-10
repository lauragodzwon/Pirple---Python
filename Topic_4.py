# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:58:28 2021

@author: User
"""

MyUniqueList = []
MyLeftovers = []

def AddToList(Value):
        if Value not in MyUniqueList:
            MyUniqueList.append(Value)
            return True
        else:
            MyLeftovers.append(Value) ##in one function
            return False

#def Leftovers(Value):    ##in two separate functions
    #if Value in MyUniqueList:
       # MyLeftovers.append(Value)
   #else:
        #pass

AddToList(1)
AddToList(10)
AddToList(1)
AddToList("Hello")
AddToList(16.0-1.2)
AddToList(14.8)
AddToList("Couch")
AddToList([1.5,12,8])
AddToList("Couch")
print(MyUniqueList)

#Leftovers(1)
#Leftovers("Hello")
#Leftovers(16.0-1.2)
#Leftovers(15)
#Leftovers("Couch")
print(MyLeftovers)