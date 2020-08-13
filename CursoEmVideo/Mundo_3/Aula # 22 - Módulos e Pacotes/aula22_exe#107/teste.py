import moeda

preco = float(input('Digite o preço: R$'))
taxa = int(input('Quantos porcentos de taxa: '))
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}')
print(f'O valor R${preco:.2f} com o acréscimo de {taxa}% fica R${moeda.aumentar(preco, taxa):.2f}')
print(f'O valor R${preco:.2f} com desconto de {taxa}% fica R${moeda.diminuir(preco, taxa):.2f}')