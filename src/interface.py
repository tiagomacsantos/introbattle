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
    fonte = pygame.font.Font('freesansbold.ttf', 50) #Declaracao da fonte
    texto = fonte.render("IntroBattle", True, (255, 255, 255)) #Renderiza texto
    rect = pygame.Rect((janela.get_width() / 2 - 200, 60), (400, 90)) #Criacao do retangulo
    pygame.draw.rect(janela, (0, 0, 0), rect) #Retangulo do titulo
    pygame.draw.rect(janela, (255, 255, 255), rect, 7) #Borda
    texto_rect = texto.get_rect(center=rect.center) #Acha o centro do retangulo
    janela.blit(texto, texto_rect) #Desenha o texto na tela

        