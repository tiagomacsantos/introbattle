import pygame
from personagens import Paladin, Rogue, Wizard, Hunter, Priest, Caveira, Necromancer
import random

class Window():

    width = 0
    height = 0
    color = (0, 0, 0)

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_window_size(self):
        return (self.height, self.width)
    
    def get_color(self):
        return self.color
    
def game_over_tela():
    #DESENHOS NA TELA PARA QUANDO O PLAYER PERDER
    return False, False

def venceu_tela():
    #DESENHOS NA TELA PARA QUANDO O PLAYER GANHAR
    return True, True

def realiza_ataque(personagem_atacante, seta_inimigos_posicoes, inimigos, janela, seta, acao_flag, eventos):
    if not hasattr(realiza_ataque, "indice_seta"):
            realiza_ataque.indice_seta = 0 # Começa com o primeiro inimigo como alvo
    alvo_selecionado = False
    acao_flag = True
    
    for event in eventos:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                realiza_ataque.indice_seta = (realiza_ataque.indice_seta + 1) % len(inimigos)
                acao_flag = True
            elif event.key == pygame.K_LEFT:
                realiza_ataque.indice_seta = (realiza_ataque.indice_seta - 1) % len(inimigos)
                acao_flag = True
            elif event.key == pygame.K_z:
                alvo_selecionado = True
                acao_flag = False

    janela.blit(seta, seta_inimigos_posicoes[realiza_ataque.indice_seta])

    return realiza_ataque.indice_seta, alvo_selecionado, acao_flag
    
def escolhe_personagem(escolhas, seta_posicoes, indice_seta, eventos):
    #Verifica pressionamento de teclas
    for event in eventos:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                indice_seta += 1
            elif event.key == pygame.K_LEFT:
                indice_seta -= 1
            elif event.key == pygame.K_z:
                if indice_seta not in escolhas:
                    escolhas.append(indice_seta)

    # Mantem o indice da seta dentro dos limites e pula personagens ja escolhidos
    while indice_seta in escolhas or indice_seta < 0 or indice_seta >= len(seta_posicoes):
        if indice_seta < 0:
            indice_seta = len(seta_posicoes) - 1
        elif indice_seta >= len(seta_posicoes):
            indice_seta = 0
        else:
            indice_seta += 1

    return escolhas, indice_seta

def escolhe_acao(seta_posicoes_acoes, indice_seta, eventos):
    acao_escolhida = None
    
    # Verifica pressionamento de teclas
    for event in eventos:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                indice_seta += 1  # Move para a direita
            elif event.key == pygame.K_LEFT:
                indice_seta -= 1  # Move para a esquerda
            elif event.key == pygame.K_c:
                acao_escolhida = indice_seta  # Seleciona a ação atual

    # Mantém o índice da seta dentro dos limites
    if indice_seta < 0:
        indice_seta = len(seta_posicoes_acoes) - 1  # Vai para a última ação
    elif indice_seta >= len(seta_posicoes_acoes):
        indice_seta = 0  # Volta para a primeira ação

    return acao_escolhida, indice_seta

