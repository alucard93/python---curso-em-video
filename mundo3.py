import os 

os.system('cls')
x = ('arroz', 'feijão', 'queijo')
# x[0] = 'gelatina' #erro tuplas são imutáveis
# print(x)

# for comida in x:
#     print('E vou comer {}'.format(comida))

# for comida in range(0,len(x)):
#     print('Eu vou comer {}'.format(x[comida]))

# for i, comida in enumerate(x):
#     print('Eu vou comer {} que está na posição {}'.format(comida, i))
# print(sorted(x))

# somar tuplas realiza concatenação
a = [2, 3, 4, 5]
# b = (4, 3, 6, 15)
# c = a + b
# print(c) 
# print(c.index(6)) 
# print(len(c))

# nomes = ('zero', 'um', 'dois', 'tres', 'quarto', 'cinco')
# while True:
#     num = int(input())
#     if 0 <= num <= 5:
#         break
#     print('Tente novamente')
# print('VocÊ digitou o número {}'.format(nomes[num]))

# print(max(a))

listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)
# print('-' * 39)
# print(f'{"LISTAGEM DE PRECOS":^39}')
# print('-' * 39)
# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end ='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')
# print('-' * 39)