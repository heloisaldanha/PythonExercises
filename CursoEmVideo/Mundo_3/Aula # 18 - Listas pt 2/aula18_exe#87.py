'''
aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digtados.
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaColuna = 0
for linha in range(0, 3):  # colocar os valores dentro da matriz
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor para inserir no lugar [{}, {}]: '.format(linha, coluna)))
for linha in range(0,3):  # para mostrar a estrutura na tela
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matriz[linha][coluna]), end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()
print()
for linha in range(0, 3):  # fazer o for pra linha, porque a coluna é fixa
    somaColuna += matriz[linha][2]  # o [2] é a coluna fixa
for coluna in range(0, 3):
    if matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(somaPar)
print(somaColuna)
print(maior)
