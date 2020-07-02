'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resposta = 0
while resposta != 5:
    print('''Escolha uma opção para realizar a operação com os dois números escolhidos:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    resposta = int(input('Escolha: '))
#   Colocar o menu no início do while pro programa não rodar infinito.
    if resposta == 1:
        print('SOMA: {} + {} = {}.'.format(n1, n2, n1 + n2))
        sleep(2)
    elif resposta == 2:
        print('MULTIPLICAÇÃO: {} x {} = {}.'.format(n1, n2, n1 * n2))
        sleep(2)
    elif resposta == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
            sleep(2)
        elif n1 < n2:
            print('O número {} é maior que o número {}.'.format(n2, n1))
            sleep(2)
        else:
            print('Os números são iguais, tente novamente.')
            sleep(2)
    elif resposta == 4:
        print('Insira novos números!')
        sleep(2)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida! Tente novamente.')
if resposta == 5:
    print('FIM DO PROGRAMA')