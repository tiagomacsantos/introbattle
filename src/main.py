import interface
import pygame 

pygame.mixer.init()

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

#musica de fundo
pygame.mixer.music.load("./sounds/musica_fundo.ogg")

pygame.mixer.music.play(-1) 

pygame.mixer.music.set_volume(0.3)

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
        pygame.mixer.music.stop()
        escolhas.clear()
        game_over, menu_principal, run = interface.game_over_tela(eventos, win)
    if venceu == True:
        pygame.mixer.music.stop()
        escolhas.clear()
        venceu, menu_principal, run = interface.venceu_tela(eventos, win)
    
    if menu_principal:
        menu_principal, escolhas = interface.desenha_menu(win, eventos)
    elif (run and not venceu) and (run and not game_over):
        game_over, venceu = interface.desenha_jogo(win, eventos, escolhas)
    
    #atualiza o display da tela
    pygame.display.flip()

pygame.quit()