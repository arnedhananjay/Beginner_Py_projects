# Self-Destroy Python Program
"""
If The Password was not matched then this program will self-destroy itself.
This program can be used as a security purpose in several ways.
"""
import os
import time
import sys
print("A PROJECT BY CODE INDIA\nINSTAGRAM - '@CODE_INDIA_OFFICIAL'\nYOUTUBE - 'CODE INDIA- DHANANJAY ARNE'\n")
print("PLEASE ENTER PASSWORD OR THIS PROGRAM WILL SELF-DESTROY ITSELF")
password = input("ENTER YOUR PASSWORD HERE:\n")
if password == "set_password":
    print("Password Matched")
else:
    os.remove(sys.argv[0])
time(2)