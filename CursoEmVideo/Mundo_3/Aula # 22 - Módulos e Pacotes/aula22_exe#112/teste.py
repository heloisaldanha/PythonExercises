from utilidadesCeV import moeda
from utilidadesCeV import dado
preco = dado.leiaDinheiro('Digite o preço: R$')
taxa = int(input('Quantos porcentos de taxa?: '))
moeda.resumo(preco, taxa)
