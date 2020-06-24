'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos quer pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('\033[34mEmpréstimo CONCEDIDO!!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!!\033[m')
