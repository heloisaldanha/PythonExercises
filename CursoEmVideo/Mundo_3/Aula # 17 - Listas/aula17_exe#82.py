'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas
'''

num = []
while True:   # o loop infinito
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] - ')).strip().upper()
    while resposta != 'N' and resposta != 'S':
        resposta2 = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()
        if resposta2 == 'N':
            break
    if resposta in 'Nn':
        break
print(num)
