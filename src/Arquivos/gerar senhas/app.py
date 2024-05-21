from uteis import apresentarprograma, cores, escolhasenha1, escolhasenha2 , escolhasenha3, gerar_senha_aleatoria

def escolhesenha():
    apresentarprograma()
    print("ao programa de Gerar senhas - \033[1;35mPara finalizar o programa digite 'Sair' ou '3' \033[m")
    while True:
        opcoes = input("""\033[1;35mMenu de opções:\n[ 1 ] Escolher o que vai ter na senha\n[ 2 ] Gerar senha aleatoria\n[ 3 ] Sair\nSua opção:\033[m """)
        
        if opcoes in '1':
            cores()
            escolhersenha = input("""\033[1;33mTemos em nosso programa as seguintes opções de senha:\n[ 1 ]Só com letras\n[ 2 ]Com letras e números\n[ 3 ]Com letras,números e caracteres\nSua opção: \033[m""")
            if escolhersenha in '1':
                escolhasenha1()
            elif escolhersenha in '2':
                escolhasenha2()
            else:
                escolhasenha3()
        else:
            if opcoes in '3' or opcoes in 'Sairsair':
                exit()
            if opcoes > '3':
                print(f"OPS, não encontramos o número {opcoes} em nossas opções.\nPor favor, repita.")
        if opcoes in '2':
            gerar_senha_aleatoria()
       
escolhesenha()