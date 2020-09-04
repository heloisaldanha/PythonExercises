'''
crie um programa que crie uma matriz de dimensão 3x3 e a preencha com valores lidos pelo teclado.
no final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):  # colocar os valores dentro da matriz
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para inserir no lugar [{}, {}]: '.format(linha, coluna)))
for linha in range(0,3):  # para mostrar a estrutura na tela
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matriz[linha][coluna]), end='')
    print()
