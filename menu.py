# coding: utf-8
# Funções de Menus
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com

import pygame, sys, os, funcoes, io
from unicodedata import *
from mouse import *
from botao import *
from main import *
from skiador import *
from obstaculo import *
from homem_neve import *
from time import sleep

pygame.init()
pygame.display.set_caption( 'Pyski' )
font = pygame.font.SysFont("arial", 20)

tamanho = largura, altura = 800, 600
branco = 255, 255, 255
tela = pygame.display.set_mode(tamanho, pygame.FULLSCREEN)
img_fundo = pygame.image.load("img/principal.jpeg")
cursor = Mouse(tela)    

tema_inicial = pygame.mixer.Sound("ost/tema_inicial.wav")
imagem_menu = pygame.image.load("img/menu.png")

# Tela ao iniciar o jogo, mostra o simbolo da instituição e do curso
def tela_inicial():
    font = pygame.font.SysFont("Cyberbit.ttf", 12)
    pygame.mouse.set_visible(False)
    tela.fill(branco)
    sleep(3)

    tema_inicial.play(-1)
    
    logo = pygame.image.load("img/logo_ufcg.png")
    tela.blit(logo, (190,150))
    pygame.display.flip()
    sleep(5)
    
    logo = pygame.image.load("img/logo_computacao.jpg")
    aviso = u"JOGO DESENVOLVIDO POR ALUNOS PARA A DISCIPLINA DE PROGRAMAÇÃO  1"
    texto_aviso = font.render(aviso, True, (0,0,0))
    tela.blit(texto_aviso,(240,560))
    tela.blit(logo, (170,150))
    pygame.display.flip()
    sleep(5)
    menu_inicial()

# Menu que liga as funcionalidades do jogo
def menu_inicial(): 
    qtd_botao = 5
    textos_botao = ["Iniciar",u"Instruções","Recordes","Sobre","Sair"]
    botoes = []
    for i in range(qtd_botao):
        botao = Botao(tela)
        botao.texto = textos_botao[i]
        botao.redimensionar(150,50)
        botoes.append(botao)

    rodando = True
    pygame.mouse.set_visible(False)
    while rodando:
        pos_mouse = pos_mouse_x, pos_mouse_y = pygame.mouse.get_pos()
 
        LIMITE_BOTAO_X = pos_mouse_x > 20 and pos_mouse_x < 170
        LIMITE_1 = LIMITE_BOTAO_X and (pos_mouse_y > 300 and pos_mouse_y < 350)
        LIMITE_2 = LIMITE_BOTAO_X and (pos_mouse_y > 355 and pos_mouse_y < 405)
        LIMITE_3 = LIMITE_BOTAO_X and (pos_mouse_y > 410 and pos_mouse_y < 460)
        LIMITE_4 = LIMITE_BOTAO_X and (pos_mouse_y > 465 and pos_mouse_y < 515)
        LIMITE_5 = LIMITE_BOTAO_X and (pos_mouse_y > 520 and pos_mouse_y < 570)
        LIMITES = [LIMITE_1,LIMITE_2,LIMITE_3,LIMITE_4,LIMITE_5]

        tela.fill(branco)
        tela.blit(img_fundo, (0,0))
        botao_y = 300
        for botao in botoes:
            botao.mostrar_botao(20,botao_y)
            texto = font.render(botao.texto, True, branco)
            tela.blit(texto, (40, botao_y + 15))
            botao_y += 55        
        cursor.mostrar(pos_mouse)

        img_selecao = pygame.image.load("img/homem_neve.png")
        for i in range(len(LIMITES)):
            if LIMITES[i]:
                tela.blit(img_selecao,(175, 300 + 55 * i))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIMITES[0]:
                    tema_inicial.stop()
                    main()
                elif LIMITES[1]:
                    sub_menu("instrucoes")
                elif LIMITES[2]:
                    sub_menu("recordes")                    
                elif LIMITES[3]:
                    sub_menu("sobre")
                elif LIMITES[4]:
                    rodando = False
                    pygame.display.quit()


