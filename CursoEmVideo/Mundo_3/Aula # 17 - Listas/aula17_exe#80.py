'''
Crie um programa que o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort())

No final, mostre a lista ordenada na tela.
'''
lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  #se n for maior que o número que está no último elemento.
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print('A lista na posição é {}'.format(lista))