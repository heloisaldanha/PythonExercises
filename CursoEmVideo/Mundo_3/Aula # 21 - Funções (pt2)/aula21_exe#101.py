'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal, indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
'''

# Voto negado: < 16 anos
# Voto opcional: 16 <= 18 e > 65 anos
# Voto obrigatório: 18 <= < 65 anos


def voto():
    from datetime import datetime
    idade = datetime.now().year - dataNascimento
    if idade < 16:
        return f'Com {idade} anos o \033[36mvoto é NEGADO.\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o \033[33mvoto é OPCIONAL.\033[m'
    return f'Com {idade} anos o \033[31mvoto é OBRIGATÓRIO.\033[m'


dataNascimento = int(input('Ano de nascimento: '))
print(voto())