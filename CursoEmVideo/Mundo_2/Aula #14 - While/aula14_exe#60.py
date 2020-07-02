'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
ex.: 5! = 5x4x3x2x1 = 120
'''
#  Usando o for:
'''mult = 1
n = int(input('Digite um número e eu direi seu fatorial: '))
for c in range(n, 0, -1):
    mult *= c
print('Calculando Fatorial de {}: {}.'.format(n, mult))'''

#  Usando módulo
'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

#  Usando while
n = int(input('Digite um número para calcular o fatorial: '))
cont = n
mult = 1
print('{}! é: '.format(n), end='')
while cont !=0:
    print('{}'.format(cont), end=' ')
    print('x' if cont != 1 else '=', end=' ')
    mult *= cont
    cont -= 1
print(mult, end='')
