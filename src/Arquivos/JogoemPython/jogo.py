from arquivos_uteis import apresentar_programa,digitar_textos_repetitivos

vidas = 5

def escopos():
    apresentar_programa(f"Bem vindo ao jogo do Alquimista, Um jogo misterioso e divertido!")
    print("ao programa do Alquimita , Um jogo de história")
    print(f"\033[1;32mIntrodução: Voce é o protagonista, está no início de sua jornada em busca de um tesouro. Ele se depara com três caminhos diferentes para seguir:\033[m")

    nome = str(input("Qual é o seu nome? "))
    jogo(nome)
    imprimir_resultado()


def jogo(nome): 
    global vidas
    try:
        print(f"Bem vindo ao jogo, Sr. {nome}, Espero que aproveite e se diverta com o jogo! ")
        caminho = int(input("\033[1;32mOpções:\n   [ 1 ] - Seguir um caminho perigoso e desconhecido, com a esperança de encontrar respostas mais rapidamente.\n   [ 2 ] - Optar por um caminho mais seguro e conhecido, mas que pode levar mais tempo para alcançar o destino final.\n   [ 3 ] - Unir-se a um grupo de viajantes, que oferece segurança em números, mas também pode ser uma distração para o objetivo principal.\nSua opção: \033[m"))

        if caminho == 1:
            caminho_perigoso(nome)
            vidas -= 1
        elif caminho == 2:
            caminho_seguro(nome)
        elif caminho == 3:
            unir_se_ao_grupo(nome)
        else:
            print("Erro! Digite novamente!")
            jogo()
    except:
        print("Erro de valor, por favor digite novamente")


def caminho_perigoso(nome):
    global vidas
    print(f"\033[1;31mVoce decidiu ir pelo caminho 1. Logo passará por essa breve caminho perigoso e receberá -1 de vida, lembre-se que voce pode recuperar ao longo das opções:\nAo longo da jornada, {nome} (que é voce) conhece a filha do comerciante local e tem duas opções de interação com ela:\033[m")

    caminho_novo = int(input(f"\033[1;34mOpções:\n [ 1 ] - Desenvolver uma amizade sincera com a filha do comerciante, aprendendo valiosas lições sobre empatia e compaixão.\n [ 2 ] - Iniciar um romance apaixonado com a filha do comerciante, enfrentando os desafios e consequências desse relacionamento.\nSua opção: \033[m" ))
    if caminho_novo == 1:
        checkpoint1_missao1(nome)
        vidas += 1
    elif caminho_novo == 2:
        checkpoint2_missao1(nome)
    else:
        print("ERRO! DIGITE NOVAMENTE!")
        caminho_perigoso()
def checkpoint1_missao1(nome):
        global vidas
        print("\033[1;32mCAMINHO SEGURO! MAIS UMA VIDA!\033[m")
        vidas += 1

        print(f"\033[1;32mCheckPoint 1:\nApós querer desenvolver uma amizade sincera voce conhece a filha do comerciante local e tem quatro opções de interação com ela:\033[m")

        caminho_novo = 1
        
        if caminho_novo == 1:
            chekpoint1_final_caminho1_missao1(nome)
        elif caminho_novo == 2:
            chekpoint1_final_caminho2_missao1(nome)
        elif caminho_novo == 3:
            chekpoint1_final_caminho3_missao1(nome)
        elif caminho_novo == 4:
            chekpoint1_final_caminho4_missao1(nome) 
        else:
            print("Erro , digite novamente!")
            checkpoint1_missao1(nome)
def chekpoint1_final_caminho1_missao1(nome):
    global vidas
    print("\033[1;31mCAMINHO PERIGOSO! menos uma vida!")
    print(f"{nome} (voce) e a filha do comerciante decidem investigar a lenda antiga durante o festival em busca de pistas sobre o tesouro. Voces aprendem com os moradores locais sobre as histórias e mitos que cercam o tesouro escondido. No entanto, as informações são vagas e contraditórias, levando-os a se questionar sobre a veracidade da lenda.\033[m")

    vidas -= 1

