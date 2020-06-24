'''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
1 - O NOME COM TODAS AS LETRAS MAIÚSCULAS
2 - O NOME COM TODAS AS LETRAS MINÚSCULAS
3 - QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS)
4 - QUANTAS LETRAS TEM O PRIMEIRO NOME'''

nomeCompleto = input('Qual seu nome completo? ').strip()
print('Letras maiúsculas: {}.'.format(nomeCompleto.upper()))
print('Letras minúsculas: {}.'.format(nomeCompleto.lower()))
lista = nomeCompleto.split()
nome1 = lista[0]
nome2 = lista[1]
print('Quantas letras tem o primeiro nome, sem contar os espaços? {}.'.format(len(nome1)))
print('(contando quantas letras têm na) Segunda palavra {}.'.format(len(nome2)))

### LEMBRAR QUE LEN CONTA QUANTAS PALAVRAS EXISTEM ESCRITAS