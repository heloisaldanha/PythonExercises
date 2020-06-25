'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-la por extenso.
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente novamente.')
print('Você digitou o número {}'.format(extenso[num]))
