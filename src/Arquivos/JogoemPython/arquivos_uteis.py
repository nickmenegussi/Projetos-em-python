from pyfiglet  import Figlet as fg
from termcolor import colored

def apresentar_programa(texto):
    texto = fg(font="standard")
    print(colored(texto.renderText(" Bem vindo"), 'blue'))

def digitar_textos_repetitivos(palavra):
    return print(palavra)

