import pyfiglet
from termcolor import colored


def linha():
    print("\033[1;32m=\033[m"*25)


def apresentar_programa():
    print(colored(pyfiglet.figlet_format("Bem vindo"), 'red'))
    print("\033[1;34mao programa Acerte um Número -  Para finalizar o programa digite 'Sair' ou '3'\033[m")

