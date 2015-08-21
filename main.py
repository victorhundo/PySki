# coding: utf-8
# Pyski
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import sys, pygame, os, menu, funcoes, random
from vida import *
from skiador import *
from obstaculo import *
from homem_neve import *
from mouse import *
from time import sleep
pygame.init()
pygame.display.set_caption( 'Pyski' )

# Propriedades da tela
tamanho = largura, altura = 800, 600
branco = 255,255,255
tela = pygame.display.set_mode(tamanho, pygame.FULLSCREEN)
barra_menu = pygame.image.load("img/barra_menu.png")

# Efeitos Sonoros
trilha_sonora = pygame.mixer.Sound("ost/som.wav")
som_batida = pygame.mixer.Sound("ost/batida.wav")
tema_inicial = pygame.mixer.Sound("ost/tema_inicial.wav")

font = pygame.font.SysFont("arial", 30)
font_menor = pygame.font.SysFont("arial", 25)
relogio = pygame.time.Clock()

def main():
    tema_inicial.stop()
    trilha_sonora.play(-1)

    logo_jogo = pygame.image.load("img/logo_pyski.png")
    logo_jogo  = pygame.transform.scale(logo_jogo, (72, 22))

    # Objetos da cena
    skiador = Skiador(tela)
    homem_neve = Homem_neve(tela)
    vida = Vida(tela)

    qtd_obstaculos = 10
    obstaculos = []
    for obstaculo in range(qtd_obstaculos):
        obstaculo = Obstaculo(tela)
        obstaculos.append(obstaculo)
    
    rodando = True
    img_vida = pygame.image.load("img/vida.gif")
    relogio.tick()
    tempo = 0
    tempo0_colisao = 0
    while rodando:
        segundo = float(relogio.tick()) * 10**-3
        tempo += segundo
        pontuacao = funcoes.cronometro(tempo)
        texto_vida = font.render("x0" + str(skiador.vida), True, (0,0,0))
        texto_pontuacao = font_menor.render(pontuacao,  True, branco)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        skiador.esconder_mouse()

        skiador.mover(mouse_x, 70)

        homem_neve.mover(mouse_x, obstaculos[0].velocidade)

        vida.mover(obstaculos[0].velocidade)
        vida.mostrar()
        
        if pygame.sprite.collide_mask(skiador,vida):
            if not(skiador.vida > 2):
                skiador.vida += 1
                vida.pos_y = -55

        if skiador.invencivel:
            imagem_anterior = skiador.imagem
            skiador.mover(mouse_x + 0.01, 70)
            skiador.mostrar_skiador()
            skiador.ativar_invencibilidade(tempo0_colisao, tempo)

        pygame.display.flip()
        for obstaculo in obstaculos:
            obstaculo.mover(tempo)

            if pygame.sprite.collide_mask(skiador,obstaculo):
                if not(skiador.invencivel):
                    tempo0_colisao = tempo
                    som_batida.play()
                    for obstaculo in obstaculos:
                        obstaculo.houve_colisao()
                    skiador.invencivel = True
                    skiador.vida -= 1

        if pygame.sprite.collide_mask(skiador,homem_neve):
            if not(skiador.invencivel):
                skiador.vida -= 3

        if skiador.vida <= 0:
            imagem = pygame.image.load("img/sangue.png")
            imagem  = pygame.transform.scale(imagem, (30, 30))
            skiador.imagem = imagem

            skiador.mostrar_skiador()
            pygame.display.flip()
            sleep(1)
            trilha_sonora.stop()

            menu.menu_final(tempo, skiador, obstaculos, homem_neve)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.display.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.pause()
                    pausa()
        
                if event.key == pygame.K_SPACE:
                    skiador.vida -= 1
        
        tela.fill(branco)        
        
        skiador.mostrar_skiador()
        homem_neve.mostrar()

        for obstaculo in obstaculos:
            obstaculo.mostrar_obstaculo()

        tela.blit(barra_menu, (0,-3))
        pos_vida = 50
        for i in range(skiador.vida):
            tela.blit(img_vida, (pos_vida, 5))
            pos_vida += 40

        tela.blit(texto_pontuacao, (320, 0))
        tela.blit(logo_jogo, (700, 5))
        pygame.display.flip()

def pausa():
    font_pequena = pygame.font.SysFont("arial", 15)
    logo = pygame.image.load("img/logo_pyski.png")
    menu_pausa = pygame.image.load("img/menu.png")
    txt_pausa = font.render("PAUSA", True, branco)
    txt_aviso1 = font_pequena.render("Pressione ESC para ir ao menu inicial", True, branco)
    txt_aviso2 = font_pequena.render("CLICK para voltar ao jogo", True, branco)
    
    tela.blit(menu_pausa, (250,80))
    tela.blit(txt_pausa, (360, 300))
    tela.blit(txt_aviso1,(290, 460)) 
    tela.blit(txt_aviso2,(330, 480))  
    tela.blit(logo, (335, 250))
    pygame.display.flip()

    pausa = True
    while pausa:
        relogio.tick()
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    tema_inicial.play(-1)
                    menu.menu_inicial()

            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    pausa = False
            

    
    pygame.mixer.unpause()
    
