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
game_over = False
fps = 60

#imagem de fundo do jogo
background = pygame.image.load("./imgs/background/teste3ps.png")
background = pygame.transform.scale(background, (1024, 768))

#Escolhas do jogador
escolhas = []

while run:
    #desenha a imagem de fundo do jogo
    win.blit(background, (0, 0))
    clock.tick(fps)

    eventos = pygame.event.get()

    for event in eventos:
        #avalia se a janela foi fechada
        if event.type == pygame.QUIT:
            run = False

    if menu_principal:
        menu_principal, escolhas = interface.desenha_menu(win, eventos)
    else:
        menu_principal, game_over = interface.desenha_jogo(win, eventos, escolhas)
    
    #atualiza o display da tela
    pygame.display.flip()

    


pygame.quit()