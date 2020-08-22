def linha():
    return '-' * 42


def leiaint(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return '---'
        else:
            return numero


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    resposta = leiaint('\033[33mSua opção: \033[m')
    return resposta

