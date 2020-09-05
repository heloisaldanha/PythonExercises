'''
crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
no final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''
ficha = []

while True:
    nome = str(input('nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? \033[36m[S]\033[m para sim / \033[36m[N]\033[m para não: ').strip().upper())
    while resposta != 'S' and resposta != 'N':
        print('\033[31mResposta inválida, tente novamente.\033[m')
        resposta = str(input('Deseja continuar? \033[36m[S]\033[m para sim / \033[36m[N]\033[m para não: ')).strip().upper()
    if resposta == 'N':
        break
print(ficha)
print('-=' * 15)
print('{:<4}{:<15}{:>8}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 30)
for voltas, listaPequena in enumerate(ficha):
# dentro da ficha, existem pequenas listas que contém o nome do aluno, as notas e a média. chamei as listas internas de listasPequenas. listasPequenas, no índice 0 tem os nomes. no índice 1 tem as notas 1 e 2 e no índice 2 tem a média.

# voltas é a quantidade de voltas que o for dá.
    print('{:<4}{:<15}{:>8}'.format(voltas + 1, listaPequena[0], listaPequena[2]))
while True:
    print('-' * 30)
    resposta = int(input('''Digite o número do aluno para abrir as notas:
(aperte 0 para sair) '''))
    if resposta == 0:
        break
    elif resposta <= len(ficha) + 1:
        print('Notas de {}: {}'.format(ficha[resposta - 1][0], ficha[resposta - 1][1]))
print('''

''')
print('\033[7mFIM DO PROGRAMA\033[m')