def chekpoint1_final_caminho2_missao1(nome):
    print("\033[1;31mCAMINHO FORA DO TESOURO! menos uma vida!\033[m")
    print(f"Santiago escolhe ajudar a filha do comerciante a resolver seu problema pessoal, priorizando sua amizade em relação à busca pelo tesouro. Voces passam tempo juntos, discutindo os desafios que ela enfrenta e encontrando soluções juntos. ")
    vidas-= 1

def chekpoint1_final_caminho3_missao1(nome):
    global vidas
    print("\033[1;32mCAMINHO SEGURO! mais uma vida!\033[m")
    vidas += 1

    print(f"Enquanto exploram, Santiago e a filha do comerciante encontram o artefato raro relacionado ao tesouro. Vices ficam emocionados com a descoberta, mas também percebem que esse artefato pode atrair a atenção de outros aventureiros e até mesmo de caçadores de tesouros inescrupulosos. .")

def chekpoint1_final_caminho4_missao1(nome):
    print("\033[1;32mCAMINHO SEGURO! mais uma vida!\033[m")
    vidas += 1
    print(f"Ao descobrir que a filha do comerciante possui conhecimento valioso sobre as armadilhas que protegem o tesouro, {nome} (voce) e ela precisam tomar uma decisão importante. Voces debatem os prós e contras de compartilhar esse conhecimento com outros aventureiros ou mantê-lo em segredo para benefício próprio. ")

def checkpoint2_missao1(nome):
        global vidas
        print(f"opcao segura! mais uma vida: total {vidas}")
        vidas += 1

        print(f"CheckPoint 2: Sr.{nome} escolheu a opção de romance, voce e a filha do comerciante enfrentam um desafio inesperado:")
        caminho_novo = int(input("Opções:\n [ 1 ] Voce contrai uma doença que lhe coloca em risco sua busca pelo tesouro, mas voce encontra força para superar a adversidade e continuar em sua jornada.\n [ 2 ] - Santiago se afasta da busca pelo tesouro, dedicando-se exclusivamente à filha e à sua recuperação.\nSua opção: "))
        if caminho_novo == 1:
            checkpoint3_missao1(nome)
        elif caminho_novo == 2:
            print("\033[1;31mCAMINHO PERIGOSO! MENOS UMA VIDA!\033[m")
            vidas += 1
            print("Voce opta por se afastar da busca pelo tesouro, priorizando a filha e sua recuperação. Ele dedica tempo integral para ajudá-la a superar seus desafios pessoais, oferecendo apoio inabalável e amor. Enquanto cuida dela, Santiago redescobre o significado da compaixão e da família. ")
        else:
            print("Erro , digite novamente!")
            checkpoint2_missao1()

def checkpoint3_missao1(nome):
        global vidas
        print(f"CheckPoint 3:Depois de enfrentar essa reviravolta, {nome} (voce) encontra novos aliados e deve decidir como agir ao longo do caminho:")
        caminho_novo = int(input("Opções:\n [ 1 ] - Ser generoso e ajudar os outros em sua própria busca, mesmo que isso signifique sacrificar um pouco de sua própria busca pelo tesouro.\n [ 2 ] - Manter o foco em seu objetivo e não se envolver com os problemas dos outros, priorizando sua jornada.\nSua opção:  "))
        if caminho_novo == 1:
            checkpoint4_missao1(nome)
        elif caminho_novo == 2:
            checkpoint5_missao1(nome)
        else:
            print("erro! digite novamente")
            checkpoint3_missao1(nome)

def checkpoint4_missao1(nome):
        global vidas
        print("caminho fora do tesouro! menos uma vida!")
        vidas -= 1
        print(f"CheckPoint 4: À medida que {nome}(voce) se aproxima do destino, voce se depara com o uma pessoa decisiva chamada CRISTIANO RONALDO, uma figura decisiva na jornada:")
        caminho_novo = int(input("Opções\n [ 1 ] - Seguir os ensinamentos do Alquimista e mergulhar em uma jornada de autoconhecimento e transformação.\n [ 2 ] - Rejeitar os ensinamentos do Alquimista e continuar a busca pelo tesouro como antes, enfrentando as consequências de sua escolha.\nSua opção:  "))
        if caminho_novo == 1:
            checkpoint5_missao1(nome)
        elif caminho_novo == 2:
            checkpoint6_missao1(nome)
        else:
            print("Erro , digite uma opcao valida! ")
            checkpoint4_missao1()

