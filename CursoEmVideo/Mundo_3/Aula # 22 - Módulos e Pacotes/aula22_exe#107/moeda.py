'''
Crie um módulo chamado moeda.py(aula22_exe#107) que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''


def aumentar(preco, taxa):  # preço e taxa são parâmetros e escopos locais
    valor = preco + (preco * taxa / 100)
    return valor


def diminuir(preco, taxa):
    valor = preco - (preco * taxa / 100)  # valor também é escopo local
    return valor


def dobro(preco):
    valor = preco * 2
    return valor


def metade(preco):
    valor = preco / 2
    return valor
