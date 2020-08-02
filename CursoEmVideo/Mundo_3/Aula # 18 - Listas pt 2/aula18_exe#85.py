'''
crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente.
'''
listaCompleta = [[], []]
for c in range(1, 8):
    num = (int(input('Número {}: '.format(c))))  # cria uma variável simples, primeiro, para que o número possa fazer operações matemáticas (nesse caso, o resto da divisão). Se fosse fazer em lista diretamente, não teria como fazer essa verificação.
    if num % 2 == 0:
        listaCompleta[0].append(num)
    else:
        listaCompleta[1].append(num)
listaCompleta[0].sort()
listaCompleta[1].sort()
print('Os valores pares são: {}'.format(listaCompleta[0]))
print('Os valores ímpares são: {}'.format(listaCompleta[1]))
