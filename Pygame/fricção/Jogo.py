import pygame
import os

BASE = os.path.dirname(__file__)

pygame.init()
Tela = pygame.display.set_mode((2560,1080))
rodando = True
clock = pygame.time.Clock()


class Bola:
    def __init__(self, sprite, x, y, massa,velocidade):
        caminho = os.path.join(os.path.dirname(__file__), sprite)
        self.sprite = pygame.image.load(caminho).convert_alpha()
        self.mask = pygame.mask.from_surface(self.sprite)
        self.x = x
        self.y = y
        self.massa = massa
        self.velocidade = velocidade
        self.colidindo = False

    def desenhar(self, tela):
        tela.blit(self.sprite,(self.x, self.y))

    def movimento(self):
        self.x += self.velocidade[0]
        self.y += self.velocidade[1]

    def colisao(self, lista_de_objetos):
         bateu = False

         for objeto in lista_de_objetos:
            if objeto != self:
                offset = (int(objeto.x - self.x), int(objeto.y - self.y))
                if self.mask.overlap(objeto.mask, offset):
                    if self.colidindo or objeto.colidindo:
                        continue
                    print(f"Colisão detectada entre {self} e {objeto}")

                    vetordacolisao = pygame.Vector2(
                        (objeto.x - self.x),
                        (objeto.y - self.y)
                    )

                    if vetordacolisao.length() != 0:
                        normal = vetordacolisao.normalize()


                    velocidade1 = pygame.Vector2(self.velocidade[0], self.velocidade[1])
                    velocidade2 = pygame.Vector2(objeto.velocidade[0], objeto.velocidade[1])

                    v1_normal = velocidade1.dot(normal)
                    v2_normal = velocidade2.dot(normal)

                    bateu = True

                    self.colidindo = True
                    objeto.colidindo = True

                    nova_velocidade1 = (
                        (((self.massa - objeto.massa) * v1_normal) + ((2*objeto.massa)*v2_normal))
                        /
                        (self.massa + objeto.massa)
                        )

                    nova_velocidade2 = (
                        (((objeto.massa - self.massa ) * v2_normal) + ((2*self.massa)*v1_normal))
                        /
                        (self.massa + objeto.massa)
                        )

                    velocidade1_tangente = velocidade1 - normal * v1_normal
                    velocidade2_tangente = velocidade2 - normal * v2_normal

                    velocidade1_final = velocidade1_tangente + normal * nova_velocidade1
                    velocidade2_final = velocidade2_tangente + normal * nova_velocidade2

                    self.velocidade[0] = velocidade1_final.x 
                    self.velocidade[1] = velocidade1_final.y 

                    objeto.velocidade[0] = velocidade2_final.x 
                    objeto.velocidade[1] = velocidade2_final.y 

                    self.x -= normal.x
                    self.y -= normal.y

                    objeto.x += normal.x
                    objeto.y += normal.y

         if not bateu:
            self.colidindo = False

    def paredes(self, largura, altura):
        raio_x = self.sprite.get_width()
        raio_y = self.sprite.get_height()

        # esquerda
        if self.x <= 0:
            self.x = 0
            self.velocidade[0] *= -1

        # direita
        if self.x + raio_x >= largura:
            self.x = largura - raio_x
            self.velocidade[0] *= -1

        # cima
        if self.y <= 0:
            self.y = 0
            self.velocidade[1] *= -1

        # baixo
        if self.y + raio_y >= altura:
            self.y = altura - raio_y
            self.velocidade[1] *= -1


                    
    def atualizar(self,tela):
        self.movimento()
        self.desenhar(tela)
        print(f"velocidade da {self} {self.velocidade}")
        print(f"colisão da {self} {self.colidindo}")
        
         
Bola1 = Bola(r"Sprites/BolaVerde.png", 1500, 400, 20,[0,0])

Bola2 = Bola(r"Sprites/BolaVerde.png", 1628, 336, 20, [0,0])
Bola3 = Bola(r"Sprites/BolaVerde.png", 1628, 464, 20, [0,0])

Bola4 = Bola(r"Sprites/BolaVerde.png", 1756, 272, 20,[0,0])
Bola5 = Bola(r"Sprites/BolaVerde.png", 1756, 400, 20, [0,0])
Bola6 = Bola(r"Sprites/BolaVerde.png", 1756, 528, 20, [0,0])

Bola7 = Bola(r"Sprites/BolaVerde.png", 1884, 208, 20,[0,0])
Bola8 = Bola(r"Sprites/BolaVerde.png", 1884, 336, 20, [0,0])
Bola9 = Bola(r"Sprites/BolaVerde.png", 1884, 464, 20, [0,0])
Bola10 = Bola(r"Sprites/BolaVerde.png", 1884, 592, 20,[0,0])

Bola11 = Bola(r"Sprites/BolaVerde.png", 2012, 144, 20, [0,0])
Bola12 = Bola(r"Sprites/BolaVerde.png", 2012, 272, 20, [0,0])
Bola13 = Bola(r"Sprites/BolaVerde.png", 2012, 400, 20,[0,0])
Bola14 = Bola(r"Sprites/BolaVerde.png", 2012, 528, 20, [0,0])
Bola15 = Bola(r"Sprites/BolaVerde.png", 2012, 656, 20, [0,0])

BolaBranca = Bola(r"Sprites/Bola.png", 500, 400, 20,[30,1])

todas_bolas = [
    Bola1, Bola2, Bola3, Bola4, Bola5,
    Bola6, Bola7, Bola8, Bola9, Bola10,
    Bola11, Bola12, Bola13, Bola14, Bola15,
    BolaBranca
]


while rodando:
    Tela.fill("white")

    for bola in todas_bolas:
        bola.colisao(todas_bolas)

    for bola in todas_bolas:
        bola.paredes(2560,1080)
        bola.atualizar(Tela)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

    pygame.display.flip()

    clock.tick(60)
    os.system("clear")
pygame.quit()