# coding: utf-8
# Classe Homem_neve
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame
import random
class Vida():
    
    def __init__(self,tela):
        self.tela = tela
        self.imagem = pygame.image.load("img/vida.gif")
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)
        self.pos_y = 800 #random.randint(800, 850)
        self.pos_x = random.randint(90, 670)
        self.pos = (self.pos_x, self.pos_y)
        self.aparece = False
        self.qtd_aparicao = 0

    def mover(self, velocidade):
        if self.pos_y < -55:
            self.pos_y = 800 #random.randint(800, 850)
            self.pos_x = random.randint(90, 670)
            self.aparece = False
            self.qtd_aparicao += 1
            
        self.vai_aparecer()
        if self.aparece:
            self.pos_y -= velocidade

        self.rect.x, self.rect.y = self.pos_x, self.pos_y
        self.pos = (self.pos_x, self.pos_y)
        
    def mostrar(self):
        return self.tela.blit(self.imagem, self.pos)

    def vai_aparecer(self):
        if random.randint(1,2000) == 1:
            self.aparece = True
