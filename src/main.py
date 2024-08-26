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
venceu = False
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

    if game_over == True:
        escolhas.clear()
        game_over, menu_principal, run = interface.game_over_tela(eventos, win)
    if venceu == True:
        escolhas.clear()
        venceu, menu_principal, run = interface.venceu_tela(eventos, win)
    
    if menu_principal:
        menu_principal, escolhas = interface.desenha_menu(win, eventos)
    elif (run and not venceu) and (run and not game_over):
        game_over, venceu = interface.desenha_jogo(win, eventos, escolhas)
    
    #atualiza o display da tela
    pygame.display.flip()

pygame.quit()