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
    
# FALTA DESENHAR OS QUADRADOS DOS PERSONAGENS E OS PERSONAGENS
def desenha_menu(janela):
    #Titulo do introbattle
    fonte = pygame.font.Font('freesansbold.ttf', 50) #Declaracao da fonte
    texto = fonte.render("IntroBattle", True, (255, 255, 255)) #Renderiza texto
    rect_introbattle = pygame.Rect((janela.get_width() / 2 - 200, 60), (400, 90)) #Criacao do retangulo
    pygame.draw.rect(janela, (0, 0, 0), rect_introbattle) #Retangulo do titulo
    pygame.draw.rect(janela, (255, 255, 255), rect_introbattle, 7) #Borda
    texto_rect = texto.get_rect(center=rect_introbattle.center) #Acha o centro do retangulo
    
    #Personagens
    personagem_tamanho = (400, 400)
    personagens = ["paladin", "rougue", "wizard", "hunter", "priest"]


    #Quadrado personagem
    botao_tamanho = (500, 500)
    botao_personagem = pygame.image.load("./imgs/UI/introcomp_menu.png")
    botao_personagem = pygame.transform.scale(botao_personagem, botao_tamanho)
    botao_posicoes = [
        (150, 150),
        (437, 150),
        (724, 150),
        (287, 400),
        (574, 400),
    ]

    for i in range(5):
        janela.blit(botao_personagem, botao_posicoes[i])
    
    #desenhos na tela
    janela.blit(texto, texto_rect) #Desenha o texto na tela

    return True


        