import moeda

preco = float(input('Digite o preço: R$'))
taxa = int(input('Quantos porcentos de taxa: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
# moeda.moeda() é o módulo
# moeda.função moeda
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
# não tem problema colocar uma função dentro da outra. Por isso que a função do dobro entra na moeda
# a moeda() formata os valores retornados nas demais funções
print(f'O valor {moeda.moeda(preco)} com o acréscimo de {taxa}% fica {moeda.aumentar(preco, taxa, True)}')
print(f'O valor {moeda.moeda(preco)} com desconto de {taxa}% fica {moeda.diminuir(preco, taxa, True)}')