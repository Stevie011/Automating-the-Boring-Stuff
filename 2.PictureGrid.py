"""
Created on Thu Jan 20 17:37:37 2022

@author: stevenstewart

This prints out all the values in each column on a single line.
i.e. 1st val from each list in grid on 1st line, 2nd val from each on 2nd and so forth

"""

grid = [['.', '.', '.', '.', '.', '.'],     #grid defined as per exercise
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

            #these 2 variables are used to iterate through the list grid
i=0         #x co-ord of grid, selects which list within grid
j=0         #y co-ord, selects which item within the (sub)list

while j<len(grid[0]):       #loop iterates which 'column' is printing(actually, which index in each sublist is printing)
    while i<len(grid):      #iterates 'row' (actually which index in main list is printing)
        print(grid[i][j], end="")   #prints whatever is at postion j of item i. end="" makes it print on the same line
        i+=1                        #moves down to next 'row'
        if i==len(grid):            #this tells us we're at the end of the row
            print('')               #this inserts a line break (functionally)
    i=0         #i back to 0, because we need to start at the beginning of the next 'row'
    j+=1        #this takes us to the next 'column'
