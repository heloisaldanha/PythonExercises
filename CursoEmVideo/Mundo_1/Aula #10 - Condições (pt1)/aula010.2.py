# Saber se o aluno foi aprovado ou não
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('A média do aluno foi: {:.1f}'.format(média))
if média >= 7.0:
    print('Aprovado!')
else:
    print('Recuperação.')