#! /usr/bin/env python3

# -----------EXTRACT-O-TRON ------------

# a python program to extract phone numbers and email addresses from web pages and documents
# """
# find way to get text into program -- pyperclip
# figure out regex pattern for phone numbers  and emails --
# compile results into separate file

# """

import pyperclip, re

#phone num regex

phoneNumRx = re.compile(r"""(
    (\d{3}|\(\d{3}\))?     #3 digits or 3 digits surrounded by brackets, made optional by ? at end
    (\s|-|\.)?             #seperator => space char or - or . (we've escaped it with \) also made optional by ?
    (\d{3})                #first 3 digits
    (\s|-|\.)              #seperator again, not optional this time
    (\d{4})                #last 4 digies
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension, also optional => \s* means any number of spaces, ext|x|ext. -- looks for any one of the three, \d{2,5} looks for 2-5 digits
)""", re.VERBOSE)

#email regex

emailRx = re.compile(r"""(
    [a-zA-Z0-9._%+-]+       #username -- unique char class -- low and upper letters, numbers, ., _ , %, + , - 
    @                       #straight up gotta be that @ symbol
    [a-zA-Z0-9.-]+           #domain nama -- another unique char class- letters, numbers, . , - 
    (\.[a-zA-Z]{2,4})       # dot whatver - looks for 2-4 letters
)""", re.VERBOSE)

#find matches in clipboard

#pyperclip paste syntax
text = str(pyperclip.paste())

#empty list to put matches into
matches = []

#phone num

#iter thru groups in text found by findall()
for groups in phoneNumRx.findall(text):
    #join the groups together
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    #check for extension
    #if val present in groups[8] it must be an ext
    if groups[8] != "":
        #add ext
        phoneNum += "x"+groups[8]
    #add it to matches list
    if len(phoneNum) > 9:
        matches.append(phoneNum)

#email
#more straightforward
for groups in emailRx.findall(text):
    matches.append(groups[0])


 

#copy results to clipboard

if len(matches)>0:
    #join makes matches into a single string separated by newlines
    pyperclip.copy("\n".join(matches))
    print("This is what was copied to the clipboard : ")
    print("\n".join(matches))
else:
    print("There weren't any matches (or the code isn't working)")