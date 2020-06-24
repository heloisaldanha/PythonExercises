# Faça um programa que leia um ano qualquer e mostre se ele é ano bissexto.
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))