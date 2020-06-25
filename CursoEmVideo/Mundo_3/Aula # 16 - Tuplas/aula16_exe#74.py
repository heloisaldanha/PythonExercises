'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor estão
na tupla.
'''
from random import randint
num = (randint(0, 101), randint(0, 101),
       randint(0, 101), randint(0, 101),
       randint(0, 101))
print(num)
maior = max(num)
menor = min(num)
print('O maior número é: {}'.format(maior))
print('O menor número é {}'.format(menor))

