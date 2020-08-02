'''
faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
a) quantas pessoas foram cadastradas.
b) uma listagem com as pessoas mais pesadas
c) uma listagem com as pessoas mais leves.
'''
# primeiro criar a lista que vai ficar dentro da lista principal:
listaMenor = []
# depois criar a lista maior:
listaMaior = []
# se tem que saber se os valores são maiores ou menores, deve-se criar a variável zerada:
maior = menor = 0  # não tem problema fazer essa ligação com variáveis simples

while True:
    listaMenor.append(str(input('Nome: ').title()))
    listaMenor.append((float(input('Peso: '))))
    if len(listaMaior) == 0:
        maior = menor = listaMenor[1]  # se o índice da maior lista for 0 (ou seja, vai ter UMA lista menor dentro com dois itens), o índice 1 da lista menor vai ser o peso. se só tiver uma lista menor, o peso vai ser o maior ou menor porque só vai ter um.
    else:
        if listaMenor[1] > maior:
            maior = listaMenor[1]
        elif listaMenor[1] < menor:
            menor = listaMenor[1]
    listaMaior.append(listaMenor[:])
    listaMenor.clear()  # é bom limpar a lista menor, senão ela vai ser repetir dentro da lista maior.
    resposta = str(input('Quer continuar? [S/N] - ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('\033[31mOPÇÃO INVÁLIDA\033[m')
        resposta = str(input('Responda usando apenas \033[36m[S]\033[m para sim e \033[36m[N]\033[m para não. Deseja cotinuar? [S/N] - ')).strip().upper()
    if resposta == 'N':
        break
print('Foram cadastradas {} pessoas.'.format(len(listaMaior)))
print('O maior peso encontrado foi o de: ')
for tudo in listaMaior:  # aqui, o programa vai varrer tudo que tá dentro da lista maior. Vai ler cada lista dentro da lista principal. para cada índice 1 (no caso, o que for o maior).
    if tudo[1] == maior:  # quando encontra o peso maior - na posição 1...
        print('[{}] '.format(tudo[0]))  # pegue o que tiver antes dele (o índice 0).
print('Sendo {}kg'.format(maior))
print('O menor peso encontrado foi o de: ')
for tudo in listaMaior:
    if tudo[1] == menor:
        print('[{}] '.format(tudo[0]))
print('Sendo {}kg.'.format(menor))


