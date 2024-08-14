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
    
# FALTA FAZER E DESENHAR A LOGICA DA SETA E ESCREVER OS NOMES DOS BONECOS
def desenha_menu(janela):
    #Titulo do introbattle
    fonte = pygame.font.Font('freesansbold.ttf', 50) #Declaracao da fonte
    texto = fonte.render("IntroBattle", True, (255, 255, 255)) #Renderiza texto
    rect_introbattle = pygame.Rect((janela.get_width() / 2 - 200, 60), (400, 90)) #Criacao do retangulo
    texto_rect = texto.get_rect(center=rect_introbattle.center) #Acha o centro do retangulo
    
    #Personagens
    personagem_tamanho = (150, 150)
    
    paladin = pygame.image.load("./imgs/personagens/paladin.png")
    rogue = pygame.image.load("./imgs/personagens/rogue.png")
    priest = pygame.image.load("./imgs/personagens/priest.png")         #Inicia as variaveis que vao guardar as imagens
    hunter = pygame.image.load("./imgs/personagens/hunter.png")
    wizard = pygame.image.load("./imgs/personagens/wizard.png")
    wizard = pygame.transform.flip(wizard, True, False) #invertendo horizontalmente a imagem do bruxo
    
    personagens = [
        paladin,
        rogue,
        wizard,         #Salva as imagens em uma lista
        hunter,
        priest,
    ]

    for i in range(len(personagens)):
        personagens[i] = pygame.transform.scale(personagens[i], personagem_tamanho) #Redimensiona o tamanho dos sprites dos personagens
    
    personagem_posicoes = [
        (137, 235), #paladin
        (432, 235), #rogue
        (720, 235), #wizard                  
        (290, 485), #hunter
        (576, 485), #priest
    ]


    #Quadrado do personagem
    botao_tamanho = (550, 500)
    botao_personagem = pygame.image.load("./imgs/UI/introcomp_menu.png")
    botao_personagem = pygame.transform.scale(botao_personagem, botao_tamanho)
    botao_posicoes = [
        (-200, -50), #paladin
        (87, -50), #rogue
        (374, -50), #wizard
        (-53, 200), #hunter
        (234, 200), #priest
    ]

    
    #desenhos na tela
    pygame.draw.rect(janela, (0, 0, 0), rect_introbattle) #Retangulo do titulo
    pygame.draw.rect(janela, (255, 255, 255), rect_introbattle, 7) #Borda do retangulo do titulo
    janela.blit(texto, texto_rect) #Desenha o texto na tela
    for i in range(5):
        janela.blit(botao_personagem, botao_posicoes[i]) #Desenha os botoes
        janela.blit(personagens[i], personagem_posicoes[i]) #Desenha os personagens
    

    return True