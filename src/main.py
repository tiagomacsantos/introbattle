import interface
import pygame 

pygame.init()

clock = pygame.time.Clock()

#instancia um obj do tipo Window
w = interface.Window(1024, 768)

#inicia a janela
win = pygame.display.set_mode(w.get_window_size())
pygame.display.set_caption("IntroBattle!")


#variaveis do loop principal
run = True
menu_principal = True
fps = 60

#imagem de fundo do jogo
background = pygame.image.load("./imgs/background/teste3ps.png")
background = pygame.transform.scale(background, (1024, 768))

while run:
    #desenha a imagem de fundo do jogo
    win.blit(background, (0, 0))
    clock.tick(fps)

    for event in pygame.event.get():
        #avalia se a janela foi fechada
        if event.type == pygame.QUIT:
            run = False

    if menu_principal:
        menu_principal = interface.desenha_menu(win)
    #else:
        #menu_principal = interface.desenha_jogo(win)
    
    #atualiza o display da tela
    pygame.display.flip()

    


pygame.quit()