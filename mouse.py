# coding: utf-8
# Mouse
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame

class Mouse():
    
    def __init__(self, tela):
        self.tela = tela
        self.imagem = pygame.image.load("img/mouse.png")
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)
        self.pos = (50,50)

    def mostrar(self, pos):
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        return self.tela.blit(self.imagem, self.pos)

    def mudar_img(self):
        self.imagem = pygame.image.load("img/mouse_sobre.png")
