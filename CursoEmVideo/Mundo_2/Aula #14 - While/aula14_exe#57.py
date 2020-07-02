'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''



sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while sexo not in 'M' and sexo not in 'F': # tudo o que estiver dentro das aspas entra
    sexo = str(input('Dados inválidos, tente outra vez. [M/F]: ')) #  colocar o recebimento novamente, senão vai rodar infinitamente
print('O sexo escolhido foi {}'.format(sexo))
