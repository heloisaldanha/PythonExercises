# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27
din = float(input('Quanto dinheiro você tem na carteira?: R$ '))
dol = din / 3.27
print('Com R${} você pode comprar {:.2f} dólares!!'.format(din, dol))

#ok