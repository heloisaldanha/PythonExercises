'''
Faça um programa que leia o nome e a média final de um aluno, guardando
também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
# eu
aluno = {}
nome = str(input('Nome: ')).strip().title()
media = float(input('Média: '))
aluno['nome'] = nome
aluno['média'] = media
if media < 5:
    aluno['situação'] = 'reprovado'
elif 5 <= media < 7:
    aluno['situação'] = 'recuperação'
elif media >= 7:
    aluno['situação'] = 'aprovado'
print(aluno)'''

# gustavo
aluno = {}
aluno['nome'] = str(input('Nome: '))  # como receber um dado para o dicionário
aluno['média'] = float(input('Média de {}: '.format(aluno['nome'])))

print(aluno)
