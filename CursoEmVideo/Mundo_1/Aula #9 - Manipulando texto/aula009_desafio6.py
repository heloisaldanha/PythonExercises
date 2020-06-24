'''FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
EX: ANA MARIA DE SOUZA
PRIMEIRO = ANA
ÚLTIMO = SOUZA'''

nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n) - 1]))
