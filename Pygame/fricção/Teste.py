import pygame
import os

BASE = os.path.dirname(__file__)

pygame.init()
Tela = pygame.display.set_mode((800, 600))
rodando = True

class Bola:
    def __init__(self, sprite, x, y, velocidade):
        caminho = os.path.join(os.path.dirname(__file__), sprite)
        self.sprite = pygame.image.load(caminho)
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.sprite)
        self.x = x
        self.y = y
        self.velocidade = velocidade

    def desenhar(self, tela):
        tela.blit(self.sprite,(self.x, self.y))

    def movimento(self):
        self.x += self.velocidade[0]
        self.y += self.velocidade[1]

    def atualizar(self,tela):
        self.desenhar(tela)
        self.movimento()
        
         
Bola1 = Bola(r"Sprites\Bola.png", 67, 67, [0,0])
Bola2 = Bola(r"Sprites\Bola.png", 200, 267, [0,0])

while rodando:
    Tela.fill("white")

    Bola1.atualizar(Tela)
    Bola2.atualizar(Tela)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
    pygame.display.flip()
pygame.quit()