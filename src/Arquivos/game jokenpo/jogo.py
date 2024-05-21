# 1. Importar bibliotecas necessárias
from uteis import apresentar_programa, jokenpo ,  linha
from random import choice

def Menu():
    apresentar_programa()
    print("ao programa de Gerar senhas - \033[1;35mPara finalizar o programa digite 'Sair' ou '3' \033[m")
    print("Escolha uma das opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n[ 3 ] Sair") 

def Jogo():
    Menu()
    # 3. Exibir Variaveis necessárias para rodar o programa
    try:
        while True:
            opcao = str(input("Qual é a sua jogada? "))
            
            if opcao in 'Sairsair' or opcao in '3':
                exit()
            else:
                if opcao != 'Sairsair' or opcao != '3':
                    jokenpo()
                    palavras = ["Pedra", "Papel" ,"Tesoura"]
                    sorteador = ''
                    sorteador += choice(palavras)
                    contadordepontos = 1

                    print(f"\033[1;32mComputador jogou: {sorteador}\033[m")
                    print(f"\033[1;32mJogador jogou: {palavras[int(opcao)]} \033[m")

                    if sorteador == palavras[int(opcao)]:
                        linha()
                        print("\033[1;32mEMPATE!!\033[m")
                        linha()
                    # 3.Inicio ao algoritmo
                        # ________________________________________________Computador jogou Pedra,Tesoura e Papel________________________________________________
                    elif sorteador == 'Pedra' and opcao == '1' or sorteador == 'Papel' and opcao == '2' or sorteador == 'Tesoura' and opcao == '3':
                        linha()
                        print("\033[1;32mJOGADOR VENCEU!!\033[m")
                        linha() 
                    else:
                        linha()
                        print("\033[1;32mCOMPUTADOR VENCEU!!\033[m")
                        linha()
                
    except (ValueError,TypeError):           
        print("\033[131m;Erro de valor.\033[m")       
Jogo()

while 0 > -1:
    print("oi")

    