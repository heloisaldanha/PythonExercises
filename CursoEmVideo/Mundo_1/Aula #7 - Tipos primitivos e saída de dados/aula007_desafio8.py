# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preço1 = float(input('Qual o preço original? R$ '))
desconto = preço1 - (preço1 * 0.05)
# desconto = preço - (preço1 * 5 / 100) --- [também pode ser feito assim]
print('O valor normal do produto é {:.2f} reais. Com 5% de desconto fica R${:.2f}.'.format(preço1, desconto))

#ok