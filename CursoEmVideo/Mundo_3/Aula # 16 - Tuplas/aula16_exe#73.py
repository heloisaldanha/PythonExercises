'''
Crie uma tupla preenchida com os 20 times do brasileirão da série A na ordem de colocação.
Depois mostre:
a: Os 5 primeiros colocados
b: Os últimos 4 colocados
c: times em ordem alfabética
d: em que posição está o time da Chapecoense?
'''

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('Os 5 primeiros colocados são: {}'.format(times[0:5]))
print('Os 4 últimos colocados: {}'.format(times[-4:]))
print('Os times em ordem alfabética: {}'.format(sorted(times)))
print('O Chapecoense está na posição: {}'.format(times.index('Chapecoense') + 1))
