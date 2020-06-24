'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.'''
from math import cos, sin, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
print('''O ângulo de {} tem:
Seno de {:.2f}
Cosseno de {:.2f}
Tangente de {:.2f}.'''.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
