#ler um número inteiro e dizer se o número é ou não um número primo
from time import sleep
num = int(input('Enter a number: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mThe number {} was divisible {} times.'.format(num, tot))
sleep(4)
print('')
print('Knowing the prime numbers are divisible for only 1 and for itself...')

sleep(5)
if tot ==2:
    print('The number {} IS A PRIME NUMBER.'.format(num))
else:
    print('The number {} IS NOT A PRIME NUMBER.'.format(num))
