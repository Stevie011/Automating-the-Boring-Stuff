# from pathlib import Path

# # p = Path("test.txt")

# # p.write_text("harzit world")

# # print(p.read_text())

# # helloFile = open("/Users/stevenstewart/Documents/vscode/Automating-the-Boring-Stuff-main/sonnet29.txt")

# # lines = helloFile.readlines()

# # for i in range(len(lines)):
# #     print(lines[i])

# testFile = open("spam.txt","a")

# testFile.write("really? 1000000 volts? \n")

# testFile.close()

# import shelve

# shelfTest = shelve.open("dataName")

# cats = ["Eve", "linx", "zuba"]

# shelfTest["cats"] = cats

# shelfTest.close()

# shelfTest =  shelve.open("dataName")

# print(type(shelfTest))

# print(shelfTest["cats"])

# shelfTest.close()

import pprint

cats = [{"name": "Eve", "desc": "soft"}, {"name": "linx", "desc": "fluffy"}]

fileTest = open("catTest.py", "w")

fileTest.write("catsList = " + pprint.pformat(cats) + "\n")

fileTest.close()