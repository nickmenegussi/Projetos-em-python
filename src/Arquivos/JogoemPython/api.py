import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

vidas = 5
nome_usuario = ""
root = None


def criar_interface_grafica():
    global nome_usuario, root

    def iniciar_jogo():
        global nome_usuario
        nome_usuario = simpledialog.askstring(
            "Nome de Usuário", "Digite seu nome:")
        if nome_usuario:
            mensagem.config(
                text=f'Bem-vindo, {nome_usuario}!\nIntrodução: Você é o protagonista, está no início de sua jornada em busca de um tesouro. Ele se depara com três caminhos diferentes para seguir:', fg='green', font=('Times New Roman', 12))
            criar_interface_opcoes()

    root = tk.Tk()
    root.title("Jogo do Alquimista")
    root.geometry("900x700")
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=canvas.yview)
    texto = tk.Label(root, text="Bem vindo ao jogo do Alquimista, Um jogo misterioso e divertido!", font=(
        'Times New Roman', 16))
    texto_introducao = tk.Label(
        root, text='Você está no jogo do Alquimista, Um jogo de história\n', font=('Times New Roman', 12))

    texto.pack(pady=15)
    texto_introducao.pack()

    button1 = tk.Button(root, text="Cadastrar nome", command=iniciar_jogo)
    button1.pack(anchor='center', padx=10, pady=5)

    mensagem = tk.Label(root, text="", font=('Times New Roman', 12))
    mensagem.pack()

    


def criar_interface_opcoes():
    label_opcoes = tk.Label(root, text="Opções:\n   [ 1 ] - Seguir um caminho perigoso e desconhecido, com a esperança de encontrar respostas mais rapidamente.\n   [ 2 ] - Optar por um caminho mais seguro e conhecido, mas que pode levar mais tempo para alcançar o destino final.\n   [ 3 ] - Unir-se a um grupo de viajantes, que oferece segurança em números, mas também pode ser uma distração para o objetivo principal.\nSua opção:")
    label_opcoes.pack(pady=15)

    button_caminhoperigo = tk.Button(
        root, text='Caminho 1', fg='blue', width=10, command=lambda: caminho_perigoso(nome_usuario))
    button_caminhoseguro = tk.Button(
        root, text='Caminho 2', fg='blue', width=10, command=lambda: caminho_seguro())
    button_caminhouniao = tk.Button(
        root, text='Caminho 3', fg='blue', width=10, command=lambda: unir_se_ao_grupo())

    button_caminhoperigo.pack()
    button_caminhoseguro.pack()
    button_caminhouniao.pack()


def caminho_perigoso(nome_usuario):
    global vidas
    label_caminho_novo = tk.Label(
        root, text=f"Você decidiu ir pelo caminho 1. Logo passará por essa breve caminho perigoso e receberá -1 de vida, lembre-se que você pode recuperar ao longo das opções:\nAo longo da jornada, {nome_usuario} (que é você) conhece a filha do comerciante local e tem duas opções de interação com ela: ")
    label_caminho_novo.pack()

    label_caminho_novo = simpledialog.askinteger(
        "Escolha sua opção", f"Opções:\n [ 1 ] - Desenvolver uma amizade sincera com a filha do comerciante, aprendendo valiosas lições sobre empatia e compaixão.\n [ 2 ] - Iniciar um romance apaixonado com a filha do comerciante, enfrentando os desafios e consequências desse relacionamento.\nSua opção: ")

    if label_caminho_novo == 1:
        vidas += 1
        checkpoint1_missao1(nome_usuario)
    elif label_caminho_novo == 2:
        checkpoint2_missao1(nome_usuario)
    else:
        label_erro = tk.Label(root, text="ERRO! DIGITE NOVAMENTE!")
        label_erro.pack()
        caminho_perigoso(nome_usuario)


def checkpoint1_missao1(nome_usuario):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"CheckPoint 1:\nApós querer desenvolver uma amizade sincera voce conhece a filha do comerciante local e tem quatro opções de interação com ela:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Desenvolver uma amizade sincera com a filha do comerciante, aprendendo valiosas lições sobre empatia e compaixão.\n"
                                                 " [ 2 ] - Iniciar um romance apaixonado com a filha do comerciante, enfrentando os desafios e consequências desse relacionamento.\n"
                                                 " [ 3 ] - Ajudar a filha do comerciante a resolver seu problema pessoal, priorizando sua amizade em relação à busca pelo tesouro.\n"
                                                 " [ 4 ] - Compartilhar com a filha do comerciante o conhecimento valioso sobre as armadilhas que protegem o tesouro, discutindo os prós e contras dessa decisão.")

    if label_caminho_novo == 1:
        chekpoint1_final_caminho1_missao1(nome_usuario)
    elif label_caminho_novo == 2:
        chekpoint1_final_caminho2_missao1(nome_usuario)
    elif label_caminho_novo == 3:
        chekpoint1_final_caminho3_missao1(nome_usuario)
    elif label_caminho_novo == 4:
        chekpoint1_final_caminho4_missao1(nome_usuario)
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        checkpoint1_missao1(nome_usuario)


