# Desenvolva um programa que leia duas notas de um aluno e calcule sua média.
nota1 = float(input('Nota da primeira avaliação: '))
nota2 = float(input('Nota da segunda avaliação: '))
print('A nota da primeira unidade foi {:.1f} e a nota da segunda unidade foi {:.1f}'. format(nota1, nota2))
média = (nota1 +nota2) / 2
print('A média desse aluno é igual a {:.1f}'.format(média))

#ok