'''
Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços organizando os dados em forma TABULAR.
'''

listagem = ('Celular', 999.99, 'Tablet', 500, 'Notebook', 3000, 'Fone Bluetooth', 200,
            'Câmera digital', 6000, 'PC', 10000)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for tabela in range(0, len(listagem)):
    if tabela % 2 == 0:
        print('{:.<30}'.format(listagem[tabela]), end='')  #  vai pegar tudo que está em listagem nas posições tabela (nas posições pares).
    else:
        print('R${:>8.2f}'.format(listagem[tabela]))
#  Esse > < dentro das chaves de formatação significa pra qual margem ele deve ir, pra margem da direita ou da esquerda.
#  A seta aponta pra qual lado se vai:
#  > vai pra direita
#  < vai pra esquerda
#  Se quiser centralizar, coloca
#  O . é pra preencher espaços vazios com pontos
#  O .2f é pra colocar duas casas decimais (float) depois do ponto

