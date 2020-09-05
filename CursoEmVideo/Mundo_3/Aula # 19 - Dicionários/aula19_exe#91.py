'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
# eu
from random import randint
pessoas = {}
jogador1 = randint(1, 6)
jogador2 = randint(1, 6)
jogador3 = randint(1, 6)
jogador4 = randint(1, 6)
pessoas['jogador 1'] = jogador1
pessoas['jogador 2'] = jogador2
pessoas['jogador 3'] = jogador3
pessoas['jogador 4'] = jogador4

print(pessoas)

#  item = jogo
#  chave = jogadores
#  valor = número aleatório
#  gustavo
from random import randint
from operator import itemgetter  # para ordenar um dicionario, precisa importar itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = {}
print('Valores sorteados:')
for k, v in jogo.items():
    print('O {} tirou: {}'.format(k, v))             # reverse para inverter a ordem
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # key=itemgetter(1) para ordenar os valores do item 1 de jogoss .e fosse item 0 seriam as chaves a mudar.
print(ranking)
for i, v in enumerate(ranking):
    print('{} lugar: {} com {}'.format(i + 1, v[0], v[1]))
