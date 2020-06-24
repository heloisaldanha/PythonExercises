'''
Crie um programa que faça o computador jogar jokenpô com você.
'''

from random import randint
print('''Suas opções:
[0] PEDRA
[5] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
jogadaComp = randint[0, 2, 5]
if jogada == 0:
    if jogadaComp == 0:
        print('EMPATE')
        



