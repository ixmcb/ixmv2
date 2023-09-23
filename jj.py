from tqdm import tqdm , trange
from tqdm import tqdm
import time
import os
import sys
from random import randint

clear = lambda: os.system('cls')
clear()

print("\033[1;36m[ X ] Finding latest server​ ")

time.sleep(5)

print("\033[1;36m[ X ] Server connected and saved in folx ")

time.sleep(5)


with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)




logo = '''

|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|                                                                                    |
|           DEVLOPER : IXMCB                                                         |         
|                                                       TEAM IXM WP TOOLS V 3.5      |
|           PROGRAM : WP LOCK V 3.5                                                  |      
|                                                                                    |         
|           GITHUB : https://github.com/ixmcb/reed                                   |  
|                                                                                    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
                                                                        

'''
print(logo)
print("                                          [TEAM IXM V 3.5 WP LOCKS]")





name = input("[ \033[1;31m- \033[1;36m] What iS your Name : ")


password = input("[ \033[1;31m- \033[1;36m] Enter the password : ")


if password == "hty":
    print(" ")
    print(" Welcome "+   name)
else:
    print("Sorry try again !")
    sys.exit(666)

print(" ")
print("[ ✓ ] Team Ixm v 3.5 ✓ ")
print("[ ✓ ] Login Done ✓ ")

def menu():
    print(" ")
    print("\033[1;31m[ \033[1;34m1 \033[1;31m] \033[1;35mFACEBOOK                      \033[1;31m[ \033[1;34m2 \033[1;31m] \033[1;35mINSTAGRAM")
    print("\033[1;31m[ \033[1;34m3 \033[1;31m] \033[1;35mHACK 2K13                     \033[1;31m[ \033[1;34m4 \033[1;31m] \033[1;35mBAN NUMBER")
    print("\033[1;31m[ \033[1;34m5 \033[1;31m] \033[1;35mBYPASS NUMBER                 \033[1;31m[ \033[1;34m6 \033[1;31m] \033[1;35mABOUT TOLLS")
    print(" ")
    print("[ E ] Type 0 to exit the tolls ")
    print(" ")


menu()
option = int(input("\033[1;32m[ + ] ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴘᴛɪᴏɴ : "))   


while option != 0:
    if option == 1:
        print(" ")
        print("FACEBOOK methods for jacking account first download password reset from our official app and then send requste to owner and then read the rules how to jack and boom !")
    elif option == 2:
        instagram = input("[ - ] Enter target account with @ : ")
        instagram = input("[ - ] conform the target without @ : ")
        conf = input("[ ! ] Are you ready to mass report y/n : ")
        while conf.lower() not in ("y", "n"):
            conf = input("[ ! ] Are you ready to mass report y/n : ")
        if conf == "n":
            print()
            print("[ | ] Canceled mass report"+instagram)
            break
        if conf == "y":
            print("")
            print("[ - ] Mass reporting .....")

            time.sleep(50)

            print("[ | ] The account has been mass reported now make method to ban it !")
            break
    elif option == 3:
        print(" ")
        print("paid")
    elif option == 4:
        county = input("\033[1;34m[ \033[1;36m= ] Enter the country code + : ")
        print(" ")
        number = input("\033[1;34m[ \033[1;36m= ] Enter victim's number : ")
        print(" ")
        conform = input("\033[1;34m[ \033[1;36m! ] Are you conform to ban this number y/n : ")
        while conform.lower() not in ("y", "n"):
             conform = input("[ ! ] Are you conform to ban this number y/n : ")
        if conform == "n":
            print()
            print("[ ! ] Canceled ban !!")
            break
        if conform == "y":
            print(" ")
            print("\033[1;34m[ \033[1;36m| ] THE NUMBER HAS STARTED PUNISHING : +"+county +number)
            time.sleep(12)  

            print(" ")
            print("\033[1;34m[ \033[1;36m| ] Number was locked by ixmcb tolls ")
            break
    elif option == 5:
        print(" ")
        county = input("\033[1;34m[ \033[1;36m= ] Enter the country code + : ")
        print(" ")
        number = input("\033[1;34m[ \033[1;36m= ] Enter victim's number : ")
        print(" ")
        conform = input("\033[1;34m[ \033[1;36m! ] Are you conform to bypass y/n : ")
        while conform.lower() not in ("y", "n"):
             conform = input("[ ! ] Are you conform bypass y/n : ")
        if conform == "n":
            print()
            print("{ + } WE HAVE CANCELED BYPASS")
            print(" ")
            break
        if conform == "y":
            print()
            print("[ - ] GETING THE NUMBER READY")
            time.sleep(12)
            print()
            print("[ = ] GOT THE CODE ")
            print()
            print("[ - ] YOUR CODE IS : ",randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

    elif option == 6:
        print(" ")
        print("THE TOLLS IS FOR FUN AND MAKE SURE TO USE THEM AS FUN ONLY. THE TOLLS ARE MAINLY FOR BAN A NUMBER MASS REP ON INSTARAM AND MANY MORE ADD SOON IN VERISON 3.5.TOLLS MADE BY IXMCB")
    else:
        print(" ")
        print("[ ! ] INVALID OPTION ")

    print()
    menu()
    option = int(input("\033[1;32m[ + ] ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴘᴛɪᴏɴ : "))           

print("[ ⚠ ] Exited")    
