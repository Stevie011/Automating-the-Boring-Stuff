# def isPhoneNumber(num):
#     if len(num) != 12:
#         return False
#     for i in range(0,3):
#         if not num[i].isdecimal():
#             return False
#     if num[3] != " ":
#         return False
#     for i in range(4,7):
#         if not num[i].isdecimal():
#             return False
#     if num[7] != " ":
#         return False
#     for i in range(8,12):
#         if not num[i].isdecimal():
#             return False
#     return True

# message = "Call me on 011 565 7878 tomorrow. The office number is 52, on 72nd street. 082 676 9595 is my cell number"

# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print("number found : " + chunk) 
# print("Done")

# message = "Call me on 011 655 7878 tomorrow. The office number is 52, on 72nd street. 082 676 9595 is my cell number"

# import re

# phoneNumRegex = re.compile(r"\d\d\d \d\d\d \d\d\d\d")

# #we can get a match object from the .search() function

# matchObject = phoneNumRegex.findall(message)

# for i in matchObject:
#     print(i)
#print("Phone number found : " + str(matchObject))

# import re

# bikiniBottomRegex = re.compile(r"Spongebob|Patrick")
# matchObject1 =  bikiniBottomRegex.search("Spongebob and Patrick")
# print(matchObject1.group())

# matchObject2 = bikiniBottomRegex.search("Patrick and Squidward")
# print(matchObject2.group())

#import re

# batRegex = re.compile(r"Bat(wo)*man")

# mo1 = batRegex.search("The adventures of Batman")

# print(mo1.group())

# mo2 = batRegex.search("The adventures of Batwowowowowoman")

# print(mo2.group())

# batRegex = re.compile(r"Bat(wo)+man")

# mo1 = batRegex.search("The adventures of Batman")
# if mo1:
#     print(mo1.group())


# mo2 = batRegex.search("The adventures of Batwowowowowoman")
# if mo2:
#     print(mo2.group()) 

# woRx = re.compile(r"(wo){3}")

# moWo = woRx.search("The adventures of Batwowowowowoman")

# print(moWo.group())

import re

# vowelRx = re.compile(r"[aeiouAEIOU]")
# vowels = vowelRx.findall("Rbobocop eats human food. HUMAN FOOD!")
# print(vowels)

phoneNumRx = re.compile(r"phone number (\d*)")

text = "lorem ipsum lorem ipsum phone number 868686868 lorem ipsum phone number 888 999 555 lorem ipsum phone number : 858 8585"

mo = phoneNumRx.findall(text)

print(mo)