'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem nno final, de acordo com a
média atingida:
- Média abaixo de 5.0: REPROVADO!
- Média entre 5.0 e 6.9: RECUPERAÇÃO!
- Média 7.0 ou superior: APROVADO!
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda a nota: '))
média = (nota1 + nota2) / 2
print('\033[35mSua média final é: {}\033[m'.format(média))
if 7 > média >= 5:
    print('\033[33mO aluno está em RECUPERAÇÃO.\033[m')
elif média <5:
    print('\033[31mO aluno está REPROVADO.\033[m')
else:
    print('\033[34mO aluno está APROVADO! Parabéns.\033[m')
