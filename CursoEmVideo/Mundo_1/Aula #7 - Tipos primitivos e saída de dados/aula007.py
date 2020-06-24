n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
ex = n1 ** n2
print('a soma é {}, \no resultado da multiplicação é {} \ne a divisão é {:.3f}'.format (s, m, d, end=' ')
print('\nO resultado inteiro da divisão é {}, \no resto é {} \ne a potência é igual a {}'.format(di, mod, ex))

