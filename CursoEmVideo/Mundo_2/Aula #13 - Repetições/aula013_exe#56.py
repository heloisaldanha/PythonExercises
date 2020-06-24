# ler nome, idade e sexo de 4 pessoas... a média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos

for p in range(1, 5):
    print('PESSOA NÚMERO {}'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
