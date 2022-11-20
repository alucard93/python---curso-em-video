import os
os.system('cls')
import math
import random

# ca = 2
# co = 2.5
# h = math.hypot(ca, co)
# # print(h)

# x = float(input())

# seno = round(math.sin(math.radians(x)), 2)
# cos = round(math.cos(math.radians(x)), 2)
# tg = round(math.tan(math.radians(x)), 2)

# # print(seno, cos, tg)

# sorteando um valor de uma lista

# names = list(map(str, input('digite 4 nomes: ').split()))
# sort = random.choice(names)
# print(sort)


# names = list(map(str, input('digite 4 nomes: ').split()))
# random.shuffle(names)
# print(names)

# meu_nome = 'marcus vinicius nascimento ferreira'
# print(meu_nome[-1])
# print(len(meu_nome))
# print(meu_nome.count('a'))
# print(meu_nome.count('i', 0, 14))
# print(meu_nome.find('cu'))
# print(meu_nome.find('cuz'))
# print(meu_nome.upper())
# print(meu_nome.lower())
# print(meu_nome.capitalize())
# print(meu_nome.title())

# cidade_que_nasceu = input('digite a cidade que você nasceu: ').strip()
# print(cidade_que_nasceu[:6].upper() == 'UNAMAR')

from random import randint
#gera um numero randomico de 0 a 5
# computador = randint(0, 5)

# from datetime import date

# ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))

# if ano == 0:
#     ano = date.today().year

# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} NÃO é BISSEXTO'.format(ano))


# cores

#style 0 - none // 1 - bold // 4 - underline // 7 - negative
#cores
    # - cinza - 30
    # - vermelho - 31
    # - verde - 32
    # - amarelo - 33
    # - azul - 34
    # - magenta - 35
    # - ciano - 36
    # - branco - 37

#back - cor de fundo

# 40 - branco // até 47

# print('\033[7;37mQue porra é essa\033[m')
s = 'prova de python'
print(len(s))