#! /usr/bin/env python3

#-----------REGEX PRACTICE-------------

# import re

# #------date detection-------------
# testRx=re.compile(r"\d")
# dateRx = re.compile("[0-3][0-9]\/[0-1][0-9]\/[0-9]{4}")

# #pasteRx = re.compile("[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}")

# testStr = "The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date. 17/02/2022 01-01-2000"

# test = dateRx.findall(testStr)

# print(test)

# todo ---

# strong password detection

#regex version of strip()


