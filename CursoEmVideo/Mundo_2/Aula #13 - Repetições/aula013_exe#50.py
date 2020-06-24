# ler 6 números inteiros e somar só os números pares
s = 0
for n in range(6):
    num = int(input('Digte um número: '))
    if num % 2 ==0:
        s = s + num
print('Você me informou {} números pares e a soma foi {}'.format(n + 1, s))


