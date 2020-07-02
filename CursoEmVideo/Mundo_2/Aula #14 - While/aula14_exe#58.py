'''
Melhore o jogo do desafio 28 onde o computador vai "pensar em um número entre 0 e 10.
Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''
from random import randint

cont = 1
num = randint(0, 10)
palpite = int(input('''Quero saber se você vai adivinhar o número que estou pensando...
Diga um número de 0 a 10: '''))
while palpite != num:
    if palpite > num:
        palpite = int(input('Não acertou, o número é menor... Fala outro: '))
    elif palpite < num:
        palpite = int(input('Não acertou, o número é maior... Fala outro: '))
    cont += 1
print('Você acertou em {} tentativas!'.format(cont))

