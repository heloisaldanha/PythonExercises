'''
Crie um programa que tenha um tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são suas vogais.
'''

palavras = ('arroz', 'computador', 'piscina', 'copo', 'dentista',
            'lazer', 'mouse', 'telefone', 'vestido', 'bermuda', 'aspirador')

for p in palavras:
    print('\nNa palavra {} temos '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
