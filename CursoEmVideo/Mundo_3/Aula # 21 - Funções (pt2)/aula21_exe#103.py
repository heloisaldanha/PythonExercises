'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gols(s) no campeonato.')


nome = str(input('Nome: '))
quantidadeGols = str(input('Quantos gols: '))
if quantidadeGols.isnumeric():
    quantidadeGols = int(quantidadeGols)
else:
    quantidadeGols = 0
if nome.strip() == '':
    ficha(gols=quantidadeGols)
else:
    ficha(nome, quantidadeGols)


