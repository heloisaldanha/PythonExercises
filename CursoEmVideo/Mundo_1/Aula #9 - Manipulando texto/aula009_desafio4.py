'''CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM SILVA NO NOME'''

nome = str(input('Nome completo: ')).strip().title().split()
print(bool('Silva' in nome))
