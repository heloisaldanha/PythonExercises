# Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é igual a: {}' .format(n1, n2, s))
# print('A soma entre os números é igual a:', s)

# Inserindo o desafio 2

x = str(s)
print('O resultado é um número?', x.isalnum())
print('O resultado é uma palavra?', x.isalpha())
print('O resultado tem dígito?', x.isdigit())
