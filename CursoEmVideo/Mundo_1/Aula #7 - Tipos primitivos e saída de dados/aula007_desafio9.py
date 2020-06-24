# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salário1 = float(input('Salário: R$ '))
#salário2 = salário1 + (salário1 * 0.15)
salário2 = salário1 + (salário1 * 15 / 100)
print('O salário anterior no valor de {:.2f} reais, teve um aumento de 15% e ficou no valor de {:.2f} reais.'.format(salário1, int(salário2)))

#ok