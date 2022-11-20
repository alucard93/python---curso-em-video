import os
os.system('cls')
# num = int(input('Digite um número inteiro: '))
# print('''Escolha uma das bases para conversão: 
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL
# ''')
# opcao = int(input('Sua opção: '))

# if opcao == 1:
#     print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

# elif opcao == 2:
#     print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

# elif opcao == 3:
#     print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

# for x in range(1, 10,-1):
#     print(x)

# for y in range(1, 10, 3):
#     print(y)

# for z in range(10, 3):
#     print(y)

# num = int(input('digite um número: '))
# for a in range(0 , num + 1):
#     print(a)


# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))

# for c in range(inicio, fim + 1, passo):
#     print(c)


# for c in range(0,3):
#     n = int(input('Digite um valor: '))
# print('fim')

# from time import sleep

# num = int(input('digite um número: '))
# for c in range(10, -1, -1):
#     print(c)
#     sleep(1)
#     if(c == 0):
#         print('BUMMMMMMMM')

# for n in range(1, 51):
#     if n % 2 == 0:
#         print(n)
# sum = 0
# count = 0
# for n in range(1, 501, 2):
#     if(n % 3 == 0):
#         sum += n
#         count += 1
#     print(sum, count)

# sum = 0
# count = 0

# for x in range(1,7):
#     num = int(input('Digite o {} valor: '.format(x)))
#     if x % 2 == 0:
#         sum += x
#         count += 1
# print(sum, count)

num = int(input('Digite um número: '))
count = 0
for x in range(1, num +1):
    if num % x == 0:
        count += 1
if count == 2:
    print('\033[33m {} \033[m é primo'.format(x))
elif count > 2:
    print('não é primo')


