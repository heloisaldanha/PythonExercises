'''
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
os valores como um valor monetário formatado.
'''


def aumentar(preco=0, taxa=0):  # preço e taxa são parâmetros e escopos locais
    valor = preco + (preco * taxa / 100)
    return valor


def diminuir(preco=0, taxa=0):
    valor = preco - (preco * taxa / 100)  # valor também é escopo local
    return valor


def dobro(preco=0):
    valor = preco * 2
    return valor


def metade(preco=0):
    valor = preco / 2
    return valor


def moeda(preco=0, moeda='R$'):  # moeda função // moeda parâmetro
    return f'{moeda}{preco:.2f}'.replace('.', ',')
