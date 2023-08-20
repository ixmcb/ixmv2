from tqdm import tqdm , trange
import time

print("[INTERNET ONLINE.... !]")

time.sleep(5)

print("[CHECKING SOME ERRORS.....]")

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


password ="hty"

for i  in range(3):
    pwd = input("Enter the passowrd to contunue : ")
    j=3
    if(pwd==password) :
        print(" WELCOME "+name)
        break 
    else:
        print("Incorrect passowrd sorry try again chances left =",j-1)
        continue

def menu():
    print("[1] FACEBOOK")
    print("[2] INSTAGRAM]")
    print("[3] HACK 2K13")
    print("[0] ALMIGHTY EMPIRE EXIT")


menu()
option = int(input("Enter your option : "))   


while option != 0:
    if option == 1:
        print("FACEBOOK methods for jacking account first download password reset from our official app and then send requste to owner and then read the rules how to jack and boom !")
    elif option == 2:
        print("hello world")
    elif option == 3:
        print("btw who")
    else:
        print("Invalid option")

    print()
    menu()
    option = int(input("Enter your option : "))           

print("Exited")    