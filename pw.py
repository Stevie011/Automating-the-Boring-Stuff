#! /usr/bin/env python3
#password locker test program -- pass-o-mat

#dict to store passwords

MEMORY_BANK= {"email": "khokyhoky879687698", "blog": "gfgfgfgf6454545", "luggage": "qwwqwqwqwq212121212"}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]   #first line of sys.argv is the account name

if account in MEMORY_BANK:
    pyperclip.copy(MEMORY_BANK[account])
    print("Pass phrase for " + account + " copied to clipboard.")
else:
    print("There is no account called : " + account)

    
