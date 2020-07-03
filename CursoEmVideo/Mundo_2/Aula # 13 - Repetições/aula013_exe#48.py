# pegar todos os números múltiplos de 3 de 1 até 500 e somar todos
soma = 0 # coloca o 0 para definr a variável (acumulador)
cont = 0 # contador
for contagem in range (1, 501):
    if contagem % 3 == 0:
        cont = cont + 1 # um contador, geralmente conta mais um
        soma = soma + contagem # acumulador acumula valores (soma, multiplicação, etc)
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
