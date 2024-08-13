class Personagem():
    def __init__(self, vida, ataque, defesa, velocidade):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
    

#herda Personagem
class Player(Personagem):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade): 
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade


#herda Personagem
class Inimigo(Personagem):

    
