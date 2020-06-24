'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da
passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''

distância = float(input('Qual a distância da viagem, em km? '))
print('Você está prestes a começar uma viagem de {:.2f}km.'.format(distância))
if distância <= 200:
    custo1 = distância * 0.50
    print('E o preço da sua passagem será de R${:.2f}.'.format(custo1))
else:
    custo2 = distância * 0.45
    print('E o preço da sua passagem será de R${:.2f}.'.format(custo2))