def checkpoint5_missao1(nome):
        global vidas
        print("caminho para o tesouro! mais uma vida!")
        vidas += 1
    
        print(f"Checkpoint 5: {nome} descobre que o tesouro pode estar escondido em uma cidade misteriosa e isolada. Ele tem três possibilidades para abordar essa descoberta:" , end=" ")
        caminho_novo = int(input("Opções:\n  [ 1 ] - Aprender com os Encontros Significativos.\n  [ 2 ] - Abraçar a Jornada Interior.\n  [ 3 ] - Transformar Desafios em Oportunidades de Crescimento.\nSua opção: "))
        if caminho_novo == 1:
            print("\033[1;32mCAMINHO SEGURO! MAIS UMA VIDA\033[m")
            vidas += 1
            print(f"Voce decide mergulhar de cabeça nos ensinamentos do Alquimista. Ele passa tempo meditando, refletindo sobre suas experiências e buscando compreender seus próprios pensamentos e emoções. Ao longo dessa jornada interior, ele começa a descobrir novas camadas de si mesmo e a encontrar respostas para perguntas que antes o desconcertavam.")
        elif caminho_novo == 2:
            print("\033[1;31mCAMINHO MEIO-ARRISCADO! MENOS UMA VIDA\033[m")
            vidas += 1
            print(f"Guiado pelos ensinamentos do Alquimista, Voce começa a observar a natureza ao seu redor com um olhar mais atento. Ele aprende a encontrar símbolos e mensagens nos elementos naturais, como o movimento das águas, a posição das estrelas e os ventos que sopram. Essa conexão com a natureza o ajuda a ganhar perspectiva sobre sua própria jornada.")
        elif caminho_novo == 3:
            print("\033[1;32mCAMINHO SEGURO! MAIS UMA VIDA\033[m")
            vidas += 1
            print(f"Voce se dedica a criar conexões mais profundas com as pessoas que encontra ao longo de sua jornada. Ele busca entender as histórias e os ensinamentos de cada indivíduo que cruza seu caminho, vendo em cada encontro uma oportunidade de crescimento e aprendizado. Essas interações moldam sua visão de mundo e expandem sua compreensão.")
        else:
            if caminho_novo != 1 or caminho_novo != 2:
                print("ERRO! DIGITE NOVAMENTE")

                caminho_novo = int(input("Opções:\n  [ 1 ] - Aprender com os Encontros Significativos.\n  [ 2 ] - Abraçar a Jornada Interior.\n  [ 3 ] - Transformar Desafios em Oportunidades de Crescimento.\nSua opção: "))
        
