# Como saber qual a classe de uma variável.

n1 = input('Digite um valor (n1): ')
print(type(n1))

# Como mudar essa variável str para int?
n2 = int(input('Digite um número (n2): '))
print(type(n2))

# Como dizer que a soma de número tal com número tal, dá tanto?
número_1 = int(input('Digite um número: '))
número_2 = int(input('Digite outro número: '))
soma = número_1 + número_2
# print('A soma de ', número_1, 'mais ', número_2, 'é igual a: ', soma)
print('A soma entre {} e {} é igual a: {}'.format (número_1, número_2, soma))