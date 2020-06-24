# Faça um programa que leia um número inteiro e mostra na tela seu sucessor e antecessor.
n = int(input('Digite um número: '))
su = n+1
an = n-1
print('O número sucessor de {} é {}.'.format(n, su))
print('E o número antecessor de {} é {}.'.format(n, an))

### PODE SER TAMBÉM ###
# n = int(input('Digite um número: '))
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n, (n-1), (n+1)))

#ok