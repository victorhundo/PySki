# coding: utf-8
# Classe Obstaculo
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame, random, math

TIPO_OBSTACULOS = ["arvore", "rocha"]
RELOGIO = pygame.time.Clock()
class Obstaculo():

    def __init__(self, tela):
        self.tela = tela
        self.imagem = self.tipo_aleatorio()
        self.pos = (0,500)
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)
        self.posicao_y = random.randint(500, 850) #tamanho final da tela
        self.posicao_x = random.randint(90,670)
        self.velocidade = 0.3
        self.aceleracao = 0
        self.tempo = 0

    def mover(self, tempo):
        #condição para que haja repetição da imagem
        if self.posicao_y < -50 : 
            self.posicao_y = random.randint(600, 850)
            self.posicao_x = random.randint(90,670)
            self.imagem = self.tipo_aleatorio()
            self.mask = pygame.mask.from_surface(self.imagem)
            self.rect = self.imagem.get_rect()
        
        self.velocidade += 0.009
        self.posicao_y -= self.velocidade  #subtraindo para subir a imagem
        self.rect.x = self.posicao_x
        self.rect.y = self.posicao_y
        self.pos = (self.rect.x, self.rect.y)

    def mostrar_obstaculo(self):
        return self.tela.blit(self.imagem, self.pos)

    def houve_colisao(self):
        self.velocidade = 0.3
        self.tempo = 0
        self.posicao_y += 30
    
    def tipo_aleatorio(self):
        tipo = TIPO_OBSTACULOS[random.randint(0,1)]
        if  tipo == 'arvore':
            return  pygame.image.load("img/arvore.png")
        elif tipo == 'rocha':
            return  pygame.image.load("img/rocha.png")
    
