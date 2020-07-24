'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as respectivas posições na lista.
'''

cont = 0
n = []
while cont != 5:
    n.append(int(input('Digite um número: ')))
    cont += 1
print('A lista com os números escolhidos é: {}.'.format(n))
n.sort()
print('o menor número é {} e o maior número é {}.'.format(n[0], n[-1]))

