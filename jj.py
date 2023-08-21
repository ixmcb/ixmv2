from tqdm import tqdm , trange
import time
import os
import sys

clear

print("\033[1;36m.[INTERNET ONLINE.... !]")

time.sleep(5)

print("\033[1;36m.[CHECKING SOME ERRORS.... !]")

time.sleep(5)


with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)








logo = '''
  \033[1;37m ######   ##      ##  ###  #######  #######  ###  ##  #######  ##  ### 
 \033[1;34m ##  ##   ##      #######    ###    ##   ##  ###  ##    ###    ##  ### 
 \033[1;34m ##  ##   ##      #######    ###    ##       ###  ##    ###    ##  ### 
 \033[1;34m #######  ###      ### ###    ###    ## ####  #######    ###    ####### 
 \033[1;34m ###  ##  ###      ##  ###    ###    ##  ###  ###  ##    ###      ###   
 \033[1;34m ###  ##  ###      ##  ###    ###    ##  ###  ###  ##    ###      ###   
 \033[1;37m ###  ##  ######   ##  ###  #######  #######  ###  ##    ###      ###   
                                                                        

'''
print(logo)
print("                                          [ALMIGHTY EMPIRE TEAM TOLLS !!]")






name = input("What is your name : ")


password = input("Enter the passowrd : ")

if password == "hty":
    print(" WELCOME"+   name)
else:
    print("Sorry try again !")
    sys.exit(666)

def menu():
    print("\033[1;31m[1] \033[1;35mFACEBOOK")
    print("\033[1;31m[2] \033[1;35mINSTAGRAM]")
    print("\033[1;31m[3] \033[1;35mHACK 2K13")
    print("\033[1;31m[4] \033[1;35mBAN NUMBER")
    print("\033[1;31m[5] \033[1;35mPROTECT NUMBER")
    print("\033[1;31m[0] \033[1;35mALMIGHTY EMPIRE EXIT")


menu()
option = int(input("\033[1;32mEnter your option : "))   


while option != 0:
    if option == 1:
        print("FACEBOOK methods for jacking account first download password reset from our official app and then send requste to owner and then read the rules how to jack and boom !")
    elif option == 2:
        print("hello world")
    elif option == 3:
        print("btw who")
    elif option == 4:
        number = input("Enter victim's number : ")
        number = input("Conform the number : ")
        conform = input("Are you conform to ban this number y/n : ")
        while conform.lower() not in ("y", "n"):
             conform = input("Are you conform to ban this number y/n : ")
        if conform == "n":
            print()
            print("canceled ban !!")
            break
        if conform == "y":
            print()
            print("banning the number will take up to 2 minutes !!")

            time.sleep(50)

            print("number banned succesfully")
            break
    elif option == 5:
        print("DOIN IT FOR PAID")
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("\033[1;32mEnter your option : "))           

print("Exited")    
