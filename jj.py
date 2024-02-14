from tqdm import tqdm , trange
from tqdm import tqdm
import time
import os
import sys
from random import randint
from time import sleep

clear = lambda: os.system('cls')
clear()

print("\033[1;36m[ X ] Connecting To Server​ ")

time.sleep(5)

print("\033[1;36m[ X ] Connected To Server")

time.sleep(5)


with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)

clear = lambda: os.system('cls')
clear()


logo = '''
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
|                                                                                    |
|           DEVLOPER : IXMCB                                                         |         
|                                                       INSTAGRAM : @ixmcb           |
|           PROGRAM : Whats App Tool 1.4                                             |      
|                                                                                    |         
|           GITHUB : Not Allowed To Show                                             |  
|                                                                                    |
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|                                                                        

'''
print(logo)
print("                                          [Whats App V 1.4]")





name = input("[ \033[1;31m- \033[1;36m] What is your Name : ")


password = input("[ \033[1;31m- \033[1;36m] Enter the password : ")


if password == "hty":
    print(" ")
    print(" Welcome "+   name)
else:
    print("Sorry try again !")
    sys.exit(666)

print(" ")
print("[ ✓ ] Logined ✓ ")
print("[ ✓ ] No Error ✓ ")

def menu():
    print(" ")
    print("--- [ 1 ] Thor || Whats App lock                  ")
    print("--- [ 2 ] Thor || Update                          ")
    print("--- [ 3 ] Thor || About               ")
    print("--- [ 0 ] Thor || Exit                ")
    print(" ")


menu()
option = int(input("\033[1;32m----> Enter The Suitable Option >>> "))   


while option != 0:
    if option == 1:
        clear = lambda: os.system('cls')
        clear()   
        print(logo)
        county = input("[ - ] Enter The Country Code >>> " )
        number = input("[ - ] Enter The Number >>> ")
        print("")
        clear = lambda: os.system('cls')
        clear()
        print(logo)
        for x in range(1,11):
            for i in ("\\", "|", "/", "-"):
                sleep(0.2)
                if x == 10:
                    print(' ',end='')
                    break
                else:
                    print('---- Connecting '+i,end='\r')

        conform = input("---- Please Conform Once y/n >>> ")
        while conform.lower() not in ("y", "n"):
            conform = input("---- Please Conform Once y/n >>> ")
        if conform == "n":
            print('')
            print("Conformation Denied")
        if conform == "y":
            clear = lambda: os.system('cls')
            clear()
            print(logo)
            for x in range(1,11):
                for i in ("\\", "|", "/", "-"):
                    sleep(0.2)
                    if x == 15:
                        print(' ',end='')
                        break
                    else:
                        print('---- Locking Number '+i,end='\r')
        print(" Number Locked +"+county +number)
        time.sleep(8)
    elif option == 2:
        print(" ")
        clear = lambda: os.system('cls')
        clear()
        for x in range(1,11):
            for i in ("\\", "|", "/", "-"):
                sleep(0.2)
                if x == 16:
                    print('No Updates Found ', end='')
                    break
                else:
                    print("---- Finding The Latest Update "+i,end='\r')
        print("No Updates Found")
        time.sleep(4)
        clear = lambda: os.system('cls')
        clear()
        print(logo)
    elif option == 3:
        print(" This Tool Is For Ethical Puroposes Made By Thor . We Are Working On V.15 Thank You .")
    else:
        print(" ")
        print("[ ! ] Invalid Option ")

    print()
    menu()
    option = int(input("\033[1;32m----> Enter The Suitable Option >>> "))           

print("[ + ] Exited")    
