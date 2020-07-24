'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma descrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

l = []
while True:
    n = int(input('Number: '))
    l.append(n)
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if res in 'Nn':
        break
print(l)
print('a) How many numbers was entered? Answer: {} numbers'.format(len(l)))
l.sort(reverse=True)
print('b) The list ordered in descending order. Answer: {}.'.format(l))
if 5 in l:
    c = 'Yes'
    l.count(5)
else:
    c = 'No'
print('c) The number 5 was entered in list? Answer: {}.'.format(c), end=' ')
if c == 'Yes':
    print('{} times.'.format(l.count(5)))