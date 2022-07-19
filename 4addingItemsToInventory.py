#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:33:51 2022

@author: stevenstewart
This takes a list and adds each item to an existing dictionary, incresing the count of each accordingly.
"""

#stuff is dict because of {}
stuff={'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', "thick stack"]

def addToInv(invo, addedItems):     #needs original inventory and the list of items to add to it
    for i in addedItems:        #iterates through the new items
        invo.setdefault(i, 0)
        invo[i] = invo[i] + 1
        """
        2 lines above are a shorter way of doing this-
        if i in invo.keys():    #checks if item already in list
            invo[i]+=1          #if it is, increases count by 1
        else:
            invo[i]=1           #if not, creates new entry with value of 1
        """
            
def displayInventory(invo):     #needs the inventory you want to display
    print("Current Inventory")  #prints title
    totalItems=0                #sets up variable for total item count
    for i,j in invo.items():    #iterates through keys (i) and values (j)
        print(j, ' ', i)        #prints number -j and key name - i
        totalItems +=j          #each iteration, adds j to total
    print('Total items : ', totalItems) #prints total
    
    

addToInv(stuff, dragonLoot) #runs first function

addToInv(stuff, ["thick stack"])
        
displayInventory(stuff) #runs second function using vales modified by 1st


