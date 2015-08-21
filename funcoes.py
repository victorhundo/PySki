# coding: utf-8
# Funções do Pyski
# George Araujo: georgeluizsantosaraujo@hotmail.com
# Victor Hugo: victohundo@gmail.com
import pygame, io

relogio = pygame.time.Clock()

# Retorna uma string de contronometro no padrão minutos:segundos:centésimos
def cronometro(tempo):
    tempo_segundos = tempo
    minutos = tempo_segundos/60
    segundos = tempo_segundos % 60
    centesimos = "%.2d" % ((tempo_segundos - int(tempo_segundos))  * 10**2)
    return "%.2d : %.2d : %s" % (minutos,segundos, centesimos)

def mostrar_ranking():
    rank = io.open("ranking.dat", "r")
    string = ""
    for i in range(10):
        string += rank.readline()
    rank.close()
    return string

def ranking(player, score):
    players = []
    scores = []
    add_score(player, score)
    rank = io.open("ranking.dat", "r")
    while True:
        linha = rank.readline().split()
        nome = ""
        if linha == []: break

        for i in range(len(linha) - 1):
            nome += linha[i] + " "
        nome = nome[:-1]

        players.append(nome)
        scores.append(float(linha[-1]))
    rank.close()
    organizar_rank(scores, players)
    add_ranking(players, scores)

def add_score(player, score):
    player = unicode(player)
    score = unicode(score)
    ranking = io.open("ranking.dat", "a",  encoding='utf8')
    ranking.write("%s    %s\n" % (player, score))
    ranking.close()

def organizar_rank(scores, players):
    troca = True
    while troca:
        troca = False
        for i in range(len(scores) - 1):
            if scores[i] < scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]
                players[i], players[i+1] = players[i+1], players[i]
                troca = True

def add_ranking(players, scores):
    rank = io.open("ranking.dat", "w")
    for i in range(len(players)):
        mensagem = "%s    %s" % (players[i], scores[i])
        rank.write("%s\n" % mensagem)
    rank.close()
