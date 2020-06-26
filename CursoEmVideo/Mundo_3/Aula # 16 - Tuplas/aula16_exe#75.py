'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,  mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares
'''
n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print('Você digitou os valores: {}'.format(n))
print('O número 9 aparece {} vezes.'.format(n.count(9)))
if 3 in n:
    print('O número 3 apareceu na posição {}.'.format(n.index(3) + 1))
else:
    print('\033[31mO número 3 não foi digitado\033[m')
print('Os valores pares digitados foram:')
for cont in n:
    if cont % 2 == 0:
        print(cont)





