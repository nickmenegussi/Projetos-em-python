from uteis import apresentar_programa
from random import randint
from time import sleep

# 1. Criar um menu  para que o usuario possa conhecer tambem as opcões.
# adicionar mais coisas

def menu():
    apresentar_programa()
    while True:
        opcao = input("[ 1 ] Conhecer as regras\n[ 2 ] Jogar\nSua opcão: \033[m").strip()
        if opcao in '1':
            print("Bem vindo as regras!")
            print("REGRAS: ")
        elif opcao in '2':
            print("\033[1;32mVAMOS JOGAR!")
            print("Computador escolheu um numero , tente acertar!\033[m")
            jogo()
        elif opcao in 'SAIRSairsair':
            exit()
        else:
            print(F"Não encontramos o valor {opcao} na gama de opções.")

def nova_partida():
    while True:
        r = input("\033[1;33mDeseja continuar? [S/N] \033[m")

        if r not in 'SsNn':
            print(f"\033[1;31mOpção {r} inválida! por favor digite uma válida\033[m")
        elif r in 'Ss':
            return jogo() # return funciona igual um break
        else:
            break

# 2. Computador irá escolher um number a 0 and 10 e o usuário tem 5 tentative para advinhar o número
def jogo():
    sorteador = randint(0, 10)
    opcao = int(input("Qual é a sua opção of jogada? "))
    
    # ______________________ Checando vitoria ou derrorta ______________________
    if opcao == sorteador:
        print(f"\033[1;31mSorteador sorteou: {sorteador}\033[m")
        print(f"\033[1;32mVoce escolheu: {opcao}\033[m")
        print("\033[1;32mVoce Acertou\033[m")
    else:
        print(f"\033[1;31mSorteador sorteou: {sorteador}")
        print(f"\033[1;32mVoce escolheu: {opcao}\033[m")
        print("\033[1;31mVoce Errou\033[m")

    nova_partida()

menu()

# Limitar Tentativas: Você mencionou que o jogador tem 5 tentativas para adivinhar o número, mas no código atual só há uma tentativa. Você pode adicionar um loop para permitir ao jogador tentar novamente até que ele adivinhe corretamente ou até que as tentativas acabem.