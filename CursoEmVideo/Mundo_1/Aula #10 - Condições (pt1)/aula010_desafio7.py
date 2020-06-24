'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.'''

salário = float(input('Qual o salário do funcionário? '))
if salário >= 1250:
    novo = salário + (salário * 0.10)
if salário < 1250:
    novo = salário + (salário * 0.15)
print('O salário no valor R${:.2f} fica R${:.2f} com o reajuste.'.format(salário, novo))