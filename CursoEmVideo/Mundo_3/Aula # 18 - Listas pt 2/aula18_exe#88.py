'''
faca um programa qie ajude um jogador da mega sena a criar palpites. o programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
'''
# não consegui fazer :(

from random import randint
lista = []  #
jogos = []
quantosJogos = int(input('Quantos jogos você deseja sortear? '))
totalJogos = 1  # o total começa com um pra mostrar no print depois, sem precisar somar +1
while totalJogos <= quantosJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1  # esse contador aqui serve pra contar os 6 números de sorteio
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])  # vai copiar várias listas dentro de uma lista grande
    lista.clear()
    totalJogos += 1
print('Sorteando {} jogos'.format(quantosJogos))
for i, l in enumerate(jogos):
# i é a quantidade de voltas que o for deu, l é cada lista menor dentro de jogos
    print('Jogo {}: {}'.format(i + 1, l))