def sub_menu(tipo):
    botao = Botao(tela)
    botao.texto = "Voltar"
    botao.redimensionar(150,50)
    while True:
        pos_mouse = pos_mouse_x, pos_mouse_y = pygame.mouse.get_pos()
        tela.fill(branco)
        menu = pygame.image.load("img/menu.png")
        menu = pygame.transform.scale(menu, (513,490))
        
        LIMITE_BOTAO_X = pos_mouse_x > 20 and pos_mouse_x < 170
        LIMITE = LIMITE_BOTAO_X and (pos_mouse_y > 520 and pos_mouse_y < 570)
        
        tela.blit(img_fundo, (0,0))
        tela.blit(menu, (200,100))
        botao.mostrar_botao(20,520)
        texto = font.render(botao.texto, True, branco)
        tela.blit(texto, (40, 520 + 15))

        if tipo == "instrucoes":
            img = pygame.image.load("img/instrucoes.png")
            tela.blit(img, (240,150))
        
        elif tipo == "sobre":
            img = pygame.image.load("img/sobre.png")
            tela.blit(img, (240,150))

        elif tipo == "recordes":
            recorde_img = pygame.image.load("img/recordes.png")
            tela.blit(recorde_img, (330,160))
            rank = io.open("ranking.dat", "r") 
            pos_y = 240
            for i in range(10):
                txt = rank.readline().split()
                if txt == []: break
                
                if i == 9:
                    txt[0] = str(i+1) + ". " + txt[0]
                else:
                    txt[0] = str(i+1) + ".   " + txt[0]                

                txt[0] += "    " + funcoes.cronometro(float(txt[1]))
                txt = txt[0]
                tela.blit(font.render(txt, True, branco), (240,pos_y))
                pos_y += 30
            

        cursor.mostrar(pos_mouse)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIMITE:
                    menu_inicial()

def menu_final(tempo,skiador, obstaculos, homem_neve):
    texto_fim = font.render("FIM DE JOGO", True, branco)
    pontuacao = funcoes.cronometro(tempo)
    texto_pontuacao = font.render(pontuacao, True, branco)
    texto_aviso = font.render("Enter para Jogar", True, branco)
    nome_usuario = ""

    imagem_input = pygame.image.load("img/input-field.png")
    imagem_input = pygame.transform.scale(imagem_input, (234,46))
    imagem_menu = pygame.image.load("img/menu.png")
    imagem_logo = pygame.image.load("img/logo_pyski.png")
    font_menor = pygame.font.SysFont("arial", 12)
    
    rodando = True
    while rodando:
        tela.fill(branco)
        skiador.mostrar_skiador()
        for obstaculo in obstaculos:
            obstaculo.mostrar_obstaculo()
        
        homem_neve.mostrar()

        texto_nome_usuario = font.render(nome_usuario, True, (0,0,0))
        texto_digite_nome = font_menor.render("Digite seu nome", True, branco)

        tela.blit(imagem_menu, (250,80))
        tela.blit(imagem_input, (285,190))
        tela.blit(texto_pontuacao, (355, 150))
        tela.blit(texto_nome_usuario, (300,200))
        tela.blit(texto_fim, (340, 380))
        tela.blit(texto_aviso, (330, 480))
        tela.blit(texto_digite_nome, (360, 240))
        tela.blit(imagem_logo, (335, 330))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.display.quit()

            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if len(nome_usuario) <= 10:
                        nome_usuario += event.unicode.upper()
                elif event.key == pygame.K_BACKSPACE:
                    nome_usuario = nome_usuario[:-1]

                elif event.key == pygame.K_RETURN:
                    if nome_usuario == "":
                        nome_usuario = "JOGADOR"
                    funcoes.ranking(nome_usuario, tempo)
                    main()

