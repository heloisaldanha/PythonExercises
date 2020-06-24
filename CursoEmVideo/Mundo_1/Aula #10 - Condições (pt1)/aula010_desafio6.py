# Faça um programa que leia três números inteiros e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
menor = c
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
print('O menor número é {}.'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior número é {}.'.format(maior))
print('fim')