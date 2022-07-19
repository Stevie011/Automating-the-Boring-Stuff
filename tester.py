"""
Add to anki section **************

1. What is a "greedy" regular expression? What is python by default?
    they match the longest possible string, python is greedy by default


2. How do we declare "mnongreedy" regexs?   
    question mark after the square brackets => {5,6}?
    nonGreedyRegex = re.compile(r"(Ha){3,5}?)
    

3. how do we create our own character class to search only for digits 0 to 5 ?  
    fiveRegex = re.compile(r"[0-5")
    

4. how do we make our own character class to regex search only for vowels?  
    vowelRegex = re.compile(r"[aeiouAEIOU")
    

5. Do we have to use .group() if we've used the .findall() method to find the regex?    
    no, it auto puts them into a list
    

6. How do we tell the regex the match must be at the beginning of the text?
    ^
    startsWithHelloRx = re.compile(r"^Hello")
    

7. How do we tell the regex search the string has to end with the pattern?
    $
    endsWithNumRx = re.compile(r"\d$")
    
    

8. What's the wildcard char for a regex pattern? What's the only thing it doesn't match with?
    .
    matches any char except newline
    Rx= re.compile(r".at")
    
    

9. How do we match an actual . in regex?
    escape it with \.  so it will be \.
    
    

10. What does the sub() method in regex do?
    substitutes text for other text
    

11. How do we create a multiline string?
    triple quotes
    

12. Can we tell regex to ignore case?
    yes => .IGNORECASE
    

13. 
    

14. 



page 133
    


"""
#dictionary creation with {}
#favColors = {"Stevie": "Blue", "Jess": "Maroon", "Amy":"Yellow"}

#iterate through values
# for i in favColors.values():
#     print(i)

#iterate through keys
# for j in favColors.keys():
#     print(j)

#you can take .keys() or .values() straight to a list

#print(list(favColors.keys()))

#.items() gives you the entire dict entry each time
# for i in favColors.items():
#     print(i)

#you can also assign multiple variables to keys and values

# for i,j in favColors.items():
#     print("i is now: " + i)
#     print("j is now: " + j)

#use "in" to check if value in .keys() or .values()

#print("Stevie" in favColors.keys()) #True

#print("Jono" in favColors.keys()) #False

#print("Stevie" in favColors) #True

#print("Maroon" in favColors) #False

#using dict name by itself is the same as using .keys()

#print(favColors.get("Jess", 0))

# favColors = {"Stevie": "Blue", "Jess": "Maroon", "Amy":"Yellow"}

# favColors.setdefault("Ally", "Red")

# print(favColors.get("Ally"))

# favColors.setdefault("Ally", "Green")

# print(favColors.get("Ally"))

# import pprint

# testStr = "here is a test string with a bunch of words in it. we will count all of these letters"

# #use dict for counting
# count ={}
# #loop through the string
# for i in testStr:
#     #adds char to diict, sets its count val to 0 if it's not present already
#     count.setdefault(i, 0)
#     #add 1 to it
#     count[i] = count[i] + 1

# pprint.pprint(count)

"""
picnicGuests = {"Alice": {"apples": 5, "pretzels": 12},
                "Bob": {"ham sandwiches": 3, "apples": 2},
                "Carol": {"cups": 3, "apple pies": 1}}




def totalItemsBrung(allStuffBrought, item):
    numBrought = 0
    #here, i will be the names in the greater dict, j will be each subdict
    for i,j in allStuffBrought.items():
        #adds number of items to numBrought or 0 if its not present
        numBrought = numBrought + j.get(item, 0)
    return numBrought

print("Apples total -- " + str(totalItemsBrung(picnicGuests, "apples")))

"""

#print(", ".join(["cats", "rats", "bats"]))

#print("hello".rjust(30, "$"))

# def printPicnicStuff(itemsDict, leftWid, rightWid):
#     print("THIS IS THE STUFF".center(leftWid + rightWid, "="))
#     for key,value in itemsDict.items():
#         print((key.ljust(leftWid, ".") + str(value).rjust(rightWid)))

# items = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}

# print(printPicnicStuff(items, 50,30))

# import pyperclip
# pyperclip.copy("hello yall")



# 1. re.compile()

# 2. coz we need to search for those elements 

# 3. an object matching the poistion of the 1st occurence of the searched string

# 4. matchObject.group()

# 5. grooup 1

# 6. escape it with \

# 7. the number of groups in the regex

# 8. pipe - works like Or

# 9. makes the thing optional

# 10. + is at least one (or more), * is is none or more

# 11. {3} is 3 occurences, {3-5} means it occurs btwn 3 and 5 times

# 12. \d digits \w word chars \s spaces 

# 13. \D anything not digit \W not word \S not space 

# 14. ???

# 15. [a-z0-9]

# 16. ???

# 17. wildcard, matches anything. DOTALL???

18. not too sure about this -- X drummers, X pipers, five rings, X hens

19. re.VERBOSE ???




import re

numRx = re.compile(r"\d+")

test = numRx.sub("X", "12 drummers, 11 pipers, five rings, 3 hens")

print(test)


