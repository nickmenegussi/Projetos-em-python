import pyfiglet

def linha():
    print("\033[1;32m=\033[m"*25)

def apresentar_programa():
    print(pyfiglet.figlet_format("Hello wolrd"))

def jokenpo():
    from time import sleep
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")

apresentar_programa()

print()