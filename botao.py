# coding: utf-8
# Botão
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame

class Botao():
    
    def __init__(self,tela):
        self.tela = tela
        self.imagem = pygame.image.load("img/botao.png")
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)
        self.texto = ""
        self.altura = self.imagem.get_height()
        self.largura = self.imagem.get_width()
        self.pos = (0,0)

    def mostrar_botao(self, pos_x, pos_y):
        self.pos = pos_x, pos_y
        self.rect.x = pos_x
        self.rect.y = pos_y
        return self.tela.blit(self.imagem, self.pos)

    def redimensionar(self,altura, largura):
        self.imagem  = pygame.transform.scale(self.imagem, (altura, largura))

