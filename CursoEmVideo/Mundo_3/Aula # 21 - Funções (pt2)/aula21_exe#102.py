'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que inndique o número
a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.
'''

def fatorial(numero, show=False):
    '''

    :param numero: Parâmetro obrigatório. O número dado para calcular o fatorial.
    :param show: Parâmetro não obrigatório, pra saber se mostra ou não o cálculo.
    :return: Retorna o RESULTADO do fatorial do número escolhido.


    '''
    f = 1
    for c in range(numero, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


n = int(input('Número: '))
print(fatorial(n, show=True))
help(fatorial)