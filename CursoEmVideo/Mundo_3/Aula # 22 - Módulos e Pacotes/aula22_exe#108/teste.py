import moeda

preco = float(input('Digite o preço: R$'))
taxa = int(input('Quantos porcentos de taxa: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
# moeda.moeda() é o módulo
# moeda.função moeda
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
# não tem problema colocar uma função dentro da outra. Por isso que a função do dobro entra na moeda
# a moeda() formata os valores retornados nas demais funções
print(f'O valor {moeda.moeda(preco)} com o acréscimo de {taxa}% fica {moeda.moeda(moeda.aumentar(preco, taxa))}')
print(f'O valor {moeda.moeda(preco)} com desconto de {taxa}% fica {moeda.moeda(moeda.diminuir(preco, taxa))}')