'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetros a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
'''


def aumentar(preco=0, taxa=0, formatado=False):  # preço e taxa são parâmetros e escopos locais
    '''
    -> aumento de x% em cima do preço de um determinado produto
    :param preco: o preço do produto
    :param taxa: porcentagem dada em cima do preço do produto
    :param formatado: formatação da moeda com troca do ponto final pela vírgula,
    adicionando duas casas decimais e R$ como parâmetro não-obrigatório.
    :return: valor do produto com o acréscimo da taxa em cima do preço
    '''
    valor = preco + (preco * taxa / 100)
    return valor if formatado is False else moeda(valor)


def diminuir(preco=0, taxa=0, formatado=False):
    '''
    -> desconto de x% em cima de um preço de um determinado produto
    :param preco: o preço do produto
    :param taxa: porcentagem dada em cima do preço do produto
    :param formatado: formatação da moeda com troca do ponto final pela vírgula,
    adicionando duas casas decimais e R$ como parâmetro não-obrigatório.
    :return: valor do produto com o desconto da taxa em cima do preço
    '''
    valor = preco - (preco * taxa / 100)  # valor também é escopo local
    return valor if formatado is False else moeda(valor)


def dobro(preco=0, formatado=False):
    '''
    -> preço x 2
    :param preco: o preço do produto
    :param formatado: formatação da moeda com troca do ponto final pela vírgula,
    adicionando duas casas decimais e R$ como parâmetro não-obrigatório.
    :return: o valor do dobro do preço do produto
    '''
    valor = preco * 2
    return valor if formatado is False else moeda(valor)


def metade(preco=0, formatado=False):
    '''
    -> preço / 2
    :param preco: o preço do produto
    :param formatado: formatação da moeda com troca do ponto final pela vírgula,
    adicionando duas casas decimais e R$ como parâmetro não-obrigatório.
    :return: o valor da metade do preço do produto
    '''
    valor = preco / 2
    return valor if formatado is False else moeda(valor)


def moeda(preco=0, moeda='R$'):  # moeda função // moeda parâmetro
    '''
    -> formatação de moeda
    :param preco: o preço do produto
    :param moeda: moeda corrente escolhida. caso nada seja informado, R$ será mostrado
    :return: formatação da moeda com troca do ponto final pela vírgula,
    adicionando duas casas decimais e R$ como parâmetro não-obrigatório.
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')
