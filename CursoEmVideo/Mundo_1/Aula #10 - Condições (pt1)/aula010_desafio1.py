'''Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
print('Vamos brincar de adivinhação?')
tentativa = 0
número = randint(0, 5)
for tentativa in range (3):
    palpite = int(input('Digite um número de 0 a 5: '))
    print('PROCESSANDO...')
    sleep(5)
    if palpite > número:
        print('É menor!')
    if palpite < número:
        print('É maior!')
    if palpite == número:
        break
if palpite == número:
    print('Muito bem! Conseguiu acertar o número em {} tentativas! PARABÉNS!'.format(tentativa + 1))
else:
    print('Que pena, você esgotou o número de tentativas. O número que eu estava pensando era {}.'.format(número))
print('---FIM---')