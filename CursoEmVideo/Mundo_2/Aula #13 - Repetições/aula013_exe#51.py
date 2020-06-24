#progressão aritmética (os dez primeiros números da razão)

termo = int(input('Primeiro Termo: ')) #de onde começa
razao = int(input('Razão: ')) #o que quer pular
décimo = termo + (10 - 1) * razao
for c in range(termo, décimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU')