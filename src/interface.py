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
            elif event.key == pygame.K_z:
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

    personagens_objetos = []

    for i in escolhas:
        match i:
            case 0:
                personagens_objetos.append(Paladin())
            case 1:
                personagens_objetos.append(Rogue())
            case 2:
                personagens_objetos.append(Wizard())
            case 3:
                personagens_objetos.append(Hunter())
            case 4:
                personagens_objetos.append(Priest())

    # Verifica se os inimigos já foram instanciados
    if not hasattr(desenha_jogo, "inimigos_instanciados"):
        desenha_jogo.inimigos_instanciados = [
            Caveira(),
            Necromancer()
        ]
        desenha_jogo.inimigo1 = random.choice(desenha_jogo.inimigos_instanciados)
        desenha_jogo.inimigo2 = random.choice(desenha_jogo.inimigos_instanciados)

    inimigo1 = desenha_jogo.inimigo1
    inimigo2 = desenha_jogo.inimigo2

    #Fonte do menu UI
    fonte = pygame.font.Font('freesansbold.ttf', 30)

    textos_acoes = [
        fonte.render("ATACAR", True, (255, 255, 255)),
        fonte.render("DEFENDER", True, (255, 255, 255)),
    ]
    #Bordas
    textos_acoes2 = [
        fonte.render("ATACAR", True, (0, 0, 0)),
        fonte.render("DEFENDER", True, (0, 0, 0)),
    ]

    #MEXER AQUI PELO AMOR DE DEUS
    textos_posicoes_acoes = [
        (150, 590),
        (350, 590),
    ]
    #Bordas
    textos_posicoes_acoes2 = [
        (151, 591),
        (351, 591),
    ]

    #Textos informacoes
    textos_informacoes = []
    textos_informacoes2 = []
    for personagem in personagens_objetos:
        textos_informacoes.append(fonte.render((f"{personagem.get_nome()}  {personagem.get_vida()} / {personagem.get_max_vida()}"), True, (255, 255, 255)))
        textos_informacoes2.append(fonte.render((f"{personagem.get_nome()}  {personagem.get_vida()} / {personagem.get_max_vida()}"), True, (0, 0, 0))) #Borda

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

    # Escolha da ação
    desenha_jogo.acao_escolhida, desenha_jogo.indice_seta_acoes = escolhe_acao(
        seta_posicoes_acoes, desenha_jogo.indice_seta_acoes, eventos
    )

    # Verifica se uma ação foi escolhida e realiza algo (ALTERAR AQUI DENTRO PARA QUANDO O USUARIO ESCOLHER ALGO)
    if desenha_jogo.acao_escolhida is not None:
        print(f"Ação escolhida: {desenha_jogo.acao_escolhida}")
        pass

    # Desenhos na tela
    janela.blit(menu_acoes, (0, 450))
    janela.blit(menu_info, (665, 450))
    janela.blit(seta, seta_posicoes_acoes[desenha_jogo.indice_seta_acoes])

    for i in range(3):
        personagens_objetos[i].set_posicao(personagem_posicoes[i])
        personagens_objetos[i].desenha_personagem(janela)
        janela.blit(textos_informacoes2[i], textos_informacoes_posicao2[i]) #BORDA
        janela.blit(textos_informacoes[i], textos_informacoes_posicao[i])


    for i in range(2):
        janela.blit(textos_acoes2[i], textos_posicoes_acoes2[i]) #BORDA
        janela.blit(textos_acoes[i], textos_posicoes_acoes[i])

    return False