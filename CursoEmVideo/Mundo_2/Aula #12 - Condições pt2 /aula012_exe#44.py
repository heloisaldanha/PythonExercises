preço = float(input('Qual o preço do produto? R$'))
print('''Formas de pagamento:
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
resposta = int(input('Escolha a forma de pagamento: '))
if resposta == 1:
    print('O valor do produto é R${:.2f} e à vista no dinheiro ou cheque fica R${:.2f}.'.format(preço, preço - (preço * 0.10)))
    pass
elif resposta == 2:
    print('O valor do produto é R${:.2f} e à vista no cartão sai por R${:.2f}.'.format(preço, preço - (preço * 0.05) ))
elif resposta == 3:
    print('O valor do produto é R${:.2f}.'.format(preço))
    print('O valor da parcela será 2x R${:.2f} SEM JUROS.'.format(preço / 2))
elif resposta == 4:
    total = preço + (preço * 0.20)
    parcelas = int(input('Escolha o número de parcelas (3 a 10x): '))
    valorFinal = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, valorFinal))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
print('\033[7mPRESS COMMAND+R TO EXIT\033[m')


    #print('O valor do produto fica R${:.2f}.'.format(preço + (preço * 0.20)))
    #parctotal = int(input('Digite o número de parcelas: '))
    #parcela = preço + (preço * 0.20) / parctotal
    #print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parctotal, parcela))

