'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
'''
valor1 = int(input('Digite um número inteiro qualquer: '))
valor2 = int(input('Digite outro valor inteiro qualquer: '))
if valor1 > valor2:
    print('O primeiro valor é {} e ele é maior que o segundo valor, que é {}.'.format(valor1, valor2))
elif valor1 < valor2:
    print('O segundo valor é {} e ele é maior que o primeiro valor, que é {}.'.format(valor2, valor1))
else:
    print('Não existe valor maior, os dois são iguais, {}.'.format(valor2))
