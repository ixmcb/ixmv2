from tqdm import tqdm , trange
import time
import os
import sys

clear = lambda: os.system('cls')
clear()

print("\033[1;36m[ X ] 🇮​🇳​🇸​🇹​🇱​🇮​🇳​🇬​ 🇫​🇮​🇱​🇪​🇸​ ")

time.sleep(5)

print("\033[1;36m[ X ] 🇫​🇮​🇱​🇪​🇸​ 🇸​🇪​🇨​🇺​🇷​🇪​🇩​ 🇮​🇳​ 🇫​🇴​🇱​🇽​ ")

time.sleep(5)


with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)




logo = '''
\033[1;36m. $$$$$$\  $$\       $$\      $$\ $$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$\     $$\ 
\033[1;31m.$$  __$$\ $$ |      $$$\    $$$ |\_$$  _|$$  __$$\ $$ |  $$ |\__$$  __|\$$\   $$  |
\033[1;31m.$$ /  $$ |$$ |      $$$$\  $$$$ |  $$ |  $$ /  \__|$$ |  $$ |   $$ |    \$$\ $$  / 
\033[1;31m.$$$$$$$$ |$$ |      $$\$$\$$ $$ |  $$ |  $$ |$$$$\ $$$$$$$$ |   $$ |     \$$$$  /  
\033[1;31m.$$  __$$ |$$ |      $$ \$$$  $$ |  $$ |  $$ |\_$$ |$$  __$$ |   $$ |      \$$  /   
\033[1;31m.$$ |  $$ |$$ |      $$ |\$  /$$ |  $$ |  $$ |  $$ |$$ |  $$ |   $$ |       $$ |    
\033[1;31m.$$ |  $$ |$$$$$$$$\ $$ | \_/ $$ |$$$$$$\ \$$$$$$  |$$ |  $$ |   $$ |       $$ |    
\033[1;36m.\__|  \__|\________|\__|     \__|\______| \______/ \__|  \__|   \__|       \__|  
                                                                        

'''
print(logo)
print("                                       [ALMIGHTY EMPIRE TEAM TOLLS VERISON 3.4 !!]")






name = input("[ - ] 𝑾𝑯𝑨𝑻 𝑰𝑺 𝒀𝑶𝑼𝑹 𝑵𝑨𝑴𝑬 : ")


password = input("[ - ] 𝗘𝗡𝗧𝗘𝗥 𝗧𝗛𝗘 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 : ")

if password == "hty":
    print(" WELCOME "+   name)
else:
    print("Sorry try again !")
    sys.exit(666)

def menu():
    print("\033[1;31m[1] \033[1;35mFACEBOOK                   [6] ABOUT")
    print("\033[1;31m[2] \033[1;35mINSTAGRAM")
    print("\033[1;31m[3] \033[1;35mHACK 2K13")
    print("\033[1;31m[4] \033[1;35mBAN NUMBER")
    print("\033[1;31m[5] \033[1;35mPROTECT NUMBER")
    print("\033[1;31m[0] \033[1;35mALMIGHTY EMPIRE EXIT")


menu()
option = int(input("\033[1;32m[ + ] ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴘᴛɪᴏɴ : "))   


while option != 0:
    if option == 1:
        print("FACEBOOK methods for jacking account first download password reset from our official app and then send requste to owner and then read the rules how to jack and boom !")
    elif option == 2:
        instagram = input("Enter target account with @ : ")
        instagram = input("conform the target withouy @ : ")
        conf = input("Are you ready to mass report y/n : ")
        while conf.lower() not in ("y", "n"):
            conf = input("Are you ready to mass report y/n : ")
        if conf == "n":
            print()
            print("canceled mass report"+instagram)
            break
        if conf == "y":
            print("")
            print("mass reporting .....")

            time.sleep(50)

            print("The account has been mass reported now make method to ban it !")
            break
    elif option == 3:
        print("paid")
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
        print("DOING IT FOR PAID")
    elif option == 6:
        print("THE TOLLS IS FOR FUN AND MAKE SURE TO USE THEM AS FUN ONLY. THE TOLLS ARE MAINLY FOR BAN A NUMBER MASS REP ON INSTARAM AND MANY MORE ADD SOON IN VERISON 3.5.TOLLS MADE BY IXMCB")
    else:
        print("[ ! ] INVALID OPTION ")

    print()
    menu()
    option = int(input("\033[1;32m[ + ] ᴇɴᴛᴇʀ ᴛʜᴇ ᴏᴘᴛɪᴏɴ : "))           

print("Exited")    