def desenha_menu(janela, eventos):
    # Título do introbattle
    fonte = pygame.font.Font('freesansbold.ttf', 50)  # Declaração da fonte
    texto = fonte.render("IntroBattle", True, (255, 255, 255))  # Renderiza texto
    rect_introbattle = pygame.Rect((janela.get_width() / 2 - 200, 60), (400, 90))  # Criação do retângulo
    texto_rect = texto.get_rect(center=rect_introbattle.center)  # Acha o centro do retângulo
    
    # Personagens
    personagem_tamanho = (150, 150)
    
    paladin = pygame.image.load("./imgs/personagens/paladin.png")
    rogue = pygame.image.load("./imgs/personagens/rogue.png")
    priest = pygame.image.load("./imgs/personagens/priest.png")  # Inicia as variáveis que vão guardar as imagens
    hunter = pygame.image.load("./imgs/personagens/hunter.png")
    wizard = pygame.image.load("./imgs/personagens/wizard.png")
    wizard = pygame.transform.flip(wizard, True, False)  # Invertendo horizontalmente a imagem do bruxo
    
    personagens = [
        paladin,
        rogue,
        wizard,  # Salva as imagens em uma lista
        hunter,
        priest,
    ]

    for i in range(len(personagens)):
        personagens[i] = pygame.transform.scale(personagens[i], personagem_tamanho)  # Redimensiona o tamanho dos sprites dos personagens
    
    personagem_posicoes = [
        (137, 235),  # paladin
        (432, 235),  # rogue
        (720, 235),  # wizard                  
        (290, 515),  # hunter
        (576, 515),  # priest
    ]

    # Nomes dos personagens
    fonte_personagens = pygame.font.Font('freesansbold.ttf', 30)
    paladin_text = fonte_personagens.render("Paladin", True, (255, 255, 255))
    rogue_text = fonte_personagens.render("Rogue", True, (255, 255, 255))
    wizard_text = fonte_personagens.render("Wizard", True, (255, 255, 255))
    hunter_text = fonte_personagens.render("Hunter", True, (255, 255, 255))
    priest_text = fonte_personagens.render("Priest", True, (255, 255, 255))

    nomes = [
        paladin_text,
        rogue_text,
        wizard_text,
        hunter_text,
        priest_text,
    ]

    nomes_posicoes = [
        (160, 400),  # Paladin
        (455, 400),  # Rogue
        (738, 400),  # Wizard
        (312, 680),  # Hunter
        (604, 680),  # Priest
    ]


    # Quadrado do personagem
    botao_tamanho = (550, 500)
    botao_personagem = pygame.image.load("./imgs/UI/introcomp_menu.png")
    botao_personagem = pygame.transform.scale(botao_personagem, botao_tamanho)
    botao_posicoes = [
        (-200, -50),  # paladin
        (87, -50),  # rogue
        (374, -50),  # wizard
        (-53, 230),  # hunter
        (234, 230),  # priest
    ]

    # Lógica para mover a seta
    seta = pygame.image.load("./imgs/UI/introcomp_seta.png")  # Criando a sprite da seta que percorrerá os personagens
    seta_tamanho = (370, 370)
    seta = pygame.transform.scale(seta, seta_tamanho)
    seta_posicoes = [
        (-62, 130),  # paladin
        (225, 130),  # rogue
        (512, 130),  # wizard
        (86, 409),  # hunter
        (373, 409),  # priest
    ]
    
    # Inicializacao de atributos da funcao
    if not hasattr(desenha_menu, "indice_seta"):
        desenha_menu.indice_seta = 0  # Inicializa o índice da seta
        desenha_menu.escolhas = []  # Inicializa a lista de escolhas

    # Escolha dos personagens                                                                                    
    desenha_menu.escolhas, desenha_menu.indice_seta = escolhe_personagem(
        desenha_menu.escolhas, seta_posicoes, desenha_menu.indice_seta, eventos
    )
    
    # Desenhos na tela
    pygame.draw.rect(janela, (0, 0, 0), rect_introbattle)  # Retângulo do título
    pygame.draw.rect(janela, (255, 255, 255), rect_introbattle, 7)  # Borda do retângulo do título
    janela.blit(texto, texto_rect)  # Desenha o texto na tela
    
    # Tempo inicial para o efeito de piscar
    tempo_piscar = 200  # Tempo em milissegundos
    tempo_atual = pygame.time.get_ticks()
    for i in range(5):
        janela.blit(botao_personagem, botao_posicoes[i]) # Desenha os botões
        

        # Se o personagem foi escolhido, aplica o efeito de piscar
        if i in desenha_menu.escolhas:
            if (tempo_atual // tempo_piscar) % 2 == 0:
                janela.blit(personagens[i], personagem_posicoes[i])  # Desenha a sprite
                janela.blit(nomes[i], nomes_posicoes[i]) # Desenha os nomes dos personagens
        else:
            janela.blit(personagens[i], personagem_posicoes[i])  # Desenha a sprite normalmente
            janela.blit(nomes[i], nomes_posicoes[i]) # Desenha os nomes dos personagens normalmente

    janela.blit(seta, seta_posicoes[desenha_menu.indice_seta]) # Desenha a seta em sua posicao atual
    
    # Verifica se três personagens foram escolhidos
    if len(desenha_menu.escolhas) >= 3:
        return False, desenha_menu.escolhas
    
    return True, desenha_menu.escolhas

def define_ordem_ataque(personagens, inimigo1, inimigo2):
    lista_ordenada = [inimigo1, inimigo2]

    for i in range(len(personagens)):
        lista_ordenada.append(personagens[i])

    lista_ordenada.sort(key=lambda entidade: entidade.get_velocidade(), reverse=True)

    return lista_ordenada

def desenha_jogo(janela, eventos, escolhas):

    # Carregamento das imagens de UI
    menu_acoes_tamanho = (700, 300)
    menu_acoes = pygame.image.load("./imgs/UI/introcomp_menu_cortado2.png")
    menu_acoes = pygame.transform.scale(menu_acoes, menu_acoes_tamanho)

    menu_info_tamanho = (360, 300)
    menu_info = pygame.image.load("./imgs/UI/introcomp_menu_cortado2.png")
    menu_info = pygame.transform.scale(menu_info, menu_info_tamanho)

    #Instanciando os objetos dos personagens e suas respectivas classes
    personagem_posicoes = [
        (300, 150),
        (200, 250),
        (300, 350),
    ]

    if not hasattr(desenha_jogo, "instanciado"):
        desenha_jogo.personagens_objetos = []

        for i in escolhas:
            match i:
                case 0:
                    desenha_jogo.personagens_objetos.append(Paladin())
                case 1:
                    desenha_jogo.personagens_objetos.append(Rogue())
                case 2:
                    desenha_jogo.personagens_objetos.append(Wizard())
                case 3:
                    desenha_jogo.personagens_objetos.append(Hunter())
                case 4:
                    desenha_jogo.personagens_objetos.append(Priest())
        
        # Marca que os personagens foram instanciados
        desenha_jogo.instanciado = True

    # Verifica se os inimigos já foram instanciados
    if not hasattr(desenha_jogo, "inimigos_instanciados"):
        desenha_jogo.inimigos_instanciados = [
            Caveira(),
            Necromancer()
        ]
        desenha_jogo.inimigo1 = desenha_jogo.inimigos_instanciados[1]
        desenha_jogo.inimigo2 = desenha_jogo.inimigos_instanciados[0]

    inimigo1 = desenha_jogo.inimigo1
    inimigo2 = desenha_jogo.inimigo2

    inimigos = [
        inimigo1,
        inimigo2,
    ]

    inimigos_posicoes = [
        (750, 200),
        (630, 320),
    ]

    #Fonte do menu UI
    fonte = pygame.font.Font('freesansbold.ttf', 30)
    fonte_inimigos = pygame.font.Font('freesansbold.ttf', 20)

    textos_acoes = [
        fonte.render("ATACAR", True, (255, 255, 255)),
        fonte.render("DEFENDER", True, (255, 255, 255)),
    ]
    #Bordas
    textos_acoes2 = [
        fonte.render("ATACAR", True, (0, 0, 0)),
        fonte.render("DEFENDER", True, (0, 0, 0)),
    ]

    textos_posicoes_acoes = [
        (150, 590),
        (350, 590),
    ]
    #Bordas
    textos_posicoes_acoes2 = [
        (151, 591),
        (351, 591),
    ]

    #Vida dos inimigos
    texto_inimigos = [
        fonte_inimigos.render((f"{int(inimigo1.get_vida())} / {inimigo1.get_max_vida()}"), True, (255, 255, 255)),
        fonte_inimigos.render((f"{int(inimigo2.get_vida())} / {inimigo2.get_max_vida()}"), True, (255, 255, 255)),
    ]
    texto_inimigos_posicoes = [
        (758, 305),
        (638, 425),
    ]

    textos_informacoes_posicao = [
        (700, 510),
        (700, 590),
        (700, 670),
    ]
    #Borda
    textos_informacoes_posicao2 = [
        (701, 511),
        (701, 591),
        (701, 671),
    ]

    #Setinha de escolha
    seta = pygame.image.load("./imgs/UI/introcomp_seta_cortada.png")
    seta = pygame.transform.scale(seta, (30, 30))
    seta = pygame.transform.rotate(seta, 90)

    seta_posicoes_acoes = [
        (118, 590),
        (315, 590),
    ]

    if not hasattr(desenha_jogo, "indice_seta_acoes"):
        desenha_jogo.indice_seta_acoes = 0  # Inicializa o indice da seta de ações
        desenha_jogo.acao_escolhida = None  # Inicializa a ação escolhida
    
    if not hasattr(desenha_jogo, "acao_flag"):
        desenha_jogo.acao_flag = False

    # Escolha da ação
    if desenha_jogo.acao_flag == False:
        desenha_jogo.acao_escolhida, desenha_jogo.indice_seta_acoes = escolhe_acao(seta_posicoes_acoes, desenha_jogo.indice_seta_acoes, eventos)
        

    lista_ordem_ataque = define_ordem_ataque(desenha_jogo.personagens_objetos, inimigo1, inimigo2)

    # Verifica se um turno já foi definido
    if not hasattr(desenha_jogo, "indice_turno"):
        desenha_jogo.indice_turno = 0  # Inicializa o índice do turno

    # Determina o personagem da vez
    personagem_turno = lista_ordem_ataque[desenha_jogo.indice_turno]

    # Exibe o nome do personagem que está jogando
    texto_turno = fonte.render(f"TURNO DO {personagem_turno.get_nome().upper()}!", True, (255, 255, 255))
    texto_turno2 = fonte.render(f"TURNO DO {personagem_turno.get_nome().upper()}!", True, (0, 0, 0))
    texto_turno_posicao = (150, 520)
    texto_turno_posicao2 = (151, 521) #Borda

    #Posicoes das setas para quando for atacar os inimigos
    seta_inimigos_posicoes = [
        (710, 250),
        (590, 370),
    ]

    # Verifica se uma ação foi escolhida e avança o turno
    if desenha_jogo.acao_escolhida is not None:
        if desenha_jogo.acao_escolhida == 0:
            seta_indice_inimigos, alvo_foi_escolhido, desenha_jogo.acao_flag = realiza_ataque(personagem_turno, seta_inimigos_posicoes, inimigos, janela, seta, desenha_jogo.acao_flag, eventos)
            if alvo_foi_escolhido == True:
                inimigo = inimigos[seta_indice_inimigos]
                dano = personagem_turno.atacar(inimigo.get_defesa())
                inimigo.atualizar_vida(dano)
        elif desenha_jogo.acao_escolhida == 1:
            pass     

    #Textos informacoes
    textos_informacoes = []
    textos_informacoes2 = []
    for personagem in desenha_jogo.personagens_objetos:
        textos_informacoes.append(fonte.render((f"{personagem.get_nome()}  {int(personagem.get_vida())} / {personagem.get_max_vida()}"), True, (255, 255, 255)))
        textos_informacoes2.append(fonte.render((f"{personagem.get_nome()}  {int(personagem.get_vida())} / {personagem.get_max_vida()}"), True, (0, 0, 0))) #Borda

    # Desenhos na tela
    janela.blit(menu_acoes, (0, 450))
    janela.blit(menu_info, (665, 450))
    if desenha_jogo.acao_flag == False:
        janela.blit(seta, seta_posicoes_acoes[desenha_jogo.indice_seta_acoes])

    for i in range(3):
        if desenha_jogo.personagens_objetos[i].esta_vivo():  # Verifica se o personagem está vivo
            desenha_jogo.personagens_objetos[i].set_posicao(personagem_posicoes[i])
            desenha_jogo.personagens_objetos[i].desenha_personagem(janela)
        # Desenha informações apenas para personagens vivos
        janela.blit(textos_informacoes2[i], textos_informacoes_posicao2[i])  # Borda
        janela.blit(textos_informacoes[i], textos_informacoes_posicao[i])


    for i in range(2):
        janela.blit(textos_acoes2[i], textos_posicoes_acoes2[i]) #BORDA
        janela.blit(textos_acoes[i], textos_posicoes_acoes[i])
        janela.blit(texto_inimigos[i], texto_inimigos_posicoes[i])

    janela.blit(texto_turno2, texto_turno_posicao2)
    janela.blit(texto_turno, texto_turno_posicao)

    janela.blit(inimigo1.get_image(), inimigos_posicoes[0])
    janela.blit(inimigo2.get_image(), inimigos_posicoes[1])  

    #PROVAVELMENTE TA AQUI O ERRO
    if desenha_jogo.acao_escolhida == True:
        desenha_jogo.indice_turno = (desenha_jogo.indice_turno + 1) % len(lista_ordem_ataque)

    # Inimigos atacando    
    while lista_ordem_ataque[desenha_jogo.indice_turno].get_nome() in ["CAVEIRA", "NECROMANCER"] or not lista_ordem_ataque[desenha_jogo.indice_turno].esta_vivo():
        if lista_ordem_ataque[desenha_jogo.indice_turno].get_nome() in ["CAVEIRA", "NECROMANCER"]:
            # Encontra o personagem jogável com a menor vida (o mais fraco)
            menor_vida = float('inf')
            alvo = None
            for personagem in desenha_jogo.personagens_objetos:
                if personagem.get_vida() > 0 and personagem.get_vida() < menor_vida:
                    menor_vida = personagem.get_vida()
                    alvo = personagem
            # Realiza o ataque no personagem encontrado
            if alvo is not None:
                dano = lista_ordem_ataque[desenha_jogo.indice_turno].atacar(alvo.get_defesa())
                print(f"Dano causado: {dano}")
                alvo.atualizar_vida(dano)  # Atualiza a vida do personagem que recebeu dano
                print(f"Vida do alvo após dano: {alvo.get_vida()}")

            # Passa para o próximo turno
            desenha_jogo.indice_turno = (desenha_jogo.indice_turno + 1) % len(lista_ordem_ataque)
        else:
            desenha_jogo.indice_turno = (desenha_jogo.indice_turno + 1) % len(lista_ordem_ataque)

        jogaveis_vivos = any(personagem.esta_vivo() for personagem in desenha_jogo.personagens_objetos)

        if not jogaveis_vivos:
            return True, False

    return False, False