def checkpoint6_missao1(nome):
        global vidas

        print(f"Checkpoint 6:{nome} descobre que o tesouro pode estar escondido em uma cidade misteriosa e isolada. Ele tem três possibilidades para abordar essa descoberta:")
        caminho_novo = int(input("Opções:\n [ 1 ] -Entrar furtivamente na cidade, evitando ser detectado pelas autoridades locais.\n[ 2 ] - Fazer amizade com os habitantes locais, ganhando sua confiança para obter informações valiosas sobre o tesouro.\n [ 3 ] - Buscar ajuda de um guia experiente que conhece os segredos e armadilhas da cidade.\nSua opção: "))
        if caminho_novo == 1:
            print("\033[1;31mCAMINHO PERIGOSO! MENOS UMA VIDA\033[m")
            vidas -= 1
            print("Voce entra furtivamente na cidade, evitando as autoridades. Explorando com cautela, ele desvenda pistas e símbolos que o levam a uma sala subterrânea, onde encontra um tesouro de artefatos preciosos e um pergaminho com sabedoria ancestral. Compartilha a história com os locais, inspirando-os.")
        elif caminho_novo == 2:
            print("\033[1;32mCAMINHO SEGURO! MAIS UMA VIDA\033[m")
            vidas += 1
            print("Voce cria laços com os habitantes, ganhando confiança. Guiado por suas conexões, encontra o tesouro não em ouro, mas em arte e tradições culturais. A cidade renova-se, unida pela jornada compartilhada.")
        elif caminho_novo == 3:
            print("\033[1;32mCAMINHO SEGURO! MAIS UMA VIDA!\033[m")
            vidas += 1
            print("Com a ajuda de um guia, Voce navega pela cidade e descobre um manuscrito antigo com ensinamentos profundos sobre autoconhecimento. Compartilha essa sabedoria com o guia e ambos partem transformados.")
        
        if caminho_novo != 1 or caminho_novo != 2 or caminho_novo != 3:
            print("ERRO, DIGITE NOVAMENTE!", end=" ")

            caminho_novo = int(input("Opções:\n [ 1 ] -Entrar furtivamente na cidade, evitando ser detectado pelas autoridades locais.\n[ 2 ] - Fazer amizade com os habitantes locais, ganhando sua confiança para obter informações valiosas sobre o tesouro.\n [ 3 ] - Buscar ajuda de um guia experiente que conhece os segredos e armadilhas da cidade.\nSua opção: "))
                        
def caminho_seguro(nome):
    global vidas
    print(f"{nome}, você escolhe o caminho seguro, optando por seguir uma rota mais conhecida e protegida. Sua jornada é mais tranquila, mas ainda há desafios pela frente.")

    print("Enquanto segue pela rota segura, você encontra um misterioso alquimista que oferece conselhos e orientações para a sua busca pelo tesouro. Ele compartilha ensinamentos sobre autoconhecimento e transformação.")

    caminho_novo = int(input("\033[1;34mOpções:\n [ 1 ] - Aceitar os ensinamentos do Alquimista e aplicá-los à sua jornada.\n [ 2 ] - Ignorar os conselhos do Alquimista e continuar seguindo a rota segura.\nSua opção: \033[m"))
    
    if caminho_novo == 1:
        print("Você decide aceitar os ensinamentos do Alquimista e mergulhar em uma jornada de autoconhecimento. À medida que aplica os ensinamentos à sua busca, você descobre novas perspectivas e supera obstáculos internos.")
        checkpoint_final_alquimista(nome)
    elif caminho_novo == 2:
        print("Você opta por ignorar os conselhos do Alquimista e continuar seguindo a rota segura. Embora sua jornada seja mais tranquila, você sente que está perdendo a oportunidade de crescimento pessoal.")
        checkpoint_final_continuar(nome)
    else:
        print("ERRO! Opção inválida. Escolha novamente.")
        caminho_seguro(nome)  # Retorna à função para escolher uma opção válida.

def checkpoint_final_alquimista(nome):
    global vidas
    print("\033[1;32mCHECKPOINT FINAL - FINAL COM O ALQUIMISTA\033[m")
    print(f"Parabéns, {nome}! Você completa a jornada com uma mente e coração transformados pelos ensinamentos do Alquimista. Você encontra o tesouro e descobre que a verdadeira recompensa está na jornada interior que você trilhou.")
    vidas += 1

def checkpoint_final_continuar(nome):
    print("\033[1;31mCHECKPOINT FINAL - FINAL AO CONTINUAR\033[m")
    print(f"Infelizmente, {nome}, ao continuar seguindo a rota segura sem aplicar os ensinamentos do Alquimista, você chega ao tesouro, mas percebe que algo está faltando. O tesouro em si não traz a satisfação que você esperava.")

def unir_se_ao_grupo(nome):
    global vidas
    print("Você escolhe se unir a um grupo de viajantes em busca do tesouro.")
    print("Você se sente mais seguro em grupo, mas também sabe que pode haver distrações.")
    
    caminho_novo = int(input(("\033[1;35mOpções:\n [ 1 ] - Se juntar ao grupo, confiando na segurança em números...\n [ 2 ] - Optar por seguir sozinho, mantendo o foco na jornada...\nSua opção: \033[m")))

    if caminho_novo == 1:
        vidas += 1  # Aumentar uma vida como recompensa por se juntar ao grupo
        print("Você decide se unir ao grupo de viajantes. Juntos, vocês enfrentam os desafios e perigos da jornada, compartilhando conhecimento e experiências.")

        # Criar subperguntas ou opções adicionais aqui, por exemplo:
        caminho_novo = int(input("\033[1;36mO grupo decide explorar uma caverna misteriosa que parece conter pistas sobre o tesouro. Você deseja entrar na caverna com o grupo?\n [ 1 ] - Sim, entrar na caverna.\n [ 2 ] - Não, esperar do lado de fora.\nSua opção: \033[m"))
        
        if caminho_novo == 1:
            # Lógica para a escolha de entrar na caverna com o grupo
            print("Você entra na caverna junto com o grupo. Dentro dela, vocês encontram inscrições antigas que indicam o próximo passo da jornada.")
            # Restante da lógica...
        elif caminho_novo == 2:
            # Lógica para a escolha de esperar do lado de fora
            print("Você decide esperar do lado de fora da caverna enquanto o grupo explora. Você percebe movimentação estranha nas sombras...")
            # Restante da lógica...
        else:
            print("ERRO! DIGITE NOVAMENTE!")
            
    elif caminho_novo == 2:
        vidas -= 1  # Diminuir uma vida como consequência de seguir sozinho
        print("Você opta por seguir sozinho em sua busca pelo tesouro. Embora seja mais arriscado, você mantém o foco em sua jornada e avança com determinação.")
        # Criar subperguntas ou opções adicionais aqui, por exemplo:
        caminho_novo = int(input(("\033[1;37mEnquanto segue sozinho, você se depara com um cruzamento que oferece duas direções.\n [ 1 ] - Escolher a trilha da esquerda.\n [ 2 ] - Escolher a trilha da direita.\nSua opção: \033[m")))
        
        if caminho_novo == 1:
            checkpoint_final_solitario(nome)
            print("Você escolhe a trilha da esquerda. Ela leva você a uma antiga ruína, onde você encontra uma inscrição enigmática que parece ser uma pista.")
        elif caminho_novo == 2:
            checkpoint_final_colaborativo()
            print("Você escolhe a trilha da direita. Ela leva você a um desfiladeiro perigoso, onde você precisa usar suas habilidades para atravessá-lo.")

        else:
            print("ERRO! DIGITE NOVAMENTE!")
            
    else:
        print("ERRO! DIGITE NOVAMENTE!")
        unir_se_ao_grupo(nome)


def checkpoint_final_solitario(nome):
    global vidas
    print("\033[1;31mCHECKPOINT FINAL - FINAL SOLITÁRIO\033[m")
    print(f"Infelizmente, {nome}, você percebe tarde demais que alguns membros do grupo têm intenções egoístas e traiçoeiras. Eles o traem e pegam o tesouro para si. Embora você tenha enfrentado muitos desafios, a ganância prevalece. A jornada termina de forma amarga.")
    vidas -= 1

def checkpoint_final_colaborativo(nome):
    global vidas
    print("\033[1;34mCHECKPOINT FINAL - FINAL COLABORATIVO\033[m")
    print(f"Parabéns, {nome}! Você completou a jornada em um espírito de cooperação e colaboração com o grupo. Juntos, vocês encontram o tesouro e compartilham a recompensa. Sua jornada é marcada por amizades duradouras e realizações significativas.")
    vidas += 1

def imprimir_resultado():
    global vidas
    if vidas > 5:
        print(f"\033[1;32mVITÓRIA! Parabéns por completar a jornada com sucesso!Com um total de {vidas} vidas\033[m")
    else:
        print(f"\033[1;31mDERROTA! Infelizmente, não foi possível alcançar o tesouro desta vez.Pois voce ficou com um total de {vidas} vidas e o maximo era 5!\033[m")


escopos()