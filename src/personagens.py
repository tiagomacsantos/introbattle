import pygame

class Personagem(pygame.sprite.Sprite):
    def __init__(self, vida, vida_inicial, ataque, defesa, velocidade, image, posicao, defesa_temporaria, defendendo):
        super().__init__()
        self.vida = vida
        self.vida_inicial = vida_inicial
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.image = image
        self.posicao = posicao
        self.defesa_temporaria = defesa_temporaria
        self.defendendo = defendendo

    def set_posicao(self, posicao):
        self.posicao = posicao

    def atualizar_vida(self, dano_recebido):
        self.vida -= dano_recebido
        if self.vida < 0:
            self.vida = 0

    def atacar(self, defesa_inimigo):
        dano = self.ataque * (50/(50 + defesa_inimigo))
        return dano
    
    def defender(self):
        self.defesa_temporaria = 2
    
    def esta_vivo(self):
        return self.vida > 0
        
    def get_vida(self):
        return self.vida
    
    def get_ataque(self):
        return self.ataque
    
    def get_defesa(self):
        return self.defesa * self.defesa_temporaria
    
    def get_velocidade(self):
        return self.velocidade
    
    def get_image(self):
        return self.image
    
    def get_max_vida(self):
        return self.vida_inicial
    
    def desenha_personagem(self, janela):
        self.image = pygame.transform.scale(self.image, (100, 100))
        janela.blit(self.image, self.posicao)
        
class Paladin(Personagem):
    def __init__(self):
        super().__init__(vida=150, vida_inicial=150, ataque=30, defesa=40, velocidade=20, image=pygame.image.load("./imgs/personagens/paladin.png"), posicao=(0, 0), defesa_temporaria=1, defendendo=False)
    
    def get_nome(self):
        return "PALADIN"
        

class Rogue(Personagem):
    def __init__(self):
        super().__init__(vida=100, vida_inicial=100, ataque=45, defesa=20, velocidade=40, image=pygame.image.load("./imgs/personagens/rogue.png"), posicao=(0, 0), defesa_temporaria=1, defendendo=False)
        
    def get_nome(self):
        return "ROGUE"

class Wizard(Personagem):
    def __init__(self):
        super().__init__(vida=80, vida_inicial=80, ataque=50, defesa=15, velocidade=25, image=pygame.image.load("./imgs/personagens/wizard.png"), posicao=(0, 0), defesa_temporaria=1, defendendo=False)
        self.image = pygame.transform.flip(self.image, True, False) #Invertendo a imagem do wizard

    def get_nome(self):
        return "WIZARD"    

class Hunter(Personagem):
    def __init__(self):
        super().__init__(vida=110, vida_inicial=110, ataque=35, defesa=25, velocidade=35, image=pygame.image.load("./imgs/personagens/hunter.png"), posicao=(0, 0), defesa_temporaria=1, defendendo=False)
    
    def get_nome(self):
        return "HUNTER"

class Priest(Personagem):
    def __init__(self):
        super().__init__(vida=90, vida_inicial=90, ataque=20, defesa=30, velocidade=30, image=pygame.image.load("./imgs/personagens/priest.png"), posicao=(0, 0), defesa_temporaria=1, defendendo=False)

    def get_nome(self):
        return "PRIEST"
    
class Inimigo(Personagem):
    def __init__(self, vida, vida_inicial, ataque, defesa, velocidade, image):
        super().__init__(vida, vida_inicial, ataque, defesa, velocidade, image, posicao=(0, 0), defesa_temporaria=1, defendendo=False)

class Caveira(Inimigo):
    def __init__(self):
        super().__init__(vida=100, vida_inicial=100, ataque=35, defesa=10, velocidade=32, image=pygame.image.load("./imgs/personagens/caveira.png"))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))
    
    def get_nome(self):
        return "CAVEIRA"

class Necromancer(Inimigo): 
    def __init__(self):
        super().__init__(vida=100, vida_inicial=100, ataque=40, defesa=10, velocidade=15, image=pygame.image.load("./imgs/personagens/necromancer.png"))
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 100))
    
    def get_nome(self):
        return "NECROMANCER"