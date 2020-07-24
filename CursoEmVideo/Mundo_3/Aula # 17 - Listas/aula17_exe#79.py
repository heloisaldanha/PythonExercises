'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.
'''

l = []
resposta = ()
while resposta != 'N':
    resposta = ()
    n = int(input('Digite um número: '))
    if n in l:
        print('Esse número já está na lista.')
        while resposta != 'N' and resposta != 'S':
            resposta = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()
            if resposta == 'N':
                break
    else:
        l.append(n)
        while resposta != 'N' and resposta != 'S':
            resposta = str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()
            if resposta == 'N':
                break
l.sort()
print(l)