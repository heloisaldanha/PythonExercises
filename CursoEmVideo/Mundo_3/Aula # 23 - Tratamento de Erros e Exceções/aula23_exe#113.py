'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também a função leiaFloat() com a mesma funcionalidade.
'''


def leiaint(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return numero


def leiafloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número decimal válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return '---'
        else:
            return numero


nInt = leiaint('Digite um número inteiro: ')
nFloat = leiafloat('Digite um número decimal: ')
print(f'Você digitou os números {nInt} e {nFloat}.')
