# coding: utf-8
# Classe Skiador
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame
class Skiador():
	
    def __init__(self,tela):
        self.tela = tela
        self.imagem = pygame.image.load("img/skiador.png")
        self.pos = (180,50)
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)
        self.pontuacao = 0
        self.vida = 3
        self.contador_img_frontal = 0
        self.invencivel = False
        self.periodo_invencivel = 3
    
    def esconder_mouse(self):
        pygame.mouse.set_visible(False)

    def mover(self, x, y):
        antiga_posicao = self.pos[0]

        if x < 90:
            x = 90
        elif x > 670:
            x = 670

        if x  > antiga_posicao:
            self.imagem = pygame.image.load("img/skiador_direita.png")
        elif x  < antiga_posicao:
            self.imagem = pygame.image.load("img/skiador_esquerda.png")
        else:
            self.contador_img_frontal += 1

        if self.contador_img_frontal > 50:
            self.imagem = pygame.image.load("img/skiador.png")
            self.contador_img_frontal = 0

        if self.invencivel:
            self.imagem = pygame.image.load("img/skiador.png")

        self.rect.x = x
        self.rect.y = y
        self.pos = (self.rect.x , self.rect.y)

    def mostrar_skiador(self):
        return self.tela.blit(self.imagem, self.pos)

    def ativar_invencibilidade(self,tempo_inicial, tempo_final):
       self.imagem = pygame.image.load("img/invisivel.png")
       if tempo_final - tempo_inicial >= self.periodo_invencivel:
           self.invencivel = False


