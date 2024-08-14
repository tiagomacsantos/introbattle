import pygame

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

    
# FALTA FAZER E DESENHAR A LOGICA DA SETA E ESCREVER OS NOMES DOS BONECOS
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