def chekpoint1_final_caminho1_missao1(nome_usuario):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO PERIGOSO! menos uma vida!")
    label_checkpoint.pack()
    vidas -= 1

    mensagem = tk.Label(root, text=f"{nome_usuario} (voce) e a filha do comerciante decidem investigar a lenda antiga durante o festival em busca de pistas sobre o tesouro. Vocês aprendem com os moradores locais sobre as histórias e mitos que cercam o tesouro escondido. No entanto, as informações são vagas e contraditórias, levando-os a se questionar sobre a veracidade da lenda.")
    mensagem.pack()
    imprimir_resultado()


def chekpoint1_final_caminho2_missao1(nome_usuario):
    global vidas
    label_checkpoint = tk.Label(
        root, text="CAMINHO FORA DO TESOURO! menos uma vida!")
    label_checkpoint.pack()
    vidas -= 1

    mensagem = tk.Label(root, text=f"Santiago escolhe ajudar a filha do comerciante a resolver seu problema pessoal, priorizando sua amizade em relação à busca pelo tesouro. Vocês passam tempo juntos, discutindo os desafios que ela enfrenta e encontrando soluções juntos.")
    mensagem.pack()
    imprimir_resultado()


def chekpoint1_final_caminho3_missao1(nome_usuario):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! mais uma vida!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(root, text=f"Enquanto exploram, Santiago e a filha do comerciante encontram o artefato raro relacionado ao tesouro. Vocês ficam emocionados com a descoberta, mas também percebem que esse artefato pode atrair a atenção de outros aventureiros e até mesmo de caçadores de tesouros inescrupulosos.")
    mensagem.pack()
    imprimir_resultado()


def chekpoint1_final_caminho4_missao1(nome_usuario):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! mais uma vida!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"Ao descobrir que a filha do comerciante possui conhecimento valioso sobre as armadilhas que protegem o tesouro, {nome_usuario} (voce) e ela precisam tomar uma decisão importante. Vocês debatem os prós e contras de compartilhar esse conhecimento com outros aventureiros ou mantê-lo em segredo para benefício próprio.")
    mensagem.pack()
    imprimir_resultado()


def checkpoint2_missao1(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"CheckPoint 2:\n{nome} escolheu a opção de romance, você e a filha do comerciante enfrentam um desafio inesperado:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Você contrai uma doença que coloca em risco sua busca pelo tesouro, mas encontra forças para superar a adversidade e continuar em sua jornada.\n"
                                                " [ 2 ] - Santiago se afasta da busca pelo tesouro, dedicando-se exclusivamente à filha e à sua recuperação.\nSua opção: ")

    if label_caminho_novo == 1:
        checkpoint3_missao1(nome)
    elif label_caminho_novo == 2:
        print("CAMINHO PERIGOSO! MENOS UMA VIDA!")
        vidas -= 1
        print(
            "Você opta por se afastar da busca pelo tesouro, priorizando a filha e sua recuperação. Ele dedica tempo integral para ajudá-la a superar seus desafios pessoais, oferecendo apoio inabalável e amor. Enquanto cuida dela, Santiago redescobre o significado da compaixão e da família.")
        imprimir_resultado()
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        checkpoint2_missao1(nome)


def checkpoint3_missao1(nome):
    global vidas
    label_checkpoint = tk.Label(
        root, text="CAMINHO MEIO-ARRISCADO! MENOS UMA VIDA!")
    label_checkpoint.pack()
    vidas -= 1

    mensagem = tk.Label(
        root, text=f"CheckPoint 3:\n{nome} enfrenta uma reviravolta e encontra novos aliados, devendo decidir como agir ao longo do caminho:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Ser generoso e ajudar os outros em sua própria busca, mesmo que isso signifique sacrificar um pouco de sua própria busca pelo tesouro.\n"
                                                " [ 2 ] - Manter o foco em seu objetivo e não se envolver com os problemas dos outros, priorizando sua jornada.\nSua opção:  ")

    if label_caminho_novo == 1:
        checkpoint4_missao1(nome)
    elif label_caminho_novo == 2:
        checkpoint5_missao1(nome)
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        checkpoint3_missao1(nome)


def checkpoint4_missao1(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO FORA DO TESOURO! MENOS UMA VIDA!")
    label_checkpoint.pack()
    vidas -= 1

    mensagem = tk.Label(
        root, text=f"CheckPoint 4:\nÀ medida que {nome} se aproxima do destino, ele se depara com uma pessoa decisiva chamada CRISTIANO RONALDO, uma figura decisiva na jornada:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Seguir os ensinamentos do Alquimista e mergulhar em uma jornada de autoconhecimento e transformação.\n"
                                                " [ 2 ] - Rejeitar os ensinamentos do Alquimista e continuar a busca pelo tesouro como antes, enfrentando as consequências de sua escolha.\nSua opção:  ")

    if label_caminho_novo == 1:
        checkpoint5_missao1(nome)
    elif label_caminho_novo == 2:
        checkpoint6_missao1(nome)
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        checkpoint4_missao1(nome)


def checkpoint5_missao1(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO PARA O TESOURO! MAIS UMA VIDA!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"Checkpoint 5:\n{nome} descobre que o tesouro pode estar escondido em uma cidade misteriosa e isolada. Ele tem três possibilidades para abordar essa descoberta:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Aprender com os Encontros Significativos.\n"
                                                " [ 2 ] - Abraçar a Jornada Interior.\n"
                                                " [ 3 ] - Transformar Desafios em Oportunidades de Crescimento.\nSua opção: ")

    if label_caminho_novo == 1:
        label_resultado = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA")
        label_resultado.pack()
        vidas += 1
        label_resultado = tk.Label(root, text=f"{nome} decide mergulhar de cabeça nos ensinamentos do Alquimista. Ele passa tempo meditando, refletindo sobre suas experiências e buscando compreender seus próprios pensamentos e emoções. Ao longo dessa jornada interior, ele começa a descobrir novas camadas de si mesmo e a encontrar respostas para perguntas que antes o desconcertavam.")
        label_resultado.pack()
        imprimir_resultado()
    elif label_caminho_novo == 2:
        label_resultado = tk.Label(root, text="CAMINHO MEIO-ARRISCADO! MENOS UMA VIDA")
        label_resultado.pack()
        vidas -= 1
        label_resultado = tk.Label(root, text=f"Guiado pelos ensinamentos do Alquimista, {nome} começa a observar a natureza ao seu redor com um olhar mais atento. Ele aprende a encontrar símbolos e mensagens nos elementos naturais, como o movimento das águas, a posição das estrelas e os ventos que sopram. Essa conexão com a natureza o ajuda a ganhar perspectiva sobre sua própria jornada.")
        label_resultado.pack()
        imprimir_resultado()
    elif label_caminho_novo == 3:
        label_resultado = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA")
        label_resultado.pack()
        vidas += 1
        label_resultado = tk.Label(root, text=f"{nome} se dedica a criar conexões mais profundas com as pessoas que encontra ao longo de sua jornada. Ele busca entender as histórias e os ensinamentos de cada indivíduo que cruza seu caminho, vendo em cada encontro uma oportunidade de crescimento e aprendizado. Essas interações moldam sua visão de mundo e expandem sua compreensão.")
        label_resultado.pack()
        imprimir_resultado()
    else:
        label_erro = tk.Label(root, text="Erro, digite novamente!")
        label_erro.pack()
        checkpoint5_missao1(nome)
def checkpoint6_missao1(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"Checkpoint 6:\n{nome} descobre que o tesouro pode estar escondido em uma cidade misteriosa e isolada. Ele tem três possibilidades para abordar essa descoberta:")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Entrar furtivamente na cidade, evitando ser detectado pelas autoridades locais.\n"
                                                " [ 2 ] - Fazer amizade com os habitantes locais, ganhando sua confiança para obter informações valiosas sobre o tesouro.\n"
                                                " [ 3 ] - Buscar ajuda de um guia experiente que conhece os segredos e armadilhas da cidade.\nSua opção: ")

    if label_caminho_novo == 1:
        label_resultado = tk.Label(root, text="CAMINHO PERIGOSO! MENOS UMA VIDA")
        label_resultado.pack()
        vidas -= 1
        label_resultado = tk.Label(root, text=f"{nome} entra furtivamente na cidade, evitando as autoridades. Explorando com cautela, ele desvenda pistas e símbolos que o levam a uma sala subterrânea, onde encontra um tesouro de artefatos preciosos e um pergaminho com sabedoria ancestral. Compartilha a história com os locais, inspirando-os.")
        label_resultado.pack()
        imprimir_resultado()
    elif label_caminho_novo == 2:
        label_resultado = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA")
        label_resultado.pack()
        vidas += 1
        label_resultado = tk.Label(root, text=f"{nome} cria laços com os habitantes, ganhando confiança. Guiado por suas conexões, encontra o tesouro não em ouro, mas em arte e tradições culturais. A cidade renova-se, unida pela jornada compartilhada.")
        label_resultado.pack()
        imprimir_resultado()
    elif label_caminho_novo == 3:
        label_resultado = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA!")
        label_resultado.pack()
        vidas += 1
        label_resultado = tk.Label(root, text=f"Com a ajuda de um guia, {nome} navega pela cidade e descobre um manuscrito antigo com ensinamentos profundos sobre autoconhecimento. Compartilha essa sabedoria com o guia e ambos partem transformados.")
        label_resultado.pack()
        imprimir_resultado()
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        checkpoint6_missao1(nome)
def caminho_seguro(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CAMINHO SEGURO! MAIS UMA VIDA!")
    label_checkpoint.pack()
    vidas += 1

    mensagem = tk.Label(
        root, text=f"{nome}, você escolhe o caminho seguro, optando por seguir uma rota mais conhecida e protegida. Sua jornada é mais tranquila, mas ainda há desafios pela frente.")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Aceitar os ensinamentos do Alquimista e aplicá-los à sua jornada.\n"
                                                " [ 2 ] - Ignorar os conselhos do Alquimista e continuar seguindo a rota segura.\nSua opção: ")

    if label_caminho_novo == 1:
        print("Você decide aceitar os ensinamentos do Alquimista e mergulhar em uma jornada de autoconhecimento. À medida que aplica os ensinamentos à sua busca, você descobre novas perspectivas e supera obstáculos internos.")
        checkpoint_final_alquimista(nome)
    elif label_caminho_novo == 2:
        print("Você opta por ignorar os conselhos do Alquimista e continuar seguindo a rota segura. Embora sua jornada seja mais tranquila, você sente que está perdendo a oportunidade de crescimento pessoal.")
        checkpoint_final_continuar(nome)
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        caminho_seguro(nome)

def checkpoint_final_alquimista(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CHECKPOINT FINAL - FINAL COM O ALQUIMISTA")
    label_checkpoint.pack()

    mensagem = tk.Label(
        root, text=f"Parabéns, {nome}! Você completa a jornada com uma mente e coração transformados pelos ensinamentos do Alquimista. Você encontra o tesouro e descobre que a verdadeira recompensa está na jornada interior que você trilhou.")
    mensagem.pack()

    vidas += 1
    imprimir_resultado()

def checkpoint_final_continuar(nome):
    label_checkpoint = tk.Label(root, text="CHECKPOINT FINAL - FINAL AO CONTINUAR")
    label_checkpoint.pack()

    mensagem = tk.Label(
        root, text=f"Infelizmente, {nome}, ao continuar seguindo a rota segura sem aplicar os ensinamentos do Alquimista, você chega ao tesouro, mas percebe que algo está faltando. O tesouro em si não traz a satisfação que você esperava.")
    mensagem.pack()

def unir_se_ao_grupo(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="UNIR-SE AO GRUPO")
    label_checkpoint.pack()

    mensagem = tk.Label(
        root, text="Você escolhe se unir a um grupo de viajantes em busca do tesouro. Você se sente mais seguro em grupo, mas também sabe que pode haver distrações.")
    mensagem.pack()

    label_caminho_novo = simpledialog.askinteger("Escolha sua opção", "Opções:\n [ 1 ] - Se juntar ao grupo, confiando na segurança em números...\n"
                                                " [ 2 ] - Optar por seguir sozinho, mantendo o foco na jornada...\nSua opção: ")

    if label_caminho_novo == 1:
        vidas += 1  # Aumentar uma vida como recompensa por se juntar ao grupo
        print("Você decide se unir ao grupo de viajantes. Juntos, vocês enfrentam os desafios e perigos da jornada, compartilhando conhecimento e experiências.")

        label_caminho_novo_grupo = simpledialog.askinteger("Escolha sua opção", "O grupo decide explorar uma caverna misteriosa que parece conter pistas sobre o tesouro. Você deseja entrar na caverna com o grupo?\n"
                                                          " [ 1 ] - Sim, entrar na caverna.\n [ 2 ] - Não, esperar do lado de fora.\nSua opção: ")

        if label_caminho_novo_grupo == 1:
            # Lógica para a escolha de entrar na caverna com o grupo
            print("Você entra na caverna junto com o grupo. Dentro dela, vocês encontram inscrições antigas que indicam o próximo passo da jornada.")
            # Restante da lógica...
            imprimir_resultado()
        elif label_caminho_novo_grupo == 2:
            # Lógica para a escolha de esperar do lado de fora
            print("Você decide esperar do lado de fora da caverna enquanto o grupo explora. Você percebe movimentação estranha nas sombras...")
            # Restante da lógica...
            imprimir_resultado()
        else:
            label_erro = tk.Label(root, text="Erro , digite novamente!")
            label_erro.pack()
            unir_se_ao_grupo(nome)
    elif label_caminho_novo == 2:
        vidas -= 1  # Diminuir uma vida como consequência de seguir sozinho
        print("Você opta por seguir sozinho em sua busca pelo tesouro. Embora seja mais arriscado, você mantém o foco em sua jornada e avança com determinação.")
        # Criar subperguntas ou opções adicionais aqui, por exemplo:
        label_caminho_novo_sozinho = simpledialog.askinteger("Escolha sua opção", "Enquanto segue sozinho, você se depara com um cruzamento que oferece duas direções.\n"
                                                             " [ 1 ] - Escolher a trilha da esquerda.\n [ 2 ] - Escolher a trilha da direita.\nSua opção: ")

        if label_caminho_novo_sozinho == 1:
            checkpoint_final_solitario(nome)
            print("Você escolhe a trilha da esquerda. Ela leva você a uma antiga ruína, onde você encontra uma inscrição enigmática que parece ser uma pista.")
            imprimir_resultado()
        elif label_caminho_novo_sozinho == 2:
            checkpoint_final_colaborativo()
            print("Você escolhe a trilha da direita. Ela leva você a um desfiladeiro perigoso, onde você precisa usar suas habilidades para atravessá-lo.")
            imprimir_resultado()
        else:
            label_erro = tk.Label(root, text="Erro , digite novamente!")
            label_erro.pack()
            unir_se_ao_grupo(nome)
    else:
        label_erro = tk.Label(root, text="Erro , digite novamente!")
        label_erro.pack()
        unir_se_ao_grupo(nome)

def checkpoint_final_solitario(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CHECKPOINT FINAL - FINAL SOLITÁRIO", fg="red")
    label_checkpoint.pack()

    mensagem = tk.Label(
        root, text=f"Infelizmente, {nome}, você percebe tarde demais que alguns membros do grupo têm intenções egoístas e traiçoeiras. Eles o traem e pegam o tesouro para si. Embora você tenha enfrentado muitos desafios, a ganância prevalece. A jornada termina de forma amarga.")
    mensagem.pack()

    vidas -= 1
    imprimir_resultado()

def checkpoint_final_colaborativo(nome):
    global vidas
    label_checkpoint = tk.Label(root, text="CHECKPOINT FINAL - FINAL COLABORATIVO", fg="blue")
    label_checkpoint.pack()

    mensagem = tk.Label(
        root, text=f"Parabéns, {nome}! Você completou a jornada em um espírito de cooperação e colaboração com o grupo. Juntos, vocês encontram o tesouro e compartilham a recompensa. Sua jornada é marcada por amizades duradouras e realizações significativas.", fg="blue")
    mensagem.pack()

    vidas += 1
    imprimir_resultado()

def imprimir_resultado():
    global vidas
    if vidas > 5:
        texto_vitoria = tk.Label(
            root, text=f"\033[1;32mVITÓRIA! Parabéns por completar a jornada com sucesso!Com um total de {vidas} vidas\033[m", fg='green')
        texto_vitoria.pack()
    else:
        texto_derrota = tk.Label(
            root, text=f"\033[1;31mDERROTA! Infelizmente, não foi possível alcançar o tesouro desta vez.Pois voce ficou com um total de {vidas} vidas e o maximo era 5!\033[m", fg='red')
        texto_derrota.pack()

    texto_deJogar = messagebox.askquestion(
        "Jogar Novamente", "Voce deseja jogar novamente?[ yes/no ]")

    if texto_deJogar == 'yes':  # tem que ser yes e nao SIM ou sim
        root.destroy()
        criar_interface_grafica()
    else:
        root.destroy()


if __name__ == "__main__":
    criar_interface_grafica()
    root.mainloop